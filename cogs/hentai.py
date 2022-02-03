import requests, hmtai
from discord.ext import commands

class Hentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ass(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "ass"))

    @commands.command()
    async def bdsm(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "bsdm"))

    @commands.command()
    async def cum(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "cum"))

    @commands.command()
    async def creampie(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "creampie"))

    @commands.command()
    async def manga(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "manga"))

    @commands.command()
    async def femdom(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "femdom"))

    @commands.command()
    async def hentai(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "hentai"))

    @commands.command()
    async def incest(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "incest"))

    @commands.command()
    async def masturbation(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "masturbation"))

    @commands.command()
    async def public(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "public"))

    @commands.command()
    async def ero(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "ero"))

    @commands.command()
    async def orgy(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "orgy"))

    @commands.command()
    async def elves(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "elves"))

    @commands.command()
    async def yuri(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "yuri"))

    @commands.command()
    async def glasses(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "glasses"))

    @commands.command()
    async def cuckold(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "cuckold"))

    @commands.command()
    async def blowjob(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "blowjob"))

    @commands.command()
    async def foot(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "foot"))

    @commands.command()
    async def thighs(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "thighs"))

    @commands.command()
    async def ahegao(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "ahegao"))

    @commands.command()
    async def uniform(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "uniform"))

    @commands.command()
    async def gangbang(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "gangbang"))

    @commands.command()
    async def tentacles(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "tentacles"))

    @commands.command()
    async def nsfwneko(self, ctx):
        await ctx.send(hmtai.useHM("2_9", "nsfwneko"))

    @commands.command()
    async def zetryo(self, ctx):
        await ctx.send(hmtai.useHM("2_6", "zetRyo"))

    @commands.command()
    async def trap(self, ctx):
        r = requests.get("https://api.xsky.dev/trap")
        data = r.json()
        await ctx.send(data["url"])
