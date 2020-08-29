from datetime import datetime
from urllib.parse import quote

import discord
import feedparser
import pytz
from dateutil import parser as dateparser
from discord.ext import commands
from markdownify import markdownify as md
from operator import itemgetter

EARTH_RSS_FEED = "feed:https://events.umich.edu/group/3170/rss"
DAY_CUTOFF = {
    "month": 30,
    "week": 7,
}
ICAL_BASE = "https://events.umich.edu/event/{event_id}/feed/ical"
EARTH_BASE = (
    "https://lsa.umich.edu/earth/news-events/all-events.detail.html/{event_id}.html"
)
GCAL_BASE = "https://www.google.com/calendar/render?action=TEMPLATE&text={title}&dates={start_date}/{end_date}&trp=false&sprop&sprop=name:&sf=true&output=xml"


def format_gcal_date(d):
    return (
        d.astimezone(tz=pytz.utc)
        .isoformat()
        .replace(":", "")
        .replace("-", "")
        .split("+")[0]
        + "Z"
    )


class EarthCog(commands.Cog):
    @commands.command()
    async def events(self, ctx, cadence="month"):
        cutoff = DAY_CUTOFF.get(cadence, DAY_CUTOFF["month"])
        today = datetime.today().astimezone()
        feed = feedparser.parse(EARTH_RSS_FEED)
        entries = feed["entries"]
        for entry in entries:
            entry["event_start"] = dateparser.parse(entry["ev_startdate"])
            entry["event_end"] = dateparser.parse(entry["ev_enddate"])
            entry["event_date"] = dateparser.parse(entry["ev_startdate"])
            entry["event_id"] = entry["id"].split("@")[0]
        filtered_entries = [
            e
            for e in sorted(entries, key=itemgetter("event_date"))
            if (e["event_date"] - today).days < cutoff
        ]

        if len(filtered_entries) == 0:
            await ctx.send(f"There are no events in the next {cutoff} days.")
            return

        embed = discord.Embed(
            title=f"Events in the next {cutoff} days", color=discord.Color.green()
        )

        for ent in filtered_entries:
            title = "(".join(ent["title"].split("(")[:-1])
            event_url = EARTH_BASE.format(event_id=ent["event_id"])
            ical_link = ICAL_BASE.format(event_id=ent["event_id"])
            gcal_link = GCAL_BASE.format(
                title=quote(title),
                start_date=format_gcal_date(ent["event_start"]),
                end_date=format_gcal_date(ent["event_end"]),
            )
            end_time = "%I:%M %p"
            embed.add_field(
                name=f"{title}",
                value=(
                    f'{ent["event_date"]:%A, %B, %e, %Y} from {ent["event_start"]:%I:%M %p} - {ent["event_end"]:%I:%M %p}\n[event url]({event_url}) '
                    f"| [add to iCal]({ical_link}) | [add to Google]({gcal_link})"
                ),
                inline=False,
            )
        await ctx.send(embed=embed)
