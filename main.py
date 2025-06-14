import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

messages = []

print("💬 Chat with LLaMA (Groq) — type 'exit' to quit.\n")

while True:
    user_input = input("🧑 You: ")

    if user_input.strip().lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("🤖 LLaMA:", reply)

    messages.append({"role": "assistant", "content": reply})
