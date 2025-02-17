from ..models import Question, Answer, ProjectPlan
from typing import List
import random

def generate_project_plan(questions: List[Question], answers: List[Answer]) -> ProjectPlan:
    tech_stack = ["React", "FastAPI", "Supabase"]
    features = ["User authentication", "Data storage", "API integration"]
    
    for question, answer in zip(questions, answers):
        selected_option = next(opt for opt in question.options if opt.id == answer.selected_option_id)
        if "mobile" in selected_option.text.lower():
            tech_stack.append("React Native")
        if "e-commerce" in selected_option.text.lower():
            features.append("Payment processing")
    
    timeline = {
        "Planning": "2 weeks",
        "Development": "8 weeks",
        "Testing": "2 weeks",
        "Deployment": "1 week"
    }
    
    total_weeks = sum(int(duration.split()[0]) for duration in timeline.values())
    hourly_rate = random.randint(100, 200)
    budget_estimate = total_weeks * 40 * hourly_rate  # Assuming 40 hours per week
    
    return ProjectPlan(
        title="Custom Software Project",
        description="A tailored software solution based on the client's requirements",
        tech_stack=tech_stack,
        features=features,
        timeline=timeline,
        budget_estimate=budget_estimate
    )