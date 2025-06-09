from crewai.tools import tool

import os
import requests
from dotenv import load_dotenv
load_dotenv()

@tool("Find Restaurants Near Location")
def food_tool(location: str, preference: str = "") -> list:
    """Find restaurants near a given location"""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    query = f"{preference} restaurants near {location}" if preference else f"restaurants near {location}"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"
    response = requests.get(url)
    results = response.json().get("results", [])
    return [{
        "name": r.get("name"),
        "address": r.get("formatted_address"),
        "rating": r.get("rating"),
        "total_ratings": r.get("user_ratings_total")
    } for r in results[:5]]