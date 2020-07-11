import discord, os, config, math
import json
from discord.ext import commands
from humanfriendly import format_timespan


#Loads Guild Specific Prefix
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


#Set's prefix for guild
client = commands.Bot(command_prefix = get_prefix)


#Removes the default help command
client.remove_command('help')


#Introduces self & initializes prefix when joining guild
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Hello I'm Luna, and I'm here to rock your world :wink:" + '\n' + "You can type '$yiff help' for a list of commands" + '\n' + "If you want to get inside of me, visit my github page:" + '\n' + "https://github.com/SuperWaffleKitty/Project-Luna")
        break


#Removes guild specific prefix when kicked from guild
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


#Allows for guild users to change prefix (must be owner)
@client.command()
@commands.is_owner()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'prefix changed to: {prefix}')


#Changes the bot's custom status & displays that the bot is running in the terminal.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity('Being Naughty :wink:'))
    print('Bot is being Sexy')


#Command to load cogs (must be owner)
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


#Command to unload cogs (must be owner)
@client.command()
@commands.is_owner()
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
