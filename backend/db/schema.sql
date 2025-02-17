-- Schema for Supabase initialization

-- Questionnaires table
CREATE TABLE questionnaires (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Questions table
CREATE TABLE questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    questionnaire_id UUID REFERENCES questionnaires(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    order_num INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Question options table
CREATE TABLE question_options (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    question_id UUID REFERENCES questions(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    order_num INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Questionnaire responses table
CREATE TABLE questionnaire_responses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    questionnaire_id UUID REFERENCES questionnaires(id) ON DELETE CASCADE,
    answers JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Project plans table
CREATE TABLE project_plans (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    questionnaire_response_id UUID REFERENCES questionnaire_responses(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    tech_stack JSONB,
    features JSONB,
    timeline JSONB,
    budget_estimate NUMERIC,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- AI-generated project details table
CREATE TABLE ai_project_details (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    questionnaire_response_id UUID REFERENCES questionnaire_responses(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    tech_stack JSONB,
    features JSONB,
    timeline JSONB,
    budget_estimate NUMERIC,
    product_requirements TEXT,
    job_description TEXT,
    required_skills JSONB,
    additional_info JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Job postings table
CREATE TABLE job_postings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ai_project_detail_id UUID REFERENCES ai_project_details(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    required_skills JSONB,
    tech_stack JSONB,
    estimated_budget NUMERIC,
    timeline JSONB,
    status TEXT DEFAULT 'draft',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);