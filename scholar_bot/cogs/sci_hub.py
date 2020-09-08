from urllib.parse import quote

import discord
from discord.ext import commands
from scholarly import scholarly

from ._formatters import to_lower


SCI_HUB_BASE = "https://sci-hub.tw/{search_term}"


def get_sci_hub_embed(paper_title) -> discord.Embed:
    paper_url = SCI_HUB_BASE.format(search_term=quote(paper_title))
    embed = discord.Embed(
        title=paper_title, url=paper_url, color=discord.Color.magenta()
    )
    return embed


class SciHubCog(commands.Cog):
    @commands.command()
    async def paper(self, ctx, *, paper_title: to_lower):
        """UNDER DEVELOPMENT - Retrieve a paper from SciHub"""
        await ctx.send(embed=get_sci_hub_embed(paper_title))
