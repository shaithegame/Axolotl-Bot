from src.client import client

@client.hybrid_command(description='Welcomes the user of the command')
async def welcome(ctx):
  await ctx.send(f'Welcome {ctx.author.mention}! =(^v^)=')
