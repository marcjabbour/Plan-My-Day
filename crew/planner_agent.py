from crewai import Agent

planner_agent = Agent(
    name="Intent Planner",
    role="You are a helpful assistant that orchestrates the planning flow.",
    goal="Recommend a fun, well-scheduled plan for the user's day based on the weather and other details relayed by the user.",
    backstory="A proactive assistent that understands the weather and gives recommendations",
    allow_delegation=True
)