from crewai import Agent
from tools.weather_tool import get_weather_forecast
from tools.date_resolver_tool import resolve_date

weather_agent = Agent(
    name="Weather Checker",
    role="Check and report the weather for a given day, which has been resolved by the date resolver tool, and location.",
    goal="Determine where the weather is best catered to indoor our outdoor activities.",
    backstory="A proactive assistent that makes sense of the weather and gives recommendations",
    tools=[resolve_date,get_weather_forecast],
    allow_delegation=False
)