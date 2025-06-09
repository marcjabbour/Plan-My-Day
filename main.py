import streamlit as st
from openai import OpenAI
from crew.create_crew import create_planner_crew
from crew.create_crew import create_food_crew
from crewai import Crew
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import re
import json
import os
import ast

from dotenv import load_dotenv
load_dotenv()

# === INITIALIZATION ===
st.set_page_config(page_title="AI Day Planner", page_icon="🧠")

if "phase" not in st.session_state:
    st.session_state.phase = "start"
    st.session_state.activities = []
    st.session_state.selected_activities = []
    st.session_state.food_suggestions = []
    st.session_state.intent = None

st.title("🧠 Plan My Day with AI")
user_input = st.chat_input("What do you want to do today?")

# === STEP 1: INTENT DETECTION ===
def detect_intent(prompt: str) -> str:
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are a smart assistant that decides what the user wants:
- If they are asking to plan something, reply: plan_day
- If they want more activity suggestions: more_activities
- If they want food suggestions after selecting activities: suggest_food
- If they want personalized food options: refine_food
- Else: unknown"""),
        ("human", "{input}")
    ])

    chain = LLMChain(llm=llm, prompt=prompt_template)
    result = chain.run(input=prompt)

    return result.strip()


# === HANDLE NEW USER MESSAGE ===
if user_input:
    intent = detect_intent(user_input)
    print(f"DETECTED INTENT: {intent}")
    st.session_state.intent = intent

    if intent == "plan_day":
        with st.spinner("Planning your day..."):
            activity_planning_crew = create_planner_crew()
            result = activity_planning_crew.kickoff(inputs={"topic": user_input})

            full_text = json.loads(result.raw)

            st.session_state.structured_activities = full_text["extra_info"]
            st.session_state.text_intro = full_text["intro"]
            st.session_state.activities = full_text["activities"]
            st.session_state.text_outro = full_text["outro"]
            st.session_state.phase = "show_activities"

    elif intent == "more_activities":
        st.session_state.phase = "start"  # Just rerun crew1

    elif intent == "suggest_food":
        st.session_state.phase = "food"

    elif intent == "refine_food":
        st.session_state.phase = "refine_food"

# === SHOW ACTIVITY CHOICES ===
if st.session_state.phase == "show_activities":
    print(f"ACTIVITIES: {st.session_state.activities}")
    st.markdown(st.session_state.text_intro)

    for i, act in enumerate(st.session_state.activities):
        st.checkbox(f"**{act['name']}**: {act['description']}", key=f"activity_{i}")

    st.markdown(st.session_state.text_outro)

    if st.button("Continue with selected activities"):
        st.session_state.selected_activities = [
            st.session_state.activities[i]
            for i in range(len(st.session_state.activities))
            if st.session_state.get(f"activity_{i}")
        ]
        st.session_state.phase = "food"

# === FOOD SUGGESTIONS ===
if st.session_state.phase == "food":
    st.subheader("🍽️ Food Suggestions Based on Your Selected Activities:")
    print(f"STRUCTURED ACTIVITIES: {st.session_state.structured_activities}")
    print(f"SELECTED ACTIVITIES: {st.session_state.selected_activities}")
    with st.spinner("Finding restaurants nearby..."):
        food_crew = create_food_crew()
        result = food_crew.kickoff(inputs={"selected_activities": st.session_state.selected_activities, "preference": ""})
        raw_food = result.raw
        try:
            st.session_state.food_suggestions = json.loads(raw_food)
        except Exception:
            try:
                st.session_state.food_suggestions = ast.literal_eval(raw_food)
            except Exception:
                st.session_state.food_suggestions = []
                st.warning("Could not parse food suggestions.")
        print(f"FOOD SUGGESTIONS: {raw_food}")

    for suggestion in st.session_state.food_suggestions:
        st.markdown(f"**Near {suggestion['location']}**")
        for restaurant in suggestion['restaurants']:
            st.write(f"- 🍽️ **{restaurant['name']}**")
            st.write(f"- - 📍 {restaurant['address']}")
            st.write(f"- - ⭐ {restaurant['rating']}  👥 {restaurant['total_ratings']} ratings")

    st.text_input("Want something specific? Enter a food preference", key="refine_input")
    if st.session_state.refine_input:
        st.session_state.phase = "refine_food"

# === REFINED FOOD ===
if st.session_state.phase == "refine_food":
    preference = st.session_state.get("refine_input", "")
    st.write(f"Finding more specific places for the following cuisine(s): {preference}")
    with st.spinner("Refining suggestions..."):
        result = food_crew.kickoff(inputs={"selected_activities": st.session_state.selected_activities, "preference": preference})
        print(f"RESULT REFINED: {result.raw}")
        raw_food_refined = result.raw
        try:
            st.session_state.food_suggestions = json.loads(raw_food_refined)
        except Exception:
            try:
                st.session_state.food_suggestions = ast.literal_eval(raw_food_refined)
            except Exception:
                st.session_state.food_suggestions = []
                st.warning("Could not parse food suggestions.")
    print(f"FOOD SUGGESTIONS REFINED: {st.session_state.food_suggestions}")
    for suggestion in st.session_state.food_suggestions:
        st.markdown(f"**Near {suggestion['location']}**")
        for restaurant in suggestion['restaurants']:
            st.write(f"- 🍽️ **{restaurant['name']}**")
            st.write(f"- - 📍 {restaurant['address']}")
            st.write(f"- - ⭐ {restaurant['rating']}  👥 {restaurant['total_ratings']} ratings")
