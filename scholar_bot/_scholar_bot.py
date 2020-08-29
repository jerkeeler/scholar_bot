from discord.ext import commands

from .cogs import EarthCog, GoogleScholarCog, MemeCog, SciHubCog


class ScholarBot(commands.Bot):
    def __init__(self, *args, command_prefix=".", **kwargs):
        super().__init__(command_prefix, *args, **kwargs)
        self.add_cog(GoogleScholarCog())
        self.add_cog(SciHubCog())
        self.add_cog(MemeCog())
        self.add_cog(EarthCog())

    async def on_ready(self):
        print(f"Ready as {self.user}!")
