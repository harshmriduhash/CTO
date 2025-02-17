export interface QuestionOption {
  id: number;
  text: string;
}

export interface Question {
  id: number;
  text: string;
  options: QuestionOption[];
  tooltip: string;
}

export interface Answer {
  question_id: number;
  selected_option_id: number;
}

export interface Questionnaire {
  id?: number;
  title: string;
  description: string;
  questions: Question[];
}

export interface UserResponse {
  questionnaire_id: number;
  answers: Answer[];
}

export interface ProjectPlan {
  title: string;
  description: string;
  tech_stack: string[];
  features: string[];
  timeline: Record<string, string>;
  budget_estimate: number;
}

export interface QuestionnaireResponse {
  questionnaire: Questionnaire;
  user_responses: Answer[];
}

// Add the AIProjectDetails interface
export interface AIProjectDetails {
  id?: string;
  questionnaire_response_id: string;
  title: string;
  description: string;
  tech_stack: string[];
  features: string[];
  timeline: Record<string, string>;
  budget_estimate: number;
  product_requirements: string;
  job_description: string;
  required_skills: string[];
  additional_info: Record<string, string>;
}

// Add the JobPosting interface
export interface JobPosting {
  id?: string;
  ai_project_detail_id: string;
  title: string;
  description: string;
  required_skills: string[];
  tech_stack: string[];
  estimated_budget: number;
  timeline: Record<string, string>;
  status: 'draft' | 'published' | 'closed';
}