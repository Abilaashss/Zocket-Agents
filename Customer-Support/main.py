from agents import *
from tasks import *
if __name__:

    crew = Crew(
  agents=[support_agent(), quality_assurance_agent()],
  tasks=[inquiry_task(), qa_review_task()],
  verbose=True,
  memory=False
)
    
    inputs = {
    "customer": "DeepLearningAI",
    "person": "Andrew Ng",
    "inquiry": "I need help with setting up a Crew "
               "and kicking it off, specifically "
               "how can I add memory to my crew? "
               "Can you provide guidance?"
}
    result = crew.kickoff(inputs=inputs)

    print(result)

