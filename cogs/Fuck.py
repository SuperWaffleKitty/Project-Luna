import discord
import random
from discord.ext import commands

class Fuck(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing "Content"')


    #@commands.command()
    #async def script(self, ctx):
    #    await ctx.send('```Currently, the sonic script is unavailable```')
    #    await ctx.send('```THIS IS NOT EBIC```')




    @commands.command()
    async def random(self, ctx):

        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return
        link = random.randint(100,2270250)
        await ctx.send('https://e621.net/posts/' + str(link))
    #https://e621.net/posts?page=2&tags=anthro

    @commands.command()
    async def me(self, ctx):
        await ctx.send("Well that's depressing")

    @commands.command()
    async def you(self, ctx):
        await ctx.send("My pleasure")

    @commands.command()
    async def yourself(self, ctx):
        await ctx.send("Why don't you do it for me pussy.")


def setup(client):
    client.add_cog(Fuck(client))
#end
#text
#HEROKU TEST
