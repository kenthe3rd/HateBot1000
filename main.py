import discord
import os
from dotenv import load_dotenv

load_dotenv('.env')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send("boom goes the dynamite")

client.run(os.getenv('TOKEN'))