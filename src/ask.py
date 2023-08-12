import discord
from src.client import client

@client.hybrid_command(description='Ask axolotl bot questions')
async def ask(ctx, *, message: str):
  answer=''
  message=''
  embed=discord.Embed(
    title= message,
    description=answer
  )
  if 'pronoun' or 'pronounce' in message.lower():
    answer='My pronouns are he/they! =*w*='

  await ctx.send({ctx.author.mention}, embed)