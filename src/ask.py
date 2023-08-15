import discord
from src.client import client

@client.hybrid_command
async def ask(ctx):
  await ctx.send('Question time initiated, ask away!')
  message=await client.wait_for('message')

  if 'pronoun' or 'pronounce' in msg.content_lower():
    await ctx.send('test')