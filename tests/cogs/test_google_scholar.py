from unittest.mock import AsyncMock

import pytest
from scholar_bot.cogs.google_scholar import GoogleScholarCog


class TestGoogleScholarCog:
    @classmethod
    def setup_class(cls):
        cls.cog = GoogleScholarCog()

    def setup_method(self):
        self.ctx_mock = AsyncMock()

    @pytest.mark.asyncio
    async def test_hello(self):
        await self.cog.hello(None, self.ctx_mock)
        self.ctx_mock.send.assert_called_once_with("Hello!")

    @pytest.mark.asyncio
    async def test_gscholar(self):
        await self.cog.gscholar(None, self.ctx_mock, author_name="Jeremy Keeler")
        self.ctx_mock.send.assert_called_once_with(f"Searching for: Jeremy Keeler")
