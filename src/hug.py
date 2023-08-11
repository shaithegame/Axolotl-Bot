import discord
from src.client import client

def map_to_ping(user: discord.User):
  return user.mention
  

@client.hybrid_command(description='MULTI-PERSON HUG TEST')
async def hug(
  ctx,
  user_1: discord.User,
  user_2: discord.User = None
):
  users = [user_1]
  if user_2 is not None:
    users.append(user_2)

  user_mentions = map(map_to_ping, users)
  mention_list = ', '.join(user_mentions)
  await ctx.send(f'Hugs for {mention_list} from {ctx.author.mention}')