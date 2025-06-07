## Python Discord Bot

A modular, beginner-friendly Discord bot written in Python, using Nextcord for easy slash commands and rich bot features.
Features

    Slash Commands: Modern, user-friendly /commands (e.g. /ping)

    Modular Command System: Organize your commands by category in folders (easy to extend)

    Customizable Status: Rotates the bot’s status message every minute

    Easy Setup: Simple config, clean structure

Getting Started

1. Clone the repository

```
git clone https://github.com/YOUR-USERNAME/YOUR-BOT-REPO.git
cd YOUR-BOT-REPO
```

2. Set up a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements

```
pip install nextcord
```

4. Configure your bot

```
    Copy your bot token and server (guild) ID into config.json:

{
    "token": "YOUR_BOT_TOKEN",
    "guild_id": 123456789012345678
}
```


5. Run the bot

```
python bot.py
```

## Adding Commands

Just drop a new .py file in the appropriate category folder inside /structure/.
Each command file should have a setup(bot) function for registering commands.

Questions or improvements? Open an issue or a pull request!
