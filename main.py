import discord
from discord import Intents, app_commands
import asyncio
from discord.audit_logs import _transform_default_reaction
from discord.ext.commands import BucketType, Cog, BadArgument, NSFWChannelRequired, command, cooldown
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

intents = discord.Intents.all()
client = commands.Bot(command_prefix="axo!", intents=intents)

colors=[
    0xF44336, 0xE91E63, 0x9C27B0, 0x673AB7, 0x3F51B5, 0x2196F3, 0x03A9F4,
    0x00BCD4, 0x009688, 0x4CAF50, 0x8BC34A, 0xCDDC39, 0xFFEB3B, 0xFFC107,
    0xFF9800, 0xFF5722, 0x795548]
gen_img=['https://upload.wikimedia.org/wikipedia/commons/7/75/Ambystoma_mexicanum_1zz.jpg', 'https://www.premierpet.com.au/productimages/GXA800-15.jpg']

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="axo!info or /info"))
  try:
    synced = await client.tree.sync()
    print(f'Synced {len(synced)} commands')
  except Exception as e:
    print(e)
    print('Worked')

@client.hybrid_command(description='Shows information on AxolotlBot, including current version info')
async def info(ctx):
  embed = discord.Embed(
    title='Welcome to AxolotlBot (v1.0)!',
    description='**Thank you for using AxolotlBot**!\nThis is a little bot created by a single person with an (debatably) unhealthy obsession with axolotls and other various small creatures. I hope this bot is able to make you smile! =(^v^)=\n\n**Key features:**\n- Over a dozen unique facts about axolotls/n-  Quality axolotl photos available at your fingertips (or... keyboard...tips...?)\n- Hug and kiss a user in true axolotl fashion\n- Axolotl jokes and compliments\n- Ask AxoBot questions/n- And, eventually, even more!\n\n**Get started!**\n Type axo!cmds or /cmds to view everything currently available!/n/n**Contact the dev!**/nGithub: [(<https://github.com/shaithegame/Axolotl-Bot>)]\nDiscord: binchildish\nThe Axolotl Bot suggestion box (axo!suggest)\n\nAll the best!\nAxoBot'
  )
  await ctx.send((f'{ctx.author.mention}'), embed=embed)
  

@client.hybrid_command(description='Provides a list of all available commands')
async def cmds(ctx):
  embed = discord.Embed(
      title='AxolotlBot Commands!',
      description='Here is a list of all available commands as of the most recent update and their uses:\n\n **axo!info or /info**: Provides basic information about AxolotlBot, including the current version.\n**axo!cmds** or **/cmds**: Congrats, you successfully used this one! This is where all relevant command info will be stored.\n**axo!welcome** or **/welcome**: Welcomes the user of the command.\n'
  )
  await ctx.send(embed=embed)

@client.hybrid_command(description='Welcomes the user of the command')
async def welcome(ctx):
  await ctx.send(f'Welcome {ctx.author.mention}! =(^v^)=')

