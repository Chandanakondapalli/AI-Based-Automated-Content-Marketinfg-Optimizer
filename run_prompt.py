import base64
import os
from google import genai

# To run this code you need to install the following dependencies:
# pip install google-genai

GEMINI_API_KEY = "AIzaSyBD0IMoue8bUXotzPY3z3SzBrcXf5R1Vwo"

def execute_gemini(prompt):
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text


if __name__ == "__main__":

    bunch = [
        "How many p are there in the word apple?",
        "How many p are there in the word apple?",
        "How many p are there in the word apple?"
    ]
    for prompt in bunch:
        execute_gemini(prompt=prompt)


def execute_gemini_for_tweets(prompt):  # INFO: THIS IS FOR TWEET CREATION
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text

