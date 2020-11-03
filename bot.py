import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} Raring to go!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!rules':
        response = 'rules text coming soon'
        await message.channel.send(response)

client.run(TOKEN)
