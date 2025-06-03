import pytest
from unittest.mock import patch, MagicMock
from tools.web_search_and_scrape_tool import invoke_web_activity_rag_tool

@patch('tools.web_search_and_scrape_tool.MCPClient')
def test_web_activity_rag_tool_valid(mock_mcp_client):
    # Arrange
    mock_instance = mock_mcp_client.return_value
    mock_instance.call.return_value = "Central Park, kayaking, and outdoor concerts are popular in NYC."
    # Act
    result = invoke_web_activity_rag_tool.run("outdoor activities in NYC")
    # Assert
    assert "Central Park" in result
    assert "NYC" in result

@patch('tools.web_search_and_scrape_tool.MCPClient')
def test_web_activity_rag_tool_error(mock_mcp_client):
    # Arrange
    mock_instance = mock_mcp_client.return_value
    mock_instance.call.side_effect = Exception("API error")
    # Act & Assert
    with pytest.raises(Exception) as excinfo:
        invoke_web_activity_rag_tool.run("outdoor activities in NYC")
    assert "API error" in str(excinfo.value)    