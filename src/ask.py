import discord
from src.client import client


@client.hybrid_command(description='Ask axolotl bot questions')
async def ask(ctx, *, msg):
  answer=''
  msg=''
  embed=discord.Embed(
    title=msg,
    description=answer
  )
  if 'pronoun' or 'pronounce' in msg.content_lower():
    answer='My pronouns are he/they! =*w*='

  await ctx.send((f'{ctx.author.mention}'), embed=embed)