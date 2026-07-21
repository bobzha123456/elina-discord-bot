# Elina Discord Bot

Elina is a small Discord character bot built with Python, `discord.py`, and Google's Gemini API. It reads recent messages from one Discord channel, sends the latest conversation to the Elina model, and posts the generated reply back to Discord.

## Project files

- `discord1.py` — connects Elina to Discord.
- `Elina 2.py` — generates Elina's replies with Gemini.
- `prompt1.txt` — defines Elina's character and response style.
- `.env.example` — shows the required private configuration.
- `requirements.txt` — lists the Python packages.

## 1. Create a virtual environment

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create the private `.env` file

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then fill in your own values:

```env
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.1-flash-lite
```

Enable **Message Content Intent** for the bot in the Discord Developer Portal. To obtain the channel ID, enable Discord Developer Mode and copy the ID of the channel where Elina should reply.

## 4. Run Elina

```bash
python discord1.py
```

## Security

Never write a real Discord token or Gemini API key directly into a Python file. Keep them only in `.env`. This repository's `.gitignore` prevents `.env` and `.venv` from being committed.

Before every GitHub upload, check the staged files:

```bash
git status
git diff --cached
```

You can also search tracked files for common secret names:

```bash
git grep -n -E "DISCORD_TOKEN|GEMINI_API_KEY|API_KEY"
```

Seeing environment-variable names is normal. Seeing an actual secret value is not. If a real token or API key was ever committed, revoke and regenerate it immediately; deleting it from the newest file is not enough because Git history may still contain it.
