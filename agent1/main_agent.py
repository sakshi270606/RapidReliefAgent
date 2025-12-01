from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.core.observability import log

class MainAgent:
    def __init__(self):
        self.planner = Planner()
        self.evaluator = Evaluator()

    def handle_message(self, user_input: str):
        log(f"Received input: {user_input}")

        tasks = self.planner.plan(user_input)
        outputs = []

        for task in tasks:
            worker = Worker(task["worker_type"])
            result = worker.run_task(task)
            outputs.append(result)

        return self.evaluator.evaluate(outputs)

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
