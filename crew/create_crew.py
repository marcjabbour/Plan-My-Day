from crewai import Crew, Agent, Task
from crew.weather_agent import weather_agent
from crew.planner_agent import planner_agent
from crew.tasks.food_task import get_food_task
from crew.activity_agent import activity_agent
from crew.food_agent import food_agent
# from crew.schedule_agent import schedule_agent

def create_planner_crew():

    ### WEATHER TASK ###
    weather_task = Task(
        description=(
            "Given a user's prompt: '{topic}', use the DateResolverTool to resolve relative dates "
            "like 'Saturday' into YYYY-MM-DD, and then use the WeatherTool to get the weather "
            "for that day in the specified location."
        ),
        agent=weather_agent,
        expected_output="The weather forecast in natural language for the given place and date.",
        input_variables=["topic"]
    )

    ### ACTIVITY TASK ###
    activity_task = Task(
        description=(
            "Using Tavily-MCP, find 3-5 current fun activities in the user's city "
            "based on the weather for that day determined by the weather agent. Be specific and suggest exact locations. Consider any other details relayed in the user's prompt: '{topic}'."
        ),
        agent=activity_agent,
        expected_output=("A JSON object with this structure: { 'intro': ..., 'activities': ..., 'outro'..., 'extra_info': ... }. "
        "The intro field should be a natural language explanation of the activities. "
        "The activities field should be a list of activities followed by a brief description of each activity. It should follow the format: "
        "[ { 'name': ..., 'description': ...}, { 'name': ..., 'description': ...}, { 'name': ..., 'description': ...} ] "
        "The outro field should be a natural language summary of the activities that acknolwedges the weather and other details relayed by the user. "
        "The extra-info field should provide information about the suggested activities, and it must be a JSON object with this structure: [{'name': ..., 'location': ...}]"
        "If the activity doesn't have a location, don't include it in the array of activities and locations."),
        input_variables=["topic"]
    )

    planner_crew = Crew(
        agents=[weather_agent, activity_agent],
        tasks=[weather_task, activity_task],
        max_iterations=3,
        verbose=True
    )

    return planner_crew


def create_food_crew():

    food_task = get_food_task(food_agent)
    food_crew = Crew(agents=[food_agent], tasks=[food_task], max_iterations=3)
    return food_crew