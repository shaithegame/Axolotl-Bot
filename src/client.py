import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix="axo!", intents=intents)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for axo!info or /info"))
  try:
    synced = await client.tree.sync()
    print(f'Synced {len(synced)} commands')
  except Exception as e:
    print(e)
    print('Worked')
