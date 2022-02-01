import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def whoami(self, ctx, *, member: discord.Member = None):
        embed=discord.Embed(
            title="Hiya, im Skysha.",
            url="https://leak.cf/",
            description="A discord bot created by Leaked, to learn python!",
            color=discord.Color.dark_purple()
            )
        embed.set_footer(text="Made with ❤ by Leaked | Skysha")
        await ctx.send(embed=embed)

