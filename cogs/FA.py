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


#This is a terrible implementation of this command, but it does work (somewhat)
    @commands.command()
    async def fa(self, ctx, type):
        Req = requests.get(f"https://faexport.spangle.org.uk/search.json?q={type}")
        ReqJson = Req.json()
        if Req.status_code != 200:
            await ctx.send(f"Couldn't contact FurAffinity. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson[random.randint(0,68)]

        Req = requests.get(f"https://faexport.spangle.org.uk/submission/{Post}.json")
        ReqJson = Req.json()
        if Req.status_code != 200:
            await ctx.send(f"Couldn't contact FurAffinity. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson["full"]
        await ctx.send(f"Here is your FurAffinity content: {Post}")


def setup(client):
    client.add_cog(FA(client))
