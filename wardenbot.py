import discord
from discord.ext import commands
import random
from pathlib import Path
import json
import requests


script_path = Path(__file__).resolve()

json_path = script_path.parent / 'config.json'

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

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if f'<@{bot.user.id}>' in message.content and 'report' in message.content:
        await message.channel.send("Nominal!")
    await bot.process_commands(message)

#Test function
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

def check_war_state():
    url = 'https://war-service-live.foxholeservices.com/api/worldconquest/war'
    response = requests.get(url)

    if response.status_code == 200:
        war_data = response.json()
        war_state = war_data['warReport']['warState']
        print(f'Current war state: {war_state}')
    else:
        print(f'Error: {response.status_code}')

if __name__ == "__main__":
    check_war_state()

bot.run(data['token'])