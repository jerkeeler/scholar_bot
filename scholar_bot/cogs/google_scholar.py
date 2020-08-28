from discord.ext import commands
from scholarly import scholarly


def to_lower(arg: str):
    return arg.lower()


class GoogleScholarCog(commands.Cog):
    @commands.command()
    async def gscholar(self, ctx, *, author_name: to_lower):
        """UNDER DEVELOPMENT - Retrieve list of recent papers by an author"""
        search_query = scholarly.search_author(author_name)
        try:
            author = next(search_query)
        except StopIteration:
            ctx.send(f"Author {author_name} not found!")
            return
        author = author.fill()
        publications = author.publications[:5]
        await ctx.send(f"Searching for: {author_name}")

    @commands.command()
    async def hello(self, ctx):
        """
        Says hello!
        """
        await ctx.send("Hello!")
