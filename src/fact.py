import discord
from src.client import client
import random
import json

fact_list = json.load(open("facts.json"))
colors=[
  0xF44336, 0xE91E63, 0x9C27B0, 0x673AB7, 0x3F51B5, 0x2196F3, 0x03A9F4,
  0x00BCD4, 0x009688, 0x4CAF50, 0x8BC34A, 0xCDDC39, 0xFFEB3B, 0xFFC107,
  0xFF9800, 0xFF5722, 0x795548
]

@client.hybrid_command(description='Generates a random axolotl fact')
async def fact(ctx):
  number = random.choice(list(range(0, len(fact_list))))
  color_choice = random.choice(colors)
  fact_value = fact_list[number]
  embed = discord.Embed(
    title = "Axolotl Fact " + str(number),
    description = fact_value["message"] + "\n\n" + get_source_links(fact_value["source"]),
    color = color_choice
  )
  await ctx.send(embed=embed)

def get_source_links(source: str | list[str]) -> str:
  if isinstance(source, str):
    return "[Source 🔗](<"+source+">)"
  output = ""
  for i in range(0, len(source)):
    link = source[i]
    output += "**[Source "+str(i+1)+" 🔗](<"+link+">)**\n"
  return output
