import discord
import random
from discord.ext import commands

#Initiates Fuck class
class Fuck(commands.Cog):

    #Initiates the cog
    def __init__(self, client):
        self.client = client

    #Prints message in terminal when running
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing "Content"')


    #Returns random e621 post only in NSFW Channels
    @commands.command()
    async def random(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return
        link = random.randint(100,2270250)
        await ctx.send('https://e621.net/posts/' + str(link))

    #Note for myself: https://e621.net/posts?page=&tags=

    #Simple message return command
    @commands.command()
    async def me(self, ctx):
        await ctx.send("Well that's depressing")

    #Simple message return command
    @commands.command()
    async def you(self, ctx):
        await ctx.send("My pleasure")

    #Simple message return command
    @commands.command()
    async def yourself(self, ctx):
        await ctx.send("Why don't you do it for me pussy.")


def setup(client):
    client.add_cog(Fuck(client))
