import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
history = []

print("Claude Chat — type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "quit":
        break

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=history,
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})

    print(f"\nClaude: {reply}\n")
