from src.client import client

@client.hybrid_command(description='Make the bot speak via TTS')
async def speak(ctx):
  await ctx.send('bark', tts=True)
