import openai
import os

class OpenAIModel:
    """Wrapper for OpenAI API"""
    def __init__(self, api_key=None, model_name="gpt-4o-mini", temperature=0.1):
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature

    def generate_response(self, messages):
        """Generates a response from OpenAI API (Updated for v1.0.0+)"""
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature
        )
        return response.choices[0].message.content
