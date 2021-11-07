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
    if message.author == client.user and not message.author.bot:
        return
    if message.embeds:
        response = MediaBias.check_bias(message.content)
        if response == "The bot was unable to rate this source":
            await message.add_reaction("❌")
        else:
            await message.reply(response)

load_dotenv('bot.env')
TOKEN=os.getenv('TOKEN')

client.run(TOKEN)