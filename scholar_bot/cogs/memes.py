import os
import random

import discord
from discord.ext import commands
from imgurpython import ImgurClient


imgur_client_id = os.getenv("IMGUR_CLIENT_ID")
imgur_client_secret = os.getenv("IMGUR_CLIENT_SECRET")
imgur_client = ImgurClient(imgur_client_id, imgur_client_secret)


def imgur(query) -> discord.Embed:
    gallery = random.choice(imgur_client.gallery_search(query.lower()))
    try:
        img_url = random.choice(gallery.images)["link"]
    except AttributeError:
        img_url = gallery.link
    return discord.Embed(title=f"{query} boi", url=img_url).set_image(url=img_url)


class MemeCog(commands.Cog):
    topics = {
        "crinoid": imgur,
        "dinosaur": imgur,
        "skeleton": imgur,
    }

    @commands.command()
    async def pls(self, ctx, topic):
        print(f"Called pls with topic: {topic}")
        if topic not in self.topics:
            await ctx.send(f"No {topic} bois found")
            return

        embed = self.topics[topic](topic)
        await ctx.send(embed=embed)
