from discord.ext import commands
from scholarly import scholarly


class GoogleScholarCog(commands.Cog):
    @commands.command()
    async def gscholar(self, ctx, *args):
        author_name = " ".join(args).lower()
        # search_query = scholarly.search_author(author_name)
        await ctx.send(f"Searching for: {author_name}")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
