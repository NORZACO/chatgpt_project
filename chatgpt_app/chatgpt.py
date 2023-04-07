# chatgpt.py

# import openai
# # from django.conf import settings
# import os

# openai.api_key = os.getenv('OPENAI_API_KEY')

# def generate_text(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     return response.choices[0].text.strip()


# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_text(prompt):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=60,
#         top_p=1.0,
#         frequency_penalty=0.5,
#         presence_penalty=0.0,
#         stop=["You:"]
#     )

#     return response.choices[0].text.strip()

# # Example usage
# prompt = "You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:"
# generated_text = generate_text(prompt)
# print(generated_text)


import os
from django.shortcuts import render
from django.http import JsonResponse
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )

    return response.choices[0].text.strip()