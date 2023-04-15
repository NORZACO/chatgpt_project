import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
roles = [{"role": "user", "content": "Hello"}]
my_models = "gpt-3.5-turbo"

completion = openai.ChatCompletion.create(
    model=my_models,
    messages=roles
)

print(completion.choices[0].message)
