import { Question } from '@/types'

export const questionnaire: Question[] = [
  {
    "question": "What best describes the primary goal of your project?",
    "options": [
      "Develop a new product/service",
      "Improve an existing product/service",
      "Automate internal processes",
      "Expand to new markets",
      "Other (please specify)"
    ],
    "tooltip": "Choose the option that most closely aligns with your project's main objective."
  },
  {
    "question": "Who is your target audience?",
    "options": [
      "Consumers (B2C)",
      "Businesses (B2B)",
      "Government",
      "Non-profit organizations",
      "Internal employees"
    ],
    "tooltip": "Select the primary group of users or customers your project aims to serve."
  },
  {
    "question": "What type of application do you need?",
    "options": [
      "Web application only",
      "Mobile application only",
      "Both web and mobile applications",
      "Desktop application",
      "Not sure"
    ],
    "tooltip": "Choose the platform(s) on which your application will run."
  },
  {
    "question": "What is your expected user base size in the first year?",
    "options": [
      "Less than 1,000 users",
      "1,000 - 10,000 users",
      "10,000 - 100,000 users",
      "100,000 - 1 million users",
      "More than 1 million users"
    ],
    "tooltip": "Estimate the number of users you expect to have within the first year of launch."
  },
  {
    "question": "Which of the following best describes your project's core functionality?",
    "options": [
      "E-commerce platform",
      "Social networking",
      "Content management system",
      "Data analytics and visualization",
      "IoT and device management",
      "Other (please specify)"
    ],
    "tooltip": "Select the primary function or purpose of your application."
  }
]