import discord
from src.client import client

@client.hybrid_command(description='Pings a selected user and gives them a hug')
async def hug(ctx, user: discord.User):
  await ctx.send(f'Hugs for {user.mention} from {ctx.author.mention}! =^w^=')
