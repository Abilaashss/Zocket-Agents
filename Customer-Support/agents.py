import warnings
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import HuggingFaceHub
from langchain_community.llms import Ollama
from langchain_together import ChatTogether
import os
from dotenv import load_dotenv
load_dotenv()

llm = Ollama(model = "gemma2:2b")

hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")

# llm = HuggingFaceHub(
#     repo_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
#     api_key = hugging_face_api_key,
#     task="text-generation",
# )


def planner_agent():
    planner = Agent(
        role = "Content Planner",
        goal = "Plan factual and accurate content on Artificial Intelligence",
        backstory = "You are working on planning a blog article"
                    "you give a detailed outline on Artificial Intelligence"
                    "you cover information that helps the "
                    "audience learn something effectively"
                    "and make informed decisions"
                    "your work is the basis for content writer"
                    "to write a detailed article on this topic.",
        allow_delegations = False,
        verbose = True,
        llm = llm


    )

    return planner

def writer_agent():
    writer = Agent(
        role = "Content Writer",
        goal = "Write factual and accurate opinion piece about Artificial Intelligence",
        backstory = "You write a detailed blog article "
                    "based on the outline given by content planner"
                    "with detailed explanations of each topic in an engaging manner"
                    "you follow the main objectives and directions of the outline.",
        allow_delegations = False,
        verbose = True,
        llm = llm

        
    )

    return writer

def editor_agent():
    editor = Agent(
        role = "Content Editor",
        goal = "Edit a given blog article to align"
                "with the writing style of the organisation",
        backstory = "You are an editor who receives a blog post"
                    "from the content writer"
                    "your goal is to review the blog post"
                    "to ensure that it doesnt have any grammatical errors,"
                    "provides balanced viewpoints,"
                    "avoids major controversial topics.",
        allow_delegations = False,
        verbose = True,
        llm = llm
    )

    return editor

