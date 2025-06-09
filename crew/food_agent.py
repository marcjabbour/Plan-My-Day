from crewai import Agent
from tools.food_tool import food_tool

food_agent = Agent(
    name="Food Agent",
    role="Recommends restaurants near selected activities",
    goal="Help users find great places to eat near their selected destinations.",
    backstory="A helpful food expert with access to real-time Google Maps data.",
    tools=[food_tool], 
    allow_delegation=False
)
