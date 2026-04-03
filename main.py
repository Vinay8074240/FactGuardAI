from crewai import Crew, Process
from agents import researcher, analyst, critic
from tasks import research_task, analysis_task, validation_task

def run_fact_checker(user_claim):
    fact_guard_crew = Crew(
        agents=[researcher, analyst, critic],
        tasks=[research_task, analysis_task, validation_task],
        process=Process.sequential, # Agentic Workflow Pattern
        verbose=True
    )
    
    result = fact_guard_crew.kickoff(inputs={'claim': user_claim})
    return result