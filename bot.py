import discord
import os
from dotenv import load_dotenv
import MediaBias

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.embeds:
        response = MediaBias.check_bias(message.content)
        await message.reply(response)

load_dotenv('bot.env')
TOKEN=os.getenv('TOKEN')

client.run(TOKEN)