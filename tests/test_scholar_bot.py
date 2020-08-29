import unittest

from scholar_bot import ScholarBot


class TestScholarBot:
    @classmethod
    def setup_class(cls):
        cls.bot = ScholarBot()

    def test_correct_cogs(self):
        expected_cogs = {"GoogleScholarCog", "SciHubCog", "MemeCog"}
        assert expected_cogs == set(self.bot.cogs.keys())
