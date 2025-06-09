from mcp.mcp_client import MCPClient

def test_tavily_search():
    mcp = MCPClient()
    query = "fun things to do in Brooklyn this weekend"
    response = mcp.call("tavily", "tavily-search", {"query": query})
    print("✅ MCP response:", response)

if __name__ == "__main__":
    test_tavily_search()