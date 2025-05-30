from crew.create_crew import create_planner_crew
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    # user_prompt = "I want to go out with friends on Saturday. We don't plan on drinking, and if the weather is good we'd like to be outside."
    user_prompt = "I'm wondering if I should go outside on Saturday in New York City"

    crew = create_planner_crew()
    plan = crew.kickoff(inputs={"topic": user_prompt})

    # print("\n--- Your Day Plan ---\n")
    print("\n--- Advice Given the Weather ---\n")
    print(plan)