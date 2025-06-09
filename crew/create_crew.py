from crewai import Crew, Agent
from crew.weather_agent import weather_agent
from crew.planner_agent import planner_agent
from crew.tasks.planner_task import get_planner_task
from crew.tasks.weather_task import get_weather_task
from crew.tasks.activity_task import get_activity_task
from crew.tasks.food_task import get_food_task
from crew.activity_agent import activity_agent
from crew.food_agent import food_agent
# from crew.schedule_agent import schedule_agent

def create_planner_crew():

    planner_task = get_planner_task(planner_agent)
    weather_task = get_weather_task(weather_agent)
    activity_task = get_activity_task(activity_agent)

    planner_crew = Crew(
        agents=[planner_agent, weather_agent, activity_agent],
        tasks=[planner_task, weather_task, activity_task],
        max_iterations=3
    )

    return planner_crew


def create_food_crew():

    food_task = get_food_task(food_agent)
    food_crew = Crew(agents=[food_agent], tasks=[food_task], max_iterations=3)
    return food_crew