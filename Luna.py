import discord, os, config, math
from discord.ext import commands
from humanfriendly import format_timespan

client = commands.Bot(command_prefix = '!fuck ')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Kinky Stuff'))
    print('Bot is being Sexy')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_command_error(ctx, error):
    ignored = (commands.CommandNotFound, commands.UserInputError)
    if hasattr(ctx.command,"on_error"):
        return
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        return
    elif isinstance(error, commands.CommandOnCooldown):
        seconds = math.ceil(error.retry_after)
        towait = format_timespan(seconds)
        return await ctx.send(f"Woah woah, slow down there, you have to wait {towait} to do this command again.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config.BOT_TOKEN)
