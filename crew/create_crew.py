from crewai import Crew, Agent
from crew.weather_agent import weather_agent
from crew.planner_agent import planner_agent
from crew.tasks.planner_task import get_planner_task
from crew.tasks.weather_task import get_weather_task
# from crew.activity_agent import activity_agent
# from crew.food_agent import food_agent
# from crew.schedule_agent import schedule_agent

def create_planner_crew():

    # Future Implementation

    # crew = Crew(
    #     agents=[planner, weather_agent, activity_agent, food_agent, schedule_agent],
    #     tasks=[
    #         {
    #             "agent": planner,
    #             "description": "Parse user prompt, then call weather agent, then activity, food, and scheduling agents."
    #         }
    #     ]
    # )

    planner_task = get_planner_task(planner_agent)
    weather_task = get_weather_task(weather_agent)

    crew = Crew(
        agents=[planner_agent, weather_agent],
        tasks=[planner_task, weather_task],
    )

    return crew