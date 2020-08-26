from discord.ext import commands
from scholarly import scholarly


class GoogleScholarCog(commands.Cog):
    @commands.command()
    async def gscholar(self, ctx, *args):
        """UNDER DEVELOPMENT - Retrieve list of recent papers by an author"""
        author_name = " ".join(args).lower()
        search_query = scholarly.search_author(author_name)
        try:
            author = next(search_query)
        except StopIteration:
            ctx.send(f"Author {author_name} not found!")
            return
        await ctx.send(f"Searching for: {author_name}")

    @commands.command()
    async def hello(self, ctx):
        """
        Says hello!
        """
        await ctx.send("Hello!")
