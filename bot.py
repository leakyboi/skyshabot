# Imports
import os
import config
from cogs.testcog import testcog
from discord.ext import commands

# Define some bot stuff
bot = commands.Bot(command_prefix=config.prefix)

# Called when bot just started.
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# Loads cogs
bot.add_cog(testcog(bot))

# Starts the bot.
bot.run(config.token)