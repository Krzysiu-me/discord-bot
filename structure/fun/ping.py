# /structure/fun/ping.py
import nextcord
from nextcord.ext import commands

def setup(bot):
    @bot.slash_command(description="Pong!", guild_ids=[bot.guild_id])
    async def ping(interaction: nextcord.Interaction):
        await interaction.response.send_message("Pong!")
