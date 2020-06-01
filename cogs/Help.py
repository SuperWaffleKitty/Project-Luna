import discord
from discord.ext import commands

#Initiates Help Class
class Help(commands.Cog):

    #Initializes the cog
    def __init__(self, client):
        self.client = client

    #Prints message in terminal when running
    @commands.Cog.listener()
    async def on_ready(self):
        print('Showing off assets')

    #Gives description of each cog
    @commands.command()
    async def help(self, ctx):
        await ctx.send('**Commands:**')
        await ctx.send('**!fuck help** : Prints this message')
        await ctx.send('**!fuck random** : Sends a random e621 image')


def setup(client):
    client.add_cog(Help(client))
