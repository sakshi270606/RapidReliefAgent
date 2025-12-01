class Worker:
    def __init__(self, worker_type: str):
        self.worker_type = worker_type

    def run_task(self, task):
        disaster = task["params"].get("disaster", "").lower()

        if self.worker_type == "shelter_worker":
            return {
                "task_id": task["task_id"],
                "content": self.shelter_response(disaster),
                "confidence": 0.95
            }

        if self.worker_type == "weather_worker":
            return {
                "task_id": task["task_id"],
                "content": self.weather_response(disaster),
                "confidence": 0.90
            }

        return {"task_id": task["task_id"], "content": "Unknown worker", "confidence": 0.1}

    def shelter_response(self, text):
        if "flood" in text:
            return """⚠️ FLOOD ALERT
- Move to higher ground immediately.
- Avoid rivers & low-lying areas.
- Turn off electricity.
- Carry essentials.
- Do NOT walk/drive through floodwaters."""

        if "earthquake" in text:
            return """⚠️ EARTHQUAKE SAFETY
- Drop, Cover, Hold.
- Stay away from glass.
- Evacuate after shaking stops.
- Avoid damaged structures."""

        if "fire" in text:
            return """🔥 FIRE EMERGENCY
- Stay low under smoke.
- Use wet cloth on mouth.
- Do NOT use lift.
- Evacuate immediately."""

        return "No shelter guidance available."

    def weather_response(self, text):
        if "flood" in text:
            return """🌧 Heavy rainfall expected.
💧 Water levels rising.
⚠️ Stay away from water bodies."""

        if "earthquake" in text:
            return "🌤 No weather data related to earthquakes."

        if "fire" in text:
            return "🌬 Wind may spread fire quickly — stay alert."

        return "No weather data."
