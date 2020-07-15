import discord
import random
import requests
from discord.ext import commands

#Initiates E621 class
class E621(commands.Cog):


    #Initiates the cog
    def __init__(self, client):
        self.client = client


    #Prints update message in terminal
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing e621 "Content"')


    #Post's E621 image based on user criteria
    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)

    #Prevents user from running command in non-NSFW server
    async def yiff(self, ctx, type):
        if not isinstance(ctx.channel, discord.DMChannel):
                if not isinstance(ctx.channel, discord.GroupChannel):
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Cannot be used in non-NSFW channels!")
                        return

        #Changes request format if type = random
        if type == "random":
            headers = {"User-Agent":"Project-Luna/1.0 (API Usage by jezzar on E621)"}
            Req = requests.get(f"https://e621.net/posts.json?tags=order:random+rating:explicit&limit=1", headers=headers)
            ReqJson = Req.json()
            if Req.status_code != 200:
                await ctx.send(f"Couldn't contact e621. Error code: {Req.status_code}.\nJson: {ReqJson}")
                return
            Post = ReqJson["posts"][0]["file"]["url"]
            await ctx.send(f"Here is your {type} yiff: {Post}\nURL: https://e621.net/posts/{ReqJson['posts'][0]['id']}")
            return

        #This doesn't work -_-
        elif not type:
            await ctx.send("For bot help, type $help")

        #Pulls and posts E621 content based on user criteria
        else:
            headers = {"User-Agent":"Project-Luna/1.0 (API Usage by jezzar on E621)"}
            Req = requests.get(f"https://e621.net/posts.json?tags=order:random+{type}+rating:explicit&limit=1", headers=headers)
            ReqJson = Req.json()
            if Req.status_code != 200:
                await ctx.send(f"Couldn't contact e621. Error code: {Req.status_code}.\nJson: {ReqJson}")
                return

            Post = ReqJson["posts"][0]["file"]["url"]
            await ctx.send(f"Here is your {type} yiff: {Post}\nURL: https://e621.net/posts/{ReqJson['posts'][0]['id']}")
            return


def setup(client):
    client.add_cog(E621(client))
