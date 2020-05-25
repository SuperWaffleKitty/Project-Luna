import discord
import os
import config
from discord.ext import commands


client = commands.Bot(command_prefix = '! ')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Kinky Stuff'))
    print('Bot is being Sexy')


#TEMP, REMOVE THIS LATER
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)




@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(config.BOT_TOKEN)

#YOOT
