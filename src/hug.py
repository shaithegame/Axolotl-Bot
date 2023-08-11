import discord
from src.client import client

def map_to_ping(user: discord.User):
  return user.mention
  

@client.hybrid_command(description='Give selected user(s) hugs')
async def hug(
  ctx,
  user_1: discord.User,
  user_2: discord.User = None,
  user_3: discord.User = None,
  user_4: discord.User = None,
  user_5: discord.User = None
):
  users = [user_1]
  if user_2 or user_3 or user_4 or user_5 != None:
    users.append(user_2)
    users.append(user_3)
    users.append(user_4)
    users.append(user_5)

  user_mentions = map(map_to_ping, users)
  mention_list = ', '.join(user_mentions)
  
  await ctx.send(f'Hugs for {mention_list} from {ctx.author.mention}')