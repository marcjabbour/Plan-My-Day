from crewai import Agent

planner_agent = Agent(
    name="Intent Planner",
    role="You are a helpful assistant that orchestrates the planning flow.",
    goal="Tell me whether or not I should go outside today.",
    backstory="A proactive assistent that understands the weather and gives recommendations",
    allow_delegation=True
)


# Future Implementation

# planner = Agent(
#     name="Intent Planner",
#     role="You are a helpful assistant that orchestrates the planning flow.",
#     goal="Create a fun, well-scheduled plan for the user's day.",
#     backstory="A proactive assistent that understands goals and delegates tasks.",
#     allow_delegation=True
# )