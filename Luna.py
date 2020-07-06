import discord, os, config, math
from discord.ext import commands
from humanfriendly import format_timespan

#Sets the command prefix
client = commands.Bot(command_prefix = '!fuck ')

#Removes the default help command
client.remove_command('help')


#Changes the bot's custom status & displays that the bot is running in the terminal.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Kinky Stuff'))
    print('Bot is being Sexy')

#Command to load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Command to unload cogs
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

#Removes .cog from info display
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#runs the client and checks for Bot Token
client.run(config.BOT_TOKEN)
