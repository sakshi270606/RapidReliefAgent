RapidReliefAgent
RapidRelief Agent — Multi-Agent AI for Real-Time Disaster Alerts, Safety Guidance & Relief Info.
Overview :
RapidReliefAgent is a multi-agent AI system designed to provide instant disaster alerts, safety instructions, and environment-based risk analysis. It uses three coordinated agents:
Planner Agent — understands the user input and creates tasks
Worker Agents — provide disaster-specific safety guidance
Evaluator Agent — combines and finalizes the response
Key Features
Real-time disaster guidance
Multi-agent architecture
Disaster-specific safety instructions
Modular Python code
Easy to extend
System Architecture
flowchart TD
User([User Input]) --> |Sends message| Planner[Planner Agent]
Planner --> |Creates tasks| ShelterW[Shelter Worker]
Planner --> |Creates tasks| WeatherW[Weather Worker]
ShelterW --> |Shelter safety instructions| Evaluator[Evaluator Agent]
WeatherW --> |Weather warnings| Evaluator
Evaluator --> |Final response| User

Project Structure
agent1/
│── agents/
│   ├── planner.py
│   ├── worker.py
│   ├── evaluator.py
│── core/
│   ├── a2a_protocol.py
│   ├── context_engineering.py
│   ├── observability.py
│── memory/
│   ├── session_memory.py
│── tools/
│   ├── tools.py
│── main_agent.py
│── run_demo.py

Example Usage
from agent1.main_agent import run_agent
print(run_agent("There is a flood in my area"))

Disaster Responses
Flood
Move to higher ground
Avoid rivers and low areas
Turn off electricity
Carry emergency essentials
Earthquake
Drop, Cover, Hold
Avoid windows
Evacuate after shaking stops

Fire
Crawl under smoke
Cover mouth with wet cloth
Do not use lifts
Evacuate immediately

Tech Stack: Python

Multi-Agent Architecture:
A2A Protocol
Custom Worker Agents

How to Run:
Download or clone repository
Open in Google Colab or local environment
Run:

from agent1.main_agent import run_agent
run_agent("Your message here")

Future Improvements:
Add more worker agents
Add live weather API
Add evacuation routes
Add multilingual support
