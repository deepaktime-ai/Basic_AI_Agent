import ollama
import json
from tools import TOOLS, calculator, search_tool
from memory import Memory
from config import MODEL


class Agent:
    def __init__(self):
        self.memory = Memory()

    def think(self, user_input):
        history = self.memory.get()

        prompt = f"""
        You are an AI agent.

        Available tools:
        {list(TOOLS.keys())}


        Respond ONLY in JSON:
        {{
            "action": "calculator | search_tool | none",
            "input": "string"
        }}

        History:
        {history}

        User: {user_input}
        """

        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    def act(self, decision):
        try:
            decision_json = json.loads(decision)

            action = decision_json.get("action")
            input_data = decision_json.get("input")

            if action in TOOLS:
                return TOOLS[action](input_data)
            return "No tool used"

            

        except Exception as e:
            return f"Parsing Error: {str(e)}"

    def respond(self, user_input, tool_result):
        history = self.memory.get()

        prompt = f"""
        You are a helpful assistant.

        History:
        {history}

        User: {user_input}
        Tool result: {tool_result}

        Give final answer.
        """

        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    def run(self, user_input):
        self.memory.add("user", user_input)

        decision = self.think(user_input)
        print("\n🧠 Decision:", decision)

        tool_result = self.act(decision)
        print("🛠 Tool Output:", tool_result)

        final_answer = self.respond(user_input, tool_result)

        self.memory.add("assistant", final_answer)

        return final_answer