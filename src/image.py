from src.client import client
import random

gen_img=['https://upload.wikimedia.org/wikipedia/commons/7/75/Ambystoma_mexicanum_1zz.jpg', 'https://www.premierpet.com.au/productimages/GXA800-15.jpg']

@client.hybrid_command(description='Sends a random axolotl image')
async def image(ctx):
  await ctx.send(random.choice(gen_img))
