import json

class TroveAgent:
    def __init__(self, name, system_prompt, model, max_loops=1):
        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.max_loops = max_loops
        self.history = []

    def run(self, query):
        """Runs the AI agent on a given query."""
        message = {"role": "user", "content": query}
        self.history.append(message)
        
        response = self.model.generate_response(self.history)
        self.history.append({"role": "assistant", "content": response})
        
        return response

    def save_state(self, file_path="agent_state.json"):
        """Saves chat history."""
        with open(file_path, "w") as file:
            json.dump(self.history, file)

    def load_state(self, file_path="agent_state.json"):
        """Loads previous chat history."""
        with open(file_path, "r") as file:
            self.history = json.load(file)
