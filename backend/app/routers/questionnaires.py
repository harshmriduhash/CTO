# Purpose: Handle questionnaire submission
# Key functions: Store responses in Supabase, process with AI assistant
# Output: Generated project plan

from fastapi import APIRouter, HTTPException, Depends
from ..models import QuestionnaireResponse, ProjectPlan
from ..services.assistant import process_questionnaire_with_assistant
from ..database import get_supabase
from supabase import Client

router = APIRouter()

@router.post("/questionnaire", response_model=ProjectPlan)
async def submit_questionnaire(response: QuestionnaireResponse, supabase: Client = Depends(get_supabase)):
    try:
        # Store the questionnaire response in Supabase
        result = supabase.table("questionnaire_responses").insert({
            "questionnaire_id": response.questionnaire.id,
            "answers": [answer.dict() for answer in response.user_responses]
        }).execute()

        if not result.data:
            raise HTTPException(status_code=500, detail="Failed to store questionnaire response")

        # Process the questionnaire with the assistant
        project_plan = await process_questionnaire_with_assistant(response)

        return project_plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))