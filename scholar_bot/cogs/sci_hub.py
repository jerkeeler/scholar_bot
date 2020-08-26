from discord.ext import commands


class SciHubCog(commands.Cog):
    @commands.command()
    async def paper(self, ctx, *args):
        paper_title = " ".join(args).lower()
        await ctx.send(f"Serching SciHub for: {paper_title}")
