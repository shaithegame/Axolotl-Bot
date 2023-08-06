import discord
from src.client import client

@client.hybrid_command(description='Shows information on AxolotlBot, including current version info')
async def info(ctx):
  embed = discord.Embed(
    title='Welcome to AxolotlBot (v1.0)!',
    description=
'''**Thank you for using AxolotlBot**!
This is a little bot created by a single person with an (debatably) unhealthy obsession with axolotls and other various small creatures. I hope this bot is able to make you smile! =(^v^)=\n\n**Key features:**
- Over a dozen unique facts about axolotls/n-  Quality axolotl photos available at your fingertips (or... keyboard...tips...?)
- Hug and kiss a user in true axolotl fashion\n- Axolotl jokes and compliments
- Ask AxoBot questions/n- And, eventually, even more!

**Get started!**
Type axo!cmds or /cmds to view everything currently available!

**Contact the dev!**
Github: <https://github.com/shaithegame/Axolotl-Bot>
Discord: binchildish\nThe Axolotl Bot suggestion box (axo!suggest)

All the best!
AxoBot'''
  )
  await ctx.send((f'{ctx.author.mention}'), embed=embed)
