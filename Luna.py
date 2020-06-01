import discord
import os
import config
from discord.ext import commands

#Sets the command prefix
client = commands.Bot(command_prefix = '!fuck ')

#Removes the default help command
client.remove_command('help')


#Changes the bot's custom status & displays that the bot is running in the terminal.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Kinky Stuff'))
    print('Bot is being Sexy')


#TEMP, REMOVE THIS LATER
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Command to load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Command to unload cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#Removes .cog from info display
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#runs the client and checks for Bot Token
client.run(config.BOT_TOKEN)
