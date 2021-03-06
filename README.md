# ScholarBot

ScholarBot is a Discord bot that can query various scholarly resources such as Google Scholar, SciHub, etc...

## Setup

This project uses [Poetry](https://python-poetry.org) for dependency management, please set Poetry up before proceeding.

1. Clone this repo
2. Create a bot account on Discord
3. Create a .env file in the root and add:

```
BOT_TOKEN=<insert your token>
```

4. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to isolate your dependencies
5. Install all dependencies with `poetry install`
6. Run the bot: `python bot.py`

### Memes

If you want to do memes you will also need to get a client id and client secret from teh [Imgure API](https://api.imgur.com).

Once you do add the following to your .env file:
```bash
IMGUR_CLIENT_ID=<client id>
IMGUR_CLIENT_SECRET=<client secret>
```

