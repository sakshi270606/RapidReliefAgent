class Evaluator:
    def evaluate(self, worker_outputs):
        response_text = "\n\n".join([w["content"] for w in worker_outputs])
        return {"response": response_text, "confidence": 0.95}
