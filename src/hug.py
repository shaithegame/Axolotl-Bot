import discord
from src.client import client

@client.hybrid_command(description='Pings a selected user and gives them a hug')
async def hug(ctx, user1: discord.User, required=True, Option(str, user2: discord.User, required=False)):
  await ctx.send(f'Hugs for {user1.mention} and {user2.mention} from {ctx.author.mention}! =(^w^)=')
