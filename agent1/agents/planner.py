class Planner:
    def plan(self, user_input: str):
        return [
            {"task_id": "t1", "worker_type": "shelter_worker", "params": {"disaster": user_input}},
            {"task_id": "t2", "worker_type": "weather_worker", "params": {"disaster": user_input}},
        ]
