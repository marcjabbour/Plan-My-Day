import streamlit as st
from crew.create_crew import create_planner_crew
from dotenv import load_dotenv
load_dotenv()

st.title("🗓️ Plan My Day Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

crew = create_planner_crew()

def clear_input():
    st.session_state['user_input'] = ""

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input(
        "What would you like to plan today?",
        value=st.session_state['user_input'],
        key='user_input',
    )
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        plan = crew.kickoff(inputs={"topic": user_input})
    st.session_state['messages'].append({"role": "assistant", "content": plan})

for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Planner:** {msg['content']}")