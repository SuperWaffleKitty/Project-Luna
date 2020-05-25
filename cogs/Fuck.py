import discord
from discord.ext import commands

class Fuck(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Providing "Content"')


#    @commands.command()
#    async def cheese(self, ctx):
#        await ctx.send('```TEXT```')



    @commands.command()
    async def mozzarella(self, ctx):
        await ctx.send('```Mozzarella cheese is a sliceable curd cheese originating in Italy. Traditional Mozzarella cheese is made from milk of water buffalos herded in very few countries such as Italy and Bulgaria. As a result, most of the Mozzarella cheeses available now are made from cows milk. It is a semi-soft cheese with a fresh milky flavor```')
        await ctx.send('https://en.wikipedia.org/wiki/Mozzarella')


def setup(client):
    client.add_cog(Fuck(client))
#end
#text
#HEROKU TEST
