# bot.py
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import nextcord
from nextcord.ext import commands
import json
from handlers.command_handler import load_commands
import statusChange   # <-- import your new status module

# Load config
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["token"]
GUILD_ID = config["guild_id"]

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.guild_id = GUILD_ID  # So we can use it for slash command registration

# Set up status rotation (call setup function)
statusChange.setup_status_task(bot)

# Load commands from structure/fun
for cmd_module in load_commands("structure/fun"):
    cmd_module.setup(bot)

bot.run(TOKEN)
