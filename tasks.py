from agents import researcher, analyst, critic
from crewai import Task

research_task = Task(
    description=(
        "Research the claim: '{claim}'. "
        "Find exactly 2-3 key facts. "
        "DO NOT provide long descriptions. Output must be under 150 words."
    ),
    expected_output="A bulleted list of 3 concise facts with sources.",
    agent=researcher
)

analysis_task = Task(
    description="Summarize the facts provided by the researcher into 2 sentences.",
    expected_output="A 2-sentence factual summary.",
    agent=analyst,
    context=[research_task]
)

validation_task = Task(
    description=(
        "1. Take the structured facts from the Analyst.\n"
        "2. Compare them against the original claim: '{claim}'.\n"
        "3. Identify if the claim is 'Verified', 'Partially Verified', or 'False'.\n"
        "4. Provide a final confidence score (0-100%)."
    ),
    expected_output="A final verified report comparing the facts to the original claim '{claim}'.",
    agent=critic
)