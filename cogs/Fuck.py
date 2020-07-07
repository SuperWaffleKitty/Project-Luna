import discord
import random
import requests
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

    #Returns random e621 post only in NSFW Channels using the E6 API
    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def random(self, ctx):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return
                        
        headers = {"User-Agent":"Project-Luna/1.0 (API Usage by jezzar on E621)"}
        link = random.randint(100,2270250)
        Req = requests.get(f"https://e621.net/posts.json?tags=id:{link}&rating:explicit", headers=headers)
        ReqJson = Req.json()
        if Req.status_code != 200:
            await ctx.send(f"Couldn't contact e621. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson["posts"][0]["file"]["url"]
        await ctx.send(f"Here is your random yiff: {Post}")

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
