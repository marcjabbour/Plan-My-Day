from crewai import Task

def get_planner_task(planner_agent):
    return Task(
        description="Given the user's request: '{topic}', determine the day and location, and delegate to the correct agents.",
        agent=planner_agent,
        expected_output="Parsed intent with a natural language date and city.",
        input_variables=["topic"]
    ) 