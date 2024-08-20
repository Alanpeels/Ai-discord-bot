import discord
from discord import Intents
import os
from discord import message
from openai import OpenAI
import test  

intents = Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.get_channel("channel_id").send("Bot is now online!  :smirk_cat: ")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ("!help"):
        await message.channel.send('Use ! "Prompt here" to test out the bot')

   
    elif message.content.startswith("!"):
        user_message = message.content[1:]
        response = await client.loop.run_in_executor(None, test.generate_response, user_message)

        if len(response) > 2000:
            chunks = [response[i:i + 2000] for i in range(0, len(response), 2000)]
            for chunk in chunks:
                await message.channel.send(chunk)
        else:
            await message.channel.send(response)


client.run(os.environ['discord'])
