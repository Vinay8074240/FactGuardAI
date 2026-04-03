import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from crewai.tools import tool

load_dotenv()

# 1. Initialize the underlying Search Engine
_tavily_engine = TavilySearch(max_results=5)

# 2. Wrap it in a CrewAI-compatible tool
@tool("search_tool")
def search_tool(query: str):
    """
    Search the internet for factual information, news, and primary sources 
    related to a specific claim or topic.
    """
    return _tavily_engine.run(query)

def get_vector_tool(content):
    # Keep your existing vector logic
    return "Vector store updated."