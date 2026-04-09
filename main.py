from crewai import Crew, Process
from agents import researcher, analyst, critic
from tasks import research_task, analysis_task, validation_task

def run_fact_checker(user_claim):
    fact_guard_crew = Crew(
    agents=[researcher, analyst, critic],
    tasks=[research_task, analysis_task, validation_task],
    process=Process.sequential,
    verbose=True,
    memory=False,      # Prevents agents from "remembering" too much unnecessary data
    max_rpm=15,         # Forces a pause between agents to let the Groq "Token Bucket" refill
    cache=False        # Disable cache to prevent large metadata overhead
  )
    
    result = fact_guard_crew.kickoff(inputs={'claim': user_claim})
    return result