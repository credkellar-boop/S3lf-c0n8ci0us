import os
import time
from openai import OpenAI
import cognitive_core # OUR COMPILED RUST MODULE!
from dotenv import load_dotenv

load_dotenv()

class ThoughtMatrix:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "mock-key")
        self.client = OpenAI(api_key=self.api_key) if self.api_key != "mock-key" else None

    def execute_cognitive_loop(self, user_prompt, framework_data):
        system_instructions = (
            f"You are operating under the S3lf-c0n8ci0us framework: {framework_data['name']}. "
            f"Description: {framework_data['description']}\n"
        )
        for step in framework_data['steps']:
            system_instructions += f"Execute Phase [{step['phase']}]: {step['prompt_injection']}\n"

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_prompt}
            ],
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                text_chunk = chunk.choices[0].delta.content
                start_time = time.perf_counter()
                
                # RUST INTERCEPT: Audit the text chunk for evasive rambling
                passed_audit = cognitive_core.rust_audit_stream(text_chunk)
                
                execution_ms = (time.perf_counter() - start_time) * 1000
                
                if not passed_audit:
                    yield ("\n\n🚨 [RUST CORE OVERRIDE]: AI Evasion detected. Stream killed.", execution_ms)
                    break
                
                yield (text_chunk, execution_ms)
