from pydantic import BaseModel
from typing import List, Optional, Dict

class QuestionOption(BaseModel):
    id: int
    text: str

class Question(BaseModel):
    id: int
    text: str
    options: List[QuestionOption]
    tooltip: str

class Answer(BaseModel):
    question_id: int
    selected_option_id: int

class Questionnaire(BaseModel):
    id: Optional[int]
    title: str
    description: str
    questions: List[Question]

class UserResponse(BaseModel):
    questionnaire_id: int
    answers: List[Answer]

class ProjectPlan(BaseModel):
    title: str
    description: str
    tech_stack: List[str]
    features: List[str]
    timeline: Dict[str, str]
    budget_estimate: float

class QuestionnaireResponse(BaseModel):
    questionnaire: Questionnaire
    user_responses: List[Answer]

class AIProjectDetails(BaseModel):
    id: Optional[str]
    questionnaire_response_id: str
    title: str
    description: str
    tech_stack: List[str]
    features: List[str]
    timeline: Dict[str, str]
    budget_estimate: float
    product_requirements: str
    job_description: str
    required_skills: List[str]
    additional_info: Dict[str, str]

class JobPosting(BaseModel):
    id: Optional[str]
    ai_project_detail_id: str
    title: str
    description: str
    required_skills: List[str]
    tech_stack: List[str]
    estimated_budget: float
    timeline: Dict[str, str]
    status: str = 'draft'