# 🗓️ Plan My Day — Agentic Day Planner with Real-World Integrations

**Plan My Day** is a smart, lightweight AI assistant that helps users plan daily outings based on their preferences, weather conditions, and location. It uses **Crew AI** to orchestrate multiple intelligent agents and **MCP-style tools** to interact with real-world services like weather APIs, Tavily, and calendars.

---

## 🚀 Features

- 🤖 Multi-agent collaboration using Crew AI
- 🌤️ Real-time weather-aware planning
- 🍽️ Restaurant suggestions (non-alcoholic, outdoor-friendly)
- 📅 Full day itinerary generation
- 🌍 MCP-style integrations with:
  - OpenWeather API
  - Tavily API
  - Google Maps (optional)
  - Calendar/Reservation APIs (optional)

---

## 📁 Project Structure

```
plan_my_day_app/
├── main.py                   # Entry point
├── crew/                     # Crew AI agents
│   ├── planner_agent.py
│   ├── weather_agent.py
│   ├── activity_agent.py
│   └── schedule_agent.py
├── tools/                    # Real-world MCP-style tools
│   ├── weather_tool.py
│   ├── food_tool.py
│   └── ...
├── prompts/                  # Optional custom prompts
├── .env                      # API keys and config
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/your-username/plan-my-day.git
cd plan-my-day
```

### 2. Install Dependencies

Ensure Python11 is installed since crewAI only supports Python 3.10 through 3.12

Tip: 
Check which Python3s are in your path
```
which -a python3
```

Then ensure Python11 is specified in your ./zshrc
```
nano ~/.zshrc  
```

Reload terminal with:
```
source ~/.zshrc  
```

Check Python version with
```
which python3
```

Troubleshoot: May have to brew unlink / brew link also
```
brew unlink python@3.13
brew link --overwrite --force python@3.11
```


Optionally set up a virtual environment since macOS (via Homebrew) now installs Python in a PEP 668 compliant way, which prevents pip from modifying the system Python environment directly.

```
python3 -m venv .venv
source .venv/bin/activate
source ~/.zshrc  
```


Now install requirements:

```
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the root directory with the following:

```env
OPENWEATHER_API_KEY=your_openweather_key
TAVILY=your_tavily_key
```

> 🔐 You can get these API keys from:
> - [OpenWeather](https://openweathermap.org/api)
> - [Yelp Fusion](https://www.yelp.com/developers/documentation/v3)

### 4. Run the App (Backend)

```
python main.py
```

---

### 5. 🧪 Running Tests

To run all tests (from the project root):

```
pytest tools/tests/
```

You can also run a specific test file, for example:

```
pytest tools/tests/test_weather_tool.py
```

---

### 6. 🚀 Running the Streamlit Chatbot UI

To launch the interactive chatbot UI, run:

```
streamlit run main.py
```

This will open a browser window where you can chat with the planner agent in real time.

## 💡 Example Prompt

```
I want to go out with friends on Saturday. We don't plan on drinking, and if the weather is good we'd like to be outside. Can you come up with a schedule for us?
```

---

## 🧠 Tech Stack

- [Crew AI](https://github.com/joaomdmoura/crewAI)
- [LangChain](https://www.langchain.com/)
- OpenAI (or other LLMs)
- MCP-style integrations (custom tools calling external APIs)
- Python + Dotenv + Requests

---

## ✅ To-Do / Extensions

- [ ] Add calendar integration (Google Calendar API)
- [ ] Add Uber/Lyft ride scheduling
- [ ✅ ] Add GUI using Streamlit or React
- [ ] Store itineraries in cloud (e.g. Firebase, Supabase)

---

## 📄 License

MIT License — use freely, modify, and share.

---

## 🙋‍♂️ Questions?

Open an issue or reach out at [marc.jabbour@me.com](mailto:marc.jabbour@me.com).
