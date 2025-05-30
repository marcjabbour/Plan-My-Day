from crewai.tools import tool
from datetime import datetime, timedelta
import dateparser

@tool("Convert natural language date to YYYY-MM-DD")
def resolve_date(relative_date: str) -> str:
    """
    Converts natural language like 'next Friday' or 'this Saturday' into a YYYY-MM-DD date.
    """
    parsed = dateparser.parse(relative_date, settings={"PREFER_DATES_FROM": "future"})
    if not parsed:
        return "Invalid date"
    return parsed.strftime("%Y-%m-%d")