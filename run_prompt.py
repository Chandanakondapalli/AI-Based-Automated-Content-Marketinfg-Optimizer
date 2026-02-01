import base64
import os
import google.generativeai as genai

# To run this code you need to install the following dependencies:
# pip install google-generativeai

GEMINI_API_KEY = "AIzaSyBD0IMoue8bUXotzPY3z3SzBrcXf5R1Vwo"

def execute_gemini(prompt):
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content(prompt)
    
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
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content(prompt)
    
    return response.text

