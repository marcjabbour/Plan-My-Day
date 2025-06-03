from crewai import Task

def get_activity_task(activity_agent):
    return Task(
        description=(
            "Using the WebActivityRAGTool, find 2-3 current fun activities in the user's city "
            "based on the weather. Consider any other details relayed in the user's prompt: '{topic}'."
        ),
        agent=activity_agent,
        expected_output="A short list of 2–3 fun, real-time activity ideas for the user.",
        input_variables=["topic"]
    )