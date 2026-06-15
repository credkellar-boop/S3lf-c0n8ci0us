import os
from google import genai
from google.genai import types

class GeminiReasoningEngine:
    def __init__(self):
        # The SDK automatically scales to Vertex AI if env vars or flags are set
        self.client = genai.Client(
            vertexai=True,
            project=os.getenv("GOOGLE_CLOUD_PROJECT"),
            location=os.getenv("GOOGLE_CLOUD_LOCATION")
        )
        # Using the advanced 3.1 Pro engine for heavy architectural & security analysis
        self.model_id = "gemini-3.1-pro" 

    def evaluate_system_anomaly(self, telemetry_payload: str) -> str:
        """
        Passes complex system metrics and log anomalies through 
        Gemini 3.1 Pro's extended deep thinking pipeline.
        """
        prompt = f"""
        Review the following telemetry dump captured by the core systems monitor. 
        Perform an adversarial and structural analysis to trace the root cause 
        of the anomalous performance signatures.
        
        [TELEMETRY DATA]:
        {telemetry_payload}
        """

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are an expert autonomous systems architect, kernel engineer, "
                        "and cybersecurity response engine. Provide exhaustive, first-principles "
                        "diagnostic analysis and concrete remediation steps."
                    ),
                    # Activating maximum complex thinking/reasoning configurations
                    thinking_config=types.ThinkingConfig(
                        thinking_level=types.ThinkingLevel.HIGH
                    ),
                    temperature=0.2, # Kept low for deterministic engineering output
                )
            )
            return response.text
            
        except Exception as e:
            return f"[ERROR] Failed to process payload through Gemini Cloud: {str(e)}"
