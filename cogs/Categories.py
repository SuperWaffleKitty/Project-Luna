import discord
import random
import requests
from discord.ext import commands

#Initiates Categories class
class Categories(commands.Cog):

    #Initiates the cog
    def __init__(self, client):
        self.client = client

    #Prints message in terminal when running
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing e621 "Content"')

    #Prints random e621 Content
    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def random(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return
        headers = {"User-Agent":"Project-Luna/1.0 (API Usage by jezzar on E621)"}
        Req = requests.get(f"https://e621.net/posts.json?tags=order:random&rating:explicit&limit=1", headers=headers)
        ReqJson = Req.json()
        if Req.status_code != 200:
            await ctx.send(f"Couldn't contact e621. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson["posts"][0]["file"]["url"]
        await ctx.send(f"Here is your random yiff: {Post}")


    #Supports all tag types
    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def tag(self, ctx, type):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return
                headers = {"User-Agent":"Project-Luna/1.0 (API Usage by jezzar on E621)"}
        Req = requests.get(f"https://e621.net/posts.json?tags=order:random+{type}&rating:explicit&limit=1", headers=headers)
        ReqJson = Req.json()
        if Req.status_code != 200:
            await ctx.send(f"Couldn't contact e621. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson["posts"][0]["file"]["url"]
        await ctx.send(f"Here is your random {type} yiff: {Post}")


def setup(client):
    client.add_cog(Categories(client))
