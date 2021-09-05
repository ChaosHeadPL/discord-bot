import os
import logging
from logging.config import dictConfig
import discord
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from discordBot.settings.log_config import LogConfig
# from discordBot.bot_client import bot

BASE_DIR = os.path.dirname(__file__)


# init app:
app = FastAPI()


# init discord bot:
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)


# CORS:
origins = ["https://localhost:300"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods="*",
    allow_headers="*",
)


# init logger:
dictConfig(LogConfig().dict())
log = logging.getLogger("applogger")


# load settings:
from discordBot.settings.config import Settings
config = Settings().dict()


# startup event:
@app.on_event("startup")
async def startup_event():
    log.info("Starting discord bot")
    asyncio.create_task(bot.start(config.get("TOKEN")))


# import routes:
import discordBot.routes
