#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p logs

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Start the backend server
echo "Starting backend..."
cd backend
if command_exists av; then
    av
else
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        echo "Virtual environment not found. Creating one..."
        python3 -m venv venv
        source venv/bin/activate
    fi
fi

# Install requirements
pip install -r requirements.txt

if command_exists uvicorn; then
    uvicorn app.main:app --reload --port 8000 > ../logs/backend.log 2>&1 &
else
    echo "Error: uvicorn not found. Please install it using 'pip install uvicorn'."
    exit 1
fi
BACKEND_PID=$!
cd ..

# Start the frontend development server
echo "Starting frontend..."
cd frontend
if command_exists npm; then
    npm install
    npm install @supabase/supabase-js
    # Load environment variables
    set -a
    source .env
    set +a
    npm run dev > ../logs/frontend.log 2>&1 &
else
    echo "Error: npm not found. Please install Node.js and npm."
    exit 1
fi
FRONTEND_PID=$!
cd ..

# Function to stop all processes
cleanup() {
    echo "Stopping all processes..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

# Set up trap to call cleanup function on script exit
trap cleanup EXIT

echo "Both frontend and backend are running. Check logs directory for output."
echo "Press Ctrl+C to stop all processes."

# Wait for user input
wait