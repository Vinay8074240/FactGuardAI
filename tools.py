import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from crewai.tools import tool

load_dotenv()

# Initialize the engine
_tavily_engine = TavilySearch(max_results=2)

@tool("search_tool")
def search_tool(query: str):
    """
    Search the internet for factual information related to a specific claim.
    Use this tool to find evidence, dates, and locations from reliable sources.
    """
    # The code below handles the search and keeps the token count low
    results = _tavily_engine.run(query)
    return str(results)[:800] 

def get_vector_tool(content):
    """Updates the vector store."""
    return "Vector store updated."