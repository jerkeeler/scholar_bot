import discord
from discord.ext import commands
from fp.fp import FreeProxy
from scholarly import scholarly

from ._formatters import to_lower
from scholar_bot._scholarly_proxy import get_new_proxy

NUMBER_ARTICLES = 3
PROFILE_URL = "https://scholar.google.com/citations?user={profile_id}&hl=en&oi=ao"


def gen_scholar_embed(author, publications) -> discord.Embed:
    profile_url = PROFILE_URL.format(profile_id=author.id)
    embed = discord.Embed(
        title=author.name, url=profile_url, color=discord.Color.magenta()
    ).set_thumbnail(url=author.url_picture)

    for pub in publications:
        author = pub.bib["author"]
        if len(author) > 50:
            author = author[:50] + "..."
        embed.add_field(
            name=f"{pub.bib['title']}",
            value=f"{author}\n*[{pub.bib.get('journal', 'N/A')}, {pub.bib['year']}]({pub.bib['url']})*",
            inline=False,
        )
    return embed


class GoogleScholarCog(commands.Cog):
    def __init__(self):
        super().__init__()

    @commands.command()
    async def gscholar(self, ctx, *, author_name: to_lower):
        """UNDER DEVELOPMENT - Retrieve list of recent papers by an author"""
        while True:
            search_query = scholarly.search_author(f'"{author_name}"')
            try:
                author = next(search_query)
                break
            except StopIteration:
                await ctx.send(f"Author {author_name} not found!")
                return
            except Exception:
                print("Error retrieving author.")
                get_new_proxy()

        author = author.fill()
        publications = [p.fill() for p in author.publications[:NUMBER_ARTICLES]]
        embed = gen_scholar_embed(author, publications)
        await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        """
        Says hello!
        """
        await ctx.send("Hello!")
