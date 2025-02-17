import os
from fastapi import FastAPI
from .routers import questionnaires
from fastapi.middleware.cors import CORSMiddleware
from .database import get_supabase
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Debug print environment variables
logger.debug(f"SUPABASE_URL: {os.getenv('SUPABASE_URL')}")
logger.debug(f"SUPABASE_KEY: {'*' * len(os.getenv('SUPABASE_KEY', ''))} (masked)")
logger.debug(f"OPENAI_API_KEY: {'*' * len(os.getenv('OPENAI_API_KEY', ''))} (masked)")
logger.debug(f"OPENAI_ASSISTANT_ID: {os.getenv('OPENAI_ASSISTANT_ID')}")

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questionnaires.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    supabase = get_supabase()
    # You can add any additional startup checks here
    logger.info("Application started")