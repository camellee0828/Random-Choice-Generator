import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!choose'):
        options = message.content.split(',').strip()[1:]
        final = random.choice(options)
        await message.channel.send(f'The final choice is ... {final}!!!')

client.run('MTA4Njk0NDAxNTA1Nzk0NDU4Ng.GLBUA3.jC6NUcuRU2Ju1AZ29f5xTyZtKNnlRTc9crQrIU')