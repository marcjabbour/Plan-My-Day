from crewai import Task

def get_weather_task(weather_agent):
    return Task(
        description=(
            "Given a user's prompt: '{topic}', use the DateResolverTool to resolve relative dates "
            "like 'Saturday' into YYYY-MM-DD, and then use the WeatherTool to get the weather "
            "for that day in the specified location."
        ),
        agent=weather_agent,
        expected_output="The weather forecast in natural language for the given place and date.",
        input_variables=["topic"]
    )