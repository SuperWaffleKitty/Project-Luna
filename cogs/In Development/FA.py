import discord
import random
import requests
from discord.ext import commands

#Initiates FA class
class FA(commands.Cog):

    #Initiates the cog
    def __init__(self, client):
        self.client = client

    #Prints message in terminal when running
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing FA "Content"')


    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def FA(self, ctx, type):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return

        if type == "random":
            Post = random.randint(1000,37155571)
            await ctx.send(f"Here is your XD so Random FA Content: " + f"https://www.furaffinity.net/view/{Post}")
            return

        elif type == "":
            await ctx.send("For bot help, type $help")
            return

        else:
            await ctx.send(f"Keywork Usage is currently unavailable for FurAffinity at the moment due to technical issues. However, it is expected to be available soon.")
            return





def setup(client):
    client.add_cog(FA(client))
