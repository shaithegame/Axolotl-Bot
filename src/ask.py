import discord
from src.client import client

@client.hybrid_command
async def ask(ctx, *, msg: str):
  await ctx.send('Question time ready!')
  
  message=await client.wait_for('message')
  
  if 'pronoun' or 'pronounce' in msg.content_lower():
    await message.send('test')