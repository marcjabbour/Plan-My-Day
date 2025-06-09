from crewai import Task

def get_activity_task(activity_agent):
    return Task(
        description=(
            "Using the WebActivityRAGTool, find 3-5 current fun activities in the user's city "
            "based on the weather. Be specific and suggest exact locations.Consider any other details relayed in the user's prompt: '{topic}'."
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