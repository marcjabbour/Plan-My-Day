from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

server_params = StdioServerParameters(
    command="env",
    args=["npx", "-y", "tavily-mcp@0.2.3"],
)

with MCPServerAdapter(server_params) as tavily_tools:
    print("Tools available:", [tool.name for tool in tavily_tools])
    activity_agent = Agent(
        name="Activity Agent",
        role="Suggests activities based on weather and location",
        goal=(
            "Recommend fun things to do in a specific city based on web search, and other details relayed by the user. Be specific and concise. Acknowledge the weather."
        ),
        backstory="An always-up-to-date local expert who knows what’s worth doing right now.",
        tools=list(tavily_tools),
        allow_delegation=False
    )