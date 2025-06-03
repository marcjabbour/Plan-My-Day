from crewai import Agent
from tools.web_search_and_scrape_tool import invoke_web_activity_rag_tool

activity_agent = Agent(
    name="Activity Agent",
    role="Suggests activities based on weather and location",
    goal="Recommend fun things to do in a specific city based on web search, and other details relayed by the user. Acknowledge the weather.",
    backstory="An always-up-to-date local expert who knows what’s worth doing right now.",
    tools=[invoke_web_activity_rag_tool],
    allow_delegation=False
)