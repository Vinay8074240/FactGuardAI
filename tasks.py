from agents import researcher, analyst, critic
from crewai import Task

research_task = Task(
    description="Search for 5 high-quality sources regarding: {claim}",
    agent=researcher,
    expected_output="A summary of facts found from search results."
)

analysis_task = Task(
    description="Format the facts into bullet points and verify they match the sources.",
    agent=analyst,
    expected_output="A structured list of verified facts."
)

validation_task = Task(
    description="Compare the analysis against the original claim. Flag any inconsistencies.",
    agent=critic,
    expected_output="A final verified report with a 'Confidence Score' from 0-100."
)