import warnings
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import HuggingFaceHub
from langchain_community.llms import Ollama
from langchain_together import ChatTogether
import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from crewai import LLM

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool


load_dotenv()

# llm = Ollama(model = "gemma2:2b")

hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")


llm = LLM(
    model="huggingface/mistralai/Mistral-7B-Instruct-v0.3"
)

def support_agent():
    support_agent = Agent(
    role="Senior Support Representative",
	goal="Be the most friendly and helpful "
        "support representative in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        " are now working on providing "
		"support to {customer}, a super important customer "
        " for your company."
		"You need to make sure that you provide the best support!"
		"Make sure to provide full complete answers, "
        " and make no assumptions."
	),
	allow_delegation=False,
	verbose=True,
    llm = llm
)
    
    return support_agent


def quality_assurance_agent():
    support_quality_assurance_agent = Agent(
	role="Support Quality Assurance Specialist",
	goal="Get recognition for providing the "
    "best support quality assurance in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        "are now working with your team "
		"on a request from {customer} ensuring that "
        "the support representative is "
		"providing the best support possible.\n"
		"You need to make sure that the support representative "
        "is providing full"
		"complete answers, and make no assumptions."
	),
	verbose=True,
    llm = llm
)
    
    return support_quality_assurance_agent



def initialise_tool():
    docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)
    
    return docs_scrape_tool










