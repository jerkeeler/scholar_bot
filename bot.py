import os
from dotenv import load_dotenv

from scholar_bot import ScholarBot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ScholarBot().run(BOT_TOKEN)
