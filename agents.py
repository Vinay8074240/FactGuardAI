import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import search_tool

load_dotenv()

# Initialize the LLM with a slight temperature reduction for more factual consistency
groq_llm = LLM(
    model="groq/llama-3.1-8b-instant", 
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3  # Lower temperature = less "creative" hallucinations
)

researcher = Agent(
    role='Lead Researcher',
    goal='Verify claims with minimal, high-impact facts for {claim}.',
    backstory='You are a concise researcher who values token efficiency.',
    tools=[search_tool],
    llm=groq_llm,
    max_iter=2,      
    allow_delegation=False,
    verbose=True
)

analyst = Agent(
    role='Data Analyst',
    goal='Compare retrieved data against the original claim: {claim}.',
    backstory='A meticulous librarian who cross-references everything.',
    llm=groq_llm, 
    max_iter=2,
    allow_delegation=False,
    verbose=True
)

critic = Agent(
    role='Fact-Check Critic',
    goal='Finalize the report for {claim} and ensure 100% accuracy.',
    backstory='A rigorous editor who ensures no hallucinations exist.',
    llm=groq_llm, 
    max_iter=2,
    allow_delegation=False, # Changed to False to save tokens/time
    verbose=True
)