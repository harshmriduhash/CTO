# Purpose: Interact with OpenAI Assistant API
# Key functions: Process questionnaire, manage assistant runs, handle responses
# Output: Structured project plan

import asyncio
import json
import logging
import os
from openai import OpenAI
from pydantic import BaseModel
from ..models import QuestionnaireResponse, ProjectPlan
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Debug print environment variables
logger.debug(f"OPENAI_API_KEY: {'*' * len(os.getenv('OPENAI_API_KEY', ''))} (masked)")
logger.debug(f"OPENAI_ASSISTANT_ID: {os.getenv('OPENAI_ASSISTANT_ID')}")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY environment variable is not set")
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

if not ASSISTANT_ID:
    logger.error("OPENAI_ASSISTANT_ID environment variable is not set")
    raise ValueError("OPENAI_ASSISTANT_ID environment variable is not set")

class Conversation(BaseModel):
    thread_id: str = None
    last_response: str = None

async def process_questionnaire_with_assistant(response: QuestionnaireResponse) -> ProjectPlan:
    conversation = Conversation()

    try:
        if not conversation.thread_id:
            thread = client.beta.threads.create()
            conversation.thread_id = thread.id

        message_content = format_questionnaire_response(response)
        await client.beta.threads.messages.create(
            thread_id=conversation.thread_id,
            role="user",
            content=message_content
        )

        run = await client.beta.threads.runs.create(
            thread_id=conversation.thread_id,
            assistant_id=ASSISTANT_ID
        )

        project_plan = await process_run(conversation, run.id)
        return project_plan

    except Exception as e:
        logger.error(f"Error in process_questionnaire_with_assistant: {str(e)}")
        raise

async def process_run(conversation: Conversation, run_id: str) -> ProjectPlan:
    while True:
        run_status = await client.beta.threads.runs.retrieve(
            thread_id=conversation.thread_id,
            run_id=run_id
        )

        if run_status.status == "completed":
            return await process_completed_run(conversation)
        elif run_status.status == "requires_action":
            run = await process_required_actions(conversation, run_status)
        elif run_status.status in ["failed", "cancelled", "expired"]:
            raise Exception(f"Run failed with status: {run_status.status}")

        await asyncio.sleep(1)

async def process_required_actions(conversation: Conversation, run_status):
    tool_outputs = []
    for tool_call in run_status.required_action.submit_tool_outputs.tool_calls:
        if tool_call.function.name == "generate_project_plan":
            project_plan = json.loads(tool_call.function.arguments)
            tool_outputs.append({
                "tool_call_id": tool_call.id,
                "output": json.dumps(project_plan)
            })

    return await client.beta.threads.runs.submit_tool_outputs(
        thread_id=conversation.thread_id,
        run_id=run_status.id,
        tool_outputs=tool_outputs
    )

async def process_completed_run(conversation: Conversation) -> ProjectPlan:
    messages = await client.beta.threads.messages.list(thread_id=conversation.thread_id)
    for message in messages.data:
        if message.role == "assistant":
            for content in message.content:
                if content.type == "text":
                    project_plan_dict = json.loads(content.text.value)
                    return ProjectPlan(**project_plan_dict)
    raise Exception("No valid response from assistant")

def format_questionnaire_response(response: QuestionnaireResponse) -> str:
    formatted_response = "Questionnaire Responses:\n\n"
    for question, answer in zip(response.questionnaire.questions, response.user_responses):
        formatted_response += f"Q: {question.text}\n"
        formatted_response += f"A: {answer.selected_option_id}\n\n"
    return formatted_response