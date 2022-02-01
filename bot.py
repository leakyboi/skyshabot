# Imports
import config, discord
from cogs.testcog import testcog
from cogs.hentai import Hentai
from cogs.general import General
from discord.ext import commands

# Define some bot stuff
bot = commands.Bot(command_prefix=config.prefix)

# Called when bot just started.
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Game("The official PornHub Game.")
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

@commands.command(name='reload', hidden=True)
async def _reload(self, *, module : str):
    """Reloads a module."""
    try:
        self.bot.unload_extension(module)
        self.bot.load_extension(module)
    except Exception as e:
        await self.bot.say('\N{PISTOL}')
        await self.bot.say('{}: {}'.format(type(e).__name__, e))
    else:
        await self.bot.say('\N{OK HAND SIGN}')

# Loads cogs
bot.add_cog(Hentai(bot))
bot.add_cog(General(bot))

# Starts the bot.
bot.run(config.token)