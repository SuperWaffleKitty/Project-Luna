import discord
from discord.ext import commands

#Initiates Help class
class Help(commands.Cog):


    #Initiates the cog
    def __init__(self, client):
        self.client = client


    #Prints update message in terminal
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing Help')


    #Replaces default help command
    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def help(self, ctx):
        await ctx.send("Here is a list of commands:")
        await ctx.send("```**$changeprefix [new prefix]**: Changes custom prefix (Owner Only)" + "\n" + "**$help**: Displays this message" + "\n" + "**$yiff [tag]**: Shows random yiff from e621" + "\n" + "**$fa [tag]**: Shows random FurAffinity Content```")

def setup(client):
    client.add_cog(Help(client))
