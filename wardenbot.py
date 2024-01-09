import discord
from discord.ext import commands
import random
import json

with open('config.json', 'r') as cfg:
    data = json.load(cfg)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if f'<@{bot.user.id}>' in message.content and 'report' in message.content:
            await message.channel.send("Nominal!")
    


"""@bot.event
async def on_message(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content and 'report' in message.content:
        print("bot mentioned and 'report' found in the message!")
        await message.channel.send("Nominal!")
    else:
        print("bot mentioned, but 'report' not found or not in the correct format")"""

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


bot.run(data['token'])