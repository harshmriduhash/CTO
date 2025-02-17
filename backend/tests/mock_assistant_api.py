import asyncio
import json
from typing import List, Dict
from pydantic import BaseModel

# Mock user responses
mock_user_responses = [
    "I want to build a mobile app for task management",
    "The app should have user authentication and cloud sync",
    "The target audience is professionals and students",
    "The budget is around $50,000",
    "The timeline is 3 months",
]

# Mock OpenAI Assistant API responses
class MockMessage(BaseModel):
    role: str
    content: List[Dict[str, str]]

class MockRun(BaseModel):
    id: str
    status: str

class MockThread(BaseModel):
    id: str

class MockAssistant:
    def __init__(self):
        self.thread_id = "mock_thread_123"
        self.run_id = "mock_run_456"

    async def create_thread(self):
        return MockThread(id=self.thread_id)

    async def add_message(self, thread_id: str, content: str):
        print(f"Added message to thread {thread_id}: {content}")

    async def run_assistant(self, thread_id: str):
        return MockRun(id=self.run_id, status="queued")

    async def get_run_status(self, thread_id: str, run_id: str):
        return MockRun(id=run_id, status="completed")

    async def get_messages(self, thread_id: str):
        return [
            MockMessage(
                role="assistant",
                content=[{
                    "type": "text",
                    "text": json.dumps({
                        "title": "Task Management Mobile App",
                        "description": "A mobile application for efficient task management, targeting professionals and students.",
                        "tech_stack": ["React Native", "Node.js", "MongoDB"],
                        "features": [
                            "User authentication",
                            "Cloud synchronization",
                            "Task creation and management",
                            "Priority setting",
                            "Reminders and notifications"
                        ],
                        "timeline": {
                            "Planning and Design": "2 weeks",
                            "Development": "8 weeks",
                            "Testing and QA": "2 weeks",
                            "Deployment": "1 week"
                        },
                        "budget_estimate": 45000,
                        "product_requirements": "The app should provide a seamless user experience for creating, organizing, and tracking tasks. It should include features such as user authentication, cloud synchronization, task creation and management, priority setting, and reminders.",
                        "job_description": "We are seeking a skilled mobile app developer with experience in React Native and Node.js. The ideal candidate should have a strong understanding of user authentication, cloud synchronization, and building intuitive user interfaces.",
                        "required_skills": [
                            "React Native",
                            "Node.js",
                            "MongoDB",
                            "RESTful API development",
                            "User authentication and security",
                            "Cloud synchronization",
                            "Mobile UI/UX design principles"
                        ]
                    })
                }]
            )
        ]

async def process_questionnaire_with_assistant(responses: List[str]):
    assistant = MockAssistant()
    
    # Create a new thread
    thread = await assistant.create_thread()
    
    # Add user messages to the thread
    for response in responses:
        await assistant.add_message(thread.id, response)
    
    # Run the assistant
    run = await assistant.run_assistant(thread.id)
    
    # Wait for the run to complete
    while True:
        run_status = await assistant.get_run_status(thread.id, run.id)
        if run_status.status == "completed":
            break
        await asyncio.sleep(1)
    
    # Get the final messages
    messages = await assistant.get_messages(thread.id)
    
    # Extract and parse the project plan
    project_plan = json.loads(messages[-1].content[0]["text"])
    return project_plan

async def main():
    project_plan = await process_questionnaire_with_assistant(mock_user_responses)
    print("Generated Project Plan:")
    print(json.dumps(project_plan, indent=2))

if __name__ == "__main__":
    asyncio.run(main())

# To run this test:
# 1. Make sure you're in the backend directory
# 2. Run the following command in your terminal:
#    python -m tests.mock_assistant_api
#
# This will execute the main() function, which simulates the questionnaire process
# using the mock responses and prints the generated project plan.

if __name__ == "__main__":
    asyncio.run(main())