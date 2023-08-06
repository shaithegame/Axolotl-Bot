import discord
from src.client import client

@client.hybrid_command(description='Provides link to suggestion box')
async def suggest(ctx):
  embed = discord.Embed(
      title='AxolotlBot Suggestion Box!',
      description='Thank you for considering helping out AxolotlBot! If you have additions to suggest, you can submit those additions here! You can also report bugs, give general feedback, and say whatever else comes to your mind regarding the bot!\n\nThe link below will direct you to a Google form. The only information collected will be what you provide in the form and the timestamps of any submissions.\n\nQuality user additions will be added to the bot!\n\n[Go to form!](<https://forms.gle/f1A8bbD8qSkjNyDj7>)')
  embed.set_image(url='https://wallpapercave.com/wp/wp8806603.jpg')
  await ctx.send(embed=embed)
