import config, discord, requests, json
from discord.ext import commands

class hentaicog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def lolis(self, ctx):
        await ctx.send('https://media.very.co.uk/i/very/MFWPY_SQ1_0000000099_N_A_SLf?$550x733_standard$')

    @commands.command()
    async def hentai(self, ctx):
        r = requests.get("https://api.xsky.dev/hentai")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def catboy(self, ctx):
        r = requests.get("https://api.xsky.dev/catboy")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def bsdm(self, ctx):
        r = requests.get("https://api.xsky.dev/bdsm")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def furry(self, ctx):
        r = requests.get("https://api.xsky.dev/furry")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def ff(self, ctx):
        r = requests.get("https://api.xsky.dev/ff")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def nekoirl(self, ctx):
        r = requests.get("https://api.xsky.dev/nekoirl")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def neko(self, ctx):
        r = requests.get("https://api.xsky.dev/neko")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def feet(self, ctx):
        r = requests.get("https://api.xsky.dev/feet")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def trap(self, ctx):
        r = requests.get("https://api.xsky.dev/trap")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def nsfwgif(self, ctx):
        r = requests.get("https://api.xsky.dev/gif")
        data = json.loads(r.content)
        await ctx.send(data['url'])
    @commands.command()
    async def futa(self, ctx):
        r = requests.get("https://api.xsky.dev/futa")
        data = json.loads(r.content)
        await ctx.send(data['url'])