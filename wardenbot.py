import discord
from discord.ext import commands
import random
import json

json_path = 'E:/Projects/wardenbot/config.json'

with open(json_path, 'r') as cfg:
    data = json.load(cfg)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if f'<@{bot.user.id}>' in message.content and 'report' in message.content:
            await message.channel.send("Nominal!")
    await bot.process_commands(message)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    
    rolling_message = f'Rolling {rolls}d{limit}...'
    await ctx.send(rolling_message)
    
    individual_rolls = [random.randint(1, limit) for r in range(rolls)]
    dicetotal = sum(individual_rolls)

    result = f'{", ".join(map(str, individual_rolls))} = {dicetotal}'
    await ctx.send(result)


bot.run(data['token'])