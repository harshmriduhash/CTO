# Purpose: Initialize OpenAI Assistant
# Key functions: Create assistant with custom instructions
# Output: Assistant ID for project plan generation

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_assistant():
    function_signatures = [
        {
            "name": "generate_project_plan",
            "description": "Generate a comprehensive project plan based on questionnaire responses",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Project title"},
                    "description": {"type": "string", "description": "Brief project description"},
                    "tech_stack": {"type": "array", "items": {"type": "string"}, "description": "List of recommended technologies"},
                    "features": {"type": "array", "items": {"type": "string"}, "description": "List of key features to be implemented"},
                    "budget_estimate": {"type": "number", "description": "Estimated project budget"},
                    "product_requirements": {"type": "string", "description": "Detailed product requirements"},
                    "job_description": {"type": "string", "description": "Job description for key roles"},
                    "required_skills": {"type": "array", "items": {"type": "string"}, "description": "List of required skills for the project team"},
                },
                "required": [
                    "title", "description", "tech_stack", "features", "budget_estimate",
                    "product_requirements", "job_description", "required_skills"
                ],
                "additionalProperties": False
            },
            "strict": True
        }
    ]

    instructions = """
    You are an AI CTO assistant designed to help generate project plans based on questionnaire responses. Your role is to analyze the information provided and create comprehensive project plans that include:

    1. A suitable project title
    2. A brief project description
    3. Recommended tech stack (list of technologies)
    4. Key features to be implemented (list)
    5. Estimated budget
    6. Product requirements
    7. Job description for key roles
    8. Required skills for the project team

    When generating project plans, consider factors such as scalability, security, user experience, and industry best practices. Provide clear and actionable insights that will help guide the development process.
    """

    assistant = client.beta.assistants.create(
        name="AI CTO Assistant",
        instructions=instructions,
        tools=[
            {"type": "function", "function": signature}
            for signature in function_signatures
        ],
        model="gpt-4-0125-preview"
    )
    return assistant

def main():
    assistant_object = create_assistant()
    if assistant_object:
        print("Assistant initialized successfully.")
        print("Please add the following line to your .env file:")
        print(f"OPENAI_ASSISTANT_ID={assistant_object.id}")
    else:
        print("Failed to initialize assistant.")

if __name__ == "__main__":
    main()