@client.hybrid_command(description='Generates a random axolotl fact')
async def fact(ctx):
  facts = [
      discord.Embed(
          title='Axolotl Fact 1',
          description='The scientific name for axolotls is *Ambystoma                    mexicanum*!\n\n[Source 🔗](<https://www.nationalgeographic.com/animals/amphibians/facts/axolotl>)',
          color=random.choice(colors)),
   
    discord.Embed(
          title='Axolotl Fact 2',
          description='Axolotls can survive in captivity for 10 to 15 years, and in the wild for five to six years.\n\n[Source 🔗](<https://www.nationalgeographic.com/animals/amphibians/facts/axolotl>)',
          color=random.choice(colors)),
    
    discord.Embed(  
      title='Axolotl Fact 3',
          description='The word "axolotl", alongside having mythological origins, translates from the Nahuatl language of the Aztecs as "water dog."\n\n[Source 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
          color=random.choice(colors)),
    
    discord.Embed(
          title='Axolotl Fact 4',
          description='The common name for axolotls is said to originate from a legend about the Aztec god of fire and lightning, Xolotl. He apparently disguised himself as a salamander to avoid being sacrificed.\n\n[Source 🔗](<https://www.nationalgeographic.com/animals/amphibians/facts/axolotl>)',
          color=random.choice(colors)),
    
    discord.Embed(
          title='Axolotl Fact 5',
          description='Axolotls are neotenic, keeping their larval characteristics (e.g. their aquatic nature, external gills, a tail, and a body fin) throughout adulthood.\n\n[Source 1 🔗](<https://www.britannica.com/animal/axolotl>) | [Source 2 🔗](<https://animals.sandiegozoo.org/animals/axolotl>) ',
          color=random.choice(colors)),
    
    discord.Embed(
          title='Axolotl Fact 6',
          description='Axolotls eat fish, mollusks, aquatic insects, bloodworms, and other assorted small organisms. Occasionally, they will even eat other axolotls.\n\n[Source 1 🔗](<https://www.britannica.com/animal/axolotl>) | [Source 2 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
      color=random.choice(colors)),
   
    discord.Embed(
          title='Axolotl Fact 7',
          description='Axolotls are only naturally found in Mexico City, specifically in Lake Xochimilco and Lake Chalco.\n\n[Source 🔗](<https://www.britannica.com/animal/axolotl>)',
      color=random.choice(colors)),
    
    discord.Embed(
          title='Axolotl Fact 8',
          description='Axolotls can regenerate limbs and organs fully, although there are occasionally some deformaties.\n\n[Source 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
      color=random.choice(colors)),
    
    discord.Embed(
          title='Axolotl Fact 9',
          description='Axolotls have been classified as endangered since 2006. However, efforts are being made to conserve the wild population, mostly by selling them as pets and introducing captive populations into the wild.\n\n[Source 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
      color=random.choice(colors)),

    discord.Embed(
          title='Axolotl Fact 10',
          description='Axolotls are about 1,000 times more resistant to cancer than other species.\n\n[Source 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
      color=random.choice(colors)),

    discord.Embed(
          title='Axolotl Fact 10',
          description='Axolotls are a bit like chameleons, able to shift the hues a few shades to act as camouflage!\n\n[Source 🔗](<https://animals.sandiegozoo.org/animals/axolotl>)',
      color=random.choice(colors)),

    discord.Embed(
          title='Axolotl Fact 11',
          description='Axolotls were introduced to Paris from Mexico in 1864, sparking a large European (and moreover, global) axolotl trade due to the ease of breeding in captivity.\n\n[Source 🔗](<https://www.nationalgeographic.com/animals/amphibians/facts/axolotl>)',
      color=random.choice(colors)),

     discord.Embed(
          title='Axolotl Fact 12',
          description='It is estimated that only about 1,000 axolotls exist in the wild (as of July 2023).\n\n[Source 🔗](<https://www.britannica.com/animal/axolotl>)',
      color=random.choice(colors)),

     discord.Embed(
          title='Axolotl Fact 13',
          description='Axolotls mate by doing a "waltz".\n\n[Source 🔗](<https://www.nationalgeographic.com/animals/amphibians/facts/axolotl>)',
      color=random.choice(colors))
  ]
  random_fact=random.choice(facts)
  await ctx.send(embed=random_fact)

@client.hybrid_command(description='Sends a random axolotl image')
async def image(ctx):
  await ctx.send(random.choice(gen_img))
  

@client.hybrid_command(description='Pings a selected user and gives them a hug')
async def hug(ctx, user: discord.User):
    await ctx.send(f'Hugs for {user.mention} from {ctx.author.mention}! =^w^=')

@client.hybrid_command(description='Make the bot speak via TTS')
async def speak(ctx):
  await ctx.send('bark', tts=True)

@client.hybrid_command(description='Provides link to suggestion box')
async def suggest(ctx):
  embed = discord.Embed(
      title='AxolotlBot Suggestion Box!',
      description='Thank you for considering helping out AxolotlBot! If you have additions to suggest, you can submit those additions here! You can also report bugs, give general feedback, and say whatever else comes to your mind regarding the bot!\n\nThe link below will direct you to a Google form. The only information collected will be what you provide in the form and the timestamps of any submissions.\n\nQuality user additions will be added to the bot!\n\n[Go to form!](<https://forms.gle/f1A8bbD8qSkjNyDj7>)')
  embed.set_image(url='https://wallpapercave.com/wp/wp8806603.jpg')
  await ctx.send(embed=embed)

try:
  keep_alive()
  client.run(os.environ['TOKEN'])
except Exception as e:
  os.system('kill 1')
