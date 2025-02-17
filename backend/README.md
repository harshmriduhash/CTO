# AI CTO Backend

This backend service powers the AI CTO project, utilizing Python, Supabase, and OpenAI's Assistant API to process questionnaires and generate project plans.

## Technologies Used

- Python 3.9+
- FastAPI
- Supabase
- OpenAI Assistant API

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_ASSISTANT_ID=your_assistant_id
   ```

## Running the Backend

To start the backend server:

```
uvicorn app.main:app --reload
```

The server will start on `http://localhost:8000`.

## OpenAI Assistant API

### Initialization

The OpenAI Assistant is initialized using the `init_assistant.py` script in the `scripts` folder. This script creates an assistant with specific instructions and function calls for project plan generation.

To initialize the assistant:

```
python scripts/init_assistant.py
```

This will create the assistant and provide you with an Assistant ID, which should be set in your `.env` file.

### Thread Management

The `assistant.py` service manages conversations with the OpenAI Assistant using threads. Each questionnaire submission creates a new thread, which is used to generate the project plan.

Key functions:
- `process_questionnaire_with_assistant`: Initiates a new thread and processes the questionnaire
- `process_run`: Manages the assistant run, handling different run statuses
- `process_required_actions`: Handles function calls required by the assistant
- `process_completed_run`: Extracts the final project plan from the completed run

## Database

The project uses Supabase as the database. The schema is defined in `db/schema.sql`. To initialize the database:

```
python scripts/init_supabase.py
```

## API Endpoints

- POST `/api/v1/questionnaire`: Submit a questionnaire and receive a project plan
- POST `/api/v1/job-postings`: Create a new job posting based on the project plan

For more details on the API, run the server and visit `http://localhost:8000/docs` for the Swagger UI documentation.

## Project Structure

```
backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routers/
│   │   └── questionnaires.py
│   └── services/
│       ├── assistant.py
│       ├── project_plan.py
│       └── llm_service.py
├── db/
│   └── schema.sql
├── scripts/
│   ├── init_assistant.py
│   └── init_supabase.py
├── requirements.txt
└── .env
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.