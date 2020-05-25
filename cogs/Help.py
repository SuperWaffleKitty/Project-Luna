import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Showing off assets')


    @commands.command()
    async def help(self, ctx):
        await ctx.send('**Commands:**')
        await ctx.send('**!help** : Prints this message')
        await ctx.send('**!fuck** : Sends a random e621 image')
        #await ctx.send('For the full list of cheese commands, click the link Below')
        #await ctx.send('https://github.com/SuperWaffleKitty/CheeseBot/blob/master/COMMANDS.md')






def setup(client):
    client.add_cog(Help(client))
#end
#text
