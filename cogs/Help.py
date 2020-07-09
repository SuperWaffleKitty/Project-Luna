import discord
from discord.ext import commands

#Initiates Help class
class Help(commands.Cog):

    #Initiates the cog
    def __init__(self, client):
        self.client = client

    #Prints message in terminal when running
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing Help')

    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def help(self, ctx):
        await ctx.send("Here is a list of commands:")
        await ctx.send("```**[prefix]changeprefix [new prefix]**: Changes custom prefix " + "\n" + "**[prefix]help**: Displays this message" + "\n" + "**[prefix]yiff random**: Shows random yiff from e621" + "\n" + "You can use any string after [prefix]yiff to specify tag" + "\n" + "eg: **$yiff gay** or **$yiff wolf**```")
        await ctx.send("Notice: NSFW Commands can only be used in specified NSFW channels" + "\n" + "For more help, visit the readme at https://github.com/superwafflekitty/Project-Luna" + "\n" + "I hope you have a great time :wink:")

def setup(client):
    client.add_cog(Help(client))
