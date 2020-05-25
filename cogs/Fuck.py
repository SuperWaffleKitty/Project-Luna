import discord
import random
from discord.ext import commands

class Fuck(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing "Content"')


    @commands.command()
    async def fuck(self, ctx):
        await ctx.send('https://e621.net/posts/' + random.randint(100,2270250)


def setup(client):
    client.add_cog(Fuck(client))
#end
#text
#HEROKU TEST
