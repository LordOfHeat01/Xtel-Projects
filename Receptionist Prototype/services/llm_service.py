from openai import OpenAI

from config import (
    HF_API_KEY, 
    HF_BASE_URL,
    LLM_MODEL,
    MAX_TOKENS,
    TEMPERATURE,)



class LLMService:
    def __init__(self):
        """Initialize the Hugging Face Clinet"""

        self.client = OpenAI(
            base_url=HF_BASE_URL,
            api_key=HF_API_KEY
        )

    def generate_response(self, messages):
        """
        Send the conversation to the LLM
        and return Sarah's response.
        """
        print("\nGenerating Sarah's response...")
        try:
            response = self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            print("Response generated successfully.")

            return response.choices[0].message.content.strip()
        

        except Exception as error:
            print(f"LLM Error: {error}")
            return (
                "I'm sorry, but I'm unable to respond at the moment."
                "Please try again."
            )
        

#this file's only jobs is conversation -> LLM -> Reply
#         