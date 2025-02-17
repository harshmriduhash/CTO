import os
import openai
from ..models import ProjectPlan

openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_project_plan_from_llm(input_text: str) -> ProjectPlan:
    prompt = f"""
    Based on the following project details and user responses, generate a comprehensive project plan:

    {input_text}

    Please provide the following information:
    1. A suitable project title
    2. A brief project description
    3. Recommended tech stack (list of technologies)
    4. Key features to be implemented (list)
    5. Project timeline (dictionary with phases and durations)
    6. Estimated budget

    Format your response as a JSON object with the following keys:
    title, description, tech_stack, features, timeline, budget_estimate
    """

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Parse the JSON response and create a ProjectPlan object
    plan_data = json.loads(response.choices[0].text.strip())
    return ProjectPlan(**plan_data)