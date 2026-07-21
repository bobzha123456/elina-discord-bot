import asyncio
import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

with open("prompt1.txt", "r", encoding="utf-8") as file:
    prompt = file.read()



API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = prompt + """

Return JSON only using exactly this format:

{
  "action": "reply",
  "messages": ["your reply"]
}

Do not include markdown.
Do not include ```json.
"""

async def get_reply(conversation: str) -> str:
    response = await client.aio.models.generate_content(
        model=MODEL,
        contents=conversation,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string"
                    },
                    "messages": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["action", "messages"]
            }
        )
    )

    raw_text = response.text or "{}"

    data = json.loads(raw_text)

    messages = data.get("messages", [])

    if not messages:
        return ""

    return messages[0].strip()

##底层逻辑结束， 可以开始自由更改
async def main():
    history = []
    print("Elina on, type exit to end")
    while True:
        try:
            user_message = input("Fugue: ")

            if (user_message.lower()== ("exit")):
                break

            if not user_message.strip():
                print("message cannot be empty")
                continue

            history.append({"speaker": "Fugue", "context": user_message })
            recent_history = history[-20:]
            conversation = build_conversation(recent_history)

            reply = await get_reply(conversation)

            history.append({"speaker": "Elina", "context": reply })

            print("Elina:", reply)

        except Exception as error:
            print(f"ERROR: {error}")

def build_conversation(history):
    hi = []
    for i in history:
        hi.append(f'{i["speaker"]}: {i["context"]}')
    
    return "\n".join(hi)


        


if __name__ == "__main__":
    asyncio.run(main())
