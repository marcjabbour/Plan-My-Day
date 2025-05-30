import pytest
from tools.date_resolver_tool import resolve_date
from datetime import datetime, timedelta


def test_resolve_date_today():
    today = datetime.now().strftime("%Y-%m-%d")
    assert resolve_date.run("today") == today

def test_resolve_date_tomorrow():
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert resolve_date.run("tomorrow") == tomorrow

def test_resolve_date_next_friday():
    # This is a bit tricky because 'next Friday' depends on today
    result = resolve_date.run("next Friday")
    assert len(result) == 10  # Should be in YYYY-MM-DD format
    assert result.count('-') == 2

def test_resolve_date_this_saturday():
    result = resolve_date.run("this Saturday")
    assert len(result) == 10
    assert result.count('-') == 2

def test_resolve_date_specific_date():
    assert resolve_date.run("January 1, 2025") == "2025-01-01"

def test_resolve_date_invalid():
    assert resolve_date.run("not a date") == "Invalid date"

def test_resolve_date_empty():
    assert resolve_date.run("") == "Invalid date" 