import os
from dotenv import load_dotenv
from crewai import Agent, LLM  # Import LLM from crewai
from tools import search_tool

load_dotenv()

# Define the Gemini model using the CrewAI LLM wrapper
# This ensures it passes all Pydantic validation checks
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash", 
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5
)

researcher = Agent(
    role='Lead Researcher',
    goal='Uncover factual evidence regarding {claim}',
    backstory='An expert investigative journalist focused on primary sources.',
    tools=[search_tool],
    llm=gemini_llm, 
    allow_delegation=False,
    verbose=True
)

analyst = Agent(
    role='Data Analyst',
    goal='Verify claims against retrieved data.',
    backstory='A meticulous librarian who cross-references everything.',
    llm=gemini_llm, 
    allow_delegation=False,
    verbose=True
)

critic = Agent(
    role='Fact-Check Critic',
    goal='Identify hallucinations or unsourced claims.',
    backstory='A rigorous editor who ensures 100% accuracy.',
    llm=gemini_llm, 
    allow_delegation=True,
    verbose=True
)