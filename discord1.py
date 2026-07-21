import importlib.util
import os
from pathlib import Path

import discord
from dotenv import load_dotenv


load_dotenv()

spec = importlib.util.spec_from_file_location(
    "elina",
    Path(__file__).with_name("Elina 2.py")
)
elina = importlib.util.module_from_spec(spec)
spec.loader.exec_module(elina)

TOKEN = os.getenv("DISCORD_TOKEN", "")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
history = []

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_message(message):
    text = message.content.strip()

    if message.author == bot.user or message.channel.id != CHANNEL_ID or not text:
        return

    history.append({
        "speaker": message.author.display_name,
        "context": text
    })

    reply = await elina.get_reply(
        elina.build_conversation(history[-20:])
    )

    if reply:
        reply = str(reply)
        history.append({"speaker": "Elina", "context": reply})
        await message.channel.send(reply)


bot.run(TOKEN)
