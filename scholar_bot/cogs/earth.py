from datetime import datetime

import discord
import feedparser
from dateutil import parser as dateparser
from discord.ext import commands
from markdownify import markdownify as md
from operator import itemgetter

EARTH_RSS_FEED = "feed:https://events.umich.edu/group/3170/rss"
DAY_CUTOFF = {
    "month": 30,
    "week": 7,
}


class EarthCog(commands.Cog):
    @commands.command()
    async def events(self, ctx, cadence="month"):
        cutoff = DAY_CUTOFF.get(cadence, DAY_CUTOFF["month"])
        today = datetime.today().astimezone()
        feed = feedparser.parse(EARTH_RSS_FEED)
        entries = feed["entries"]
        for entry in entries:
            entry["event_date"] = dateparser.parse(entry["ev_startdate"])
        filtered_entries = [
            e
            for e in sorted(entries, key=itemgetter("event_date"))
            if (e["event_date"] - today).days < cutoff
        ]
        embed = discord.Embed(
            title=f"Events in the next {cutoff} days", color=discord.Color.green()
        )

        for ent in filtered_entries:
            embed.add_field(
                name=f'{ent["title"]}',
                value=ent["event_date"].strftime("%A, %B, %e, %Y at %I:%M %p"),
                # value=f'{md(ent["summary"]).strip()}\n[event url]({ent["link"]})',
                inline=False,
            )
        await ctx.send(embed=embed)
