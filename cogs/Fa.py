import discord
import random
import requests
from discord.ext import commands

#Initiates Fa class
class Fa(commands.Cog):


    #Initiates the cog
    def __init__(self, client):
        self.client = client

    #Prints update message in terminal
    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing FA "Content"')


    #Post's FurAffinity image based on user criteria
    @commands.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def fa(self, ctx, type):
        FAMsg = await ctx.send("Getting FA post")
        #Finds random post id based on user criteria.
        Req = requests.get(f"https://faexport.spangle.org.uk/search.json?q={type}")
        ReqJson = Req.json()
        if Req.status_code != 200:
            await FAMsg.edit(content=f"Couldn't contact FurAffinity. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        Post = ReqJson[random.randint(0,len(ReqJson) - 1)]
        
        #Finds and returns image data based on post ID.
        Req = requests.get(f"https://faexport.spangle.org.uk/submission/{Post}.json")
        ReqJson = Req.json()
        if Req.status_code != 200:
            await FAMsg.edit(content=f"Couldn't contact FurAffinity. Error code: {Req.status_code}.\nJson: {ReqJson}")
            return
        try:
            Post = ReqJson["full"]
        except KeyError:
            await FAMsg.edit(content=f"There was an error getting your FA content. Error Message: {ReqJson['error']}")
            return
        await FAMsg.edit(content=f"Here is your FurAffinity content: {Post}")


def setup(client):
    client.add_cog(Fa(client))
