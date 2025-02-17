import { QuestionnaireResponse, ProjectPlan, Questionnaire, AIProjectDetails, JobPosting } from '@/types'
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

if (!supabaseUrl || !supabaseAnonKey) {
  throw new Error('Supabase URL and Anon Key must be provided')
}

const supabase = createClient(supabaseUrl, supabaseAnonKey)

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function submitQuestionnaire(data: QuestionnaireResponse): Promise<AIProjectDetails> {
  const response = await fetch(`${API_URL}/api/v1/questionnaire`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Failed to submit questionnaire')
  }

  return response.json()
}

export async function getQuestionnaire(id: number): Promise<Questionnaire> {
  const { data, error } = await supabase
    .from('questionnaires')
    .select('*')
    .eq('id', id)
    .single()

  if (error) throw error

  return data
}

export async function createJobPosting(data: Omit<JobPosting, 'id' | 'status'>): Promise<JobPosting> {
  const response = await fetch(`${API_URL}/api/v1/job-postings`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  if (!response.ok) {
    throw new Error('Failed to create job posting')
  }

  return response.json()
}