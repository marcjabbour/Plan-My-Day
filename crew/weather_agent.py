from crewai import Agent
from tools.weather_tool import get_weather_forecast
from tools.date_resolver_tool import resolve_date

weather_agent = Agent(
    name="Weather Agent",
    role="Weather forecaster for specific locations and days",
    goal="Get the accurate weather for a given day and location",
    backstory="A reliable weather assistant that uses official sources to help with day planning.",
    tools=[resolve_date,get_weather_forecast],
    allow_delegation=False
)