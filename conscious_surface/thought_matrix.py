import os
import json
from openai import OpenAI

class ThoughtMatrix:
    def __init__(self):
        # Fallback to local simulation if key isn't present
        self.api_key = os.getenv("OPENAI_API_KEY", "mock-key")
        self.client = OpenAI(api_key=self.api_key) if self.api_key != "mock-key" else None

    def execute_cognitive_loop(self, user_prompt, framework_data):
        # Injecting the structural boundaries directly into the agent's subconscious
        system_instructions = (
            f"You are operating under the S3lf-c0n8ci0us framework: {framework_data['name']}. "
            f"Description: {framework_data['description']}\n"
        )
        for step in framework_data['steps']:
            system_instructions += f"Execute Phase [{step['phase']}]: {step['prompt_injection']}\n"

        if not self.client:
            return f"[Simulation Mode] S3lf-c0n8ci0us intercepted: {user_prompt}\nInjected Framework Context: {framework_data['name']}"

        # Hit the model using the strict structured instructions
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_prompt}
            ],
            stream=True
        )
        return response
