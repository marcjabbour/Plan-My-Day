######## DEPRECATED ########

# from crewai.tools import tool
# from mcp.mcp_client import MCPClient

# @tool
# def invoke_web_activity_rag_tool(query: str) -> str:
#     """Searches the web and summarizes activities using RAG for the given query."""
#     mcp = MCPClient()
#     return mcp.call("tavily", "tavily-search", {"query": query})