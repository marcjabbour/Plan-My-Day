from crewai import Task

def get_weather_task(weather_agent):
    return Task(
        description="Use the tools to first resolve the date, then check the weather for that date and city.",
        agent=weather_agent,
        expected_output="The forecast and a recommendation on whether it's good to go outside.",
        async_execution=False
    ) 