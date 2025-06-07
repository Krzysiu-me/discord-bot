# statusChange.py
# Copyright (c) 2025 Krzysiu
# Licensed under the MIT License. See LICENSE file for details.

import itertools
import nextcord
from nextcord.ext import tasks

# List of rotating statuses
statuses = itertools.cycle([
    "with slash commands!",
    "Pong! Try /ping",
    "Discord Bot by Krzysiu",
    "Add me to your server!",
    "Use /ping for a test!",
])

def setup_status_task(bot):
    @tasks.loop(minutes=1)
    async def change_status():
        status = next(statuses)
        await bot.change_presence(activity=nextcord.Game(status))

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")
        change_status.start()
