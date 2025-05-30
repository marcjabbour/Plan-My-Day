import pytest
from unittest.mock import patch, MagicMock
from tools.weather_tool import get_weather_forecast


def mock_response(json_data, status=200):
    mock_resp = MagicMock()
    mock_resp.status_code = status
    mock_resp.json.return_value = json_data
    return mock_resp

@patch('tools.weather_tool.requests.get')
def test_get_weather_forecast_valid(mock_get):
    mock_data = {
        "list": [
            {
                "dt_txt": "2024-06-14 12:00:00",
                "weather": [{"description": "clear sky"}],
                "main": {"temp": 25}
            }
        ]
    }
    mock_get.return_value = mock_response(mock_data)
    result = get_weather_forecast.run("New York", "2024-06-14")
    assert result == "Forecast: clear sky, 25°C"

@patch('tools.weather_tool.requests.get')
def test_get_weather_forecast_no_forecast(mock_get):
    mock_data = {"list": [
        {"dt_txt": "2024-06-15 12:00:00", "weather": [{"description": "rain"}], "main": {"temp": 18}}
    ]}
    mock_get.return_value = mock_response(mock_data)
    result = get_weather_forecast.run("New York", "2024-06-14")
    assert result == "No forecast data found for this date"

@patch('tools.weather_tool.requests.get')
def test_get_weather_forecast_invalid_response(mock_get):
    mock_data = {}
    mock_get.return_value = mock_response(mock_data)
    with pytest.raises(KeyError):
        # This will raise because 'list' is missing
        get_weather_forecast.run("New York", "2024-06-14") 