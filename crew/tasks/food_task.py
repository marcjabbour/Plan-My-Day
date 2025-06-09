from crewai import Task

def get_food_task(food_agent):
    return Task(
        description="Given an array of activities and locations: '{selected_activities}', for each activity, find restaurants near the location. Be as specific as possible with the location. If a preference is specified, include it in the request: {preference}",
        expected_output="A JSON object that has the following format: [{'activity': ..., 'location': ..., 'restaurants': [{'name': ..., 'address': ..., 'rating': ..., 'total_ratings': ...}]}]",
        agent=food_agent,
        input_variables=["selected_activities", "preference"]
    )