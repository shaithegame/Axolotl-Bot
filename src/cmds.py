import discord
from src.client import client

@client.hybrid_command(description='Provides a list of all available commands')
async def cmds(ctx):
  embed = discord.Embed(
    title='AxolotlBot Commands!',
    description=
'''Here is a list of all available commands as of the most recent update and their uses:
- **axo!info or /info**: Provides basic information about AxolotlBot, including the current version.
- **axo!cmds** or **/cmds**: Congrats, you successfully used this one! This is where all relevant command info will be stored.
- **axo!welcome** or **/welcome**: Welcomes the user of the command.
'''
  )
  await ctx.send(embed=embed)
