from discord import channel, client
from fastapi import HTTPException, Depends
from fastapi.responses import PlainTextResponse
from discordBot import app, log, bot
from datetime import date, datetime
from discordBot.models.news import dailyNews



@app.get("/")
def home():
    return {"Hello": str(bot.user.name)}



@app.get("/send")
async def send():
    user = None
    for member in bot.get_all_members():
        if "ChaosHead" in member.name:
            user = member

    log.info(dir(user))
    await user.send("Hello")

    return "DOne"



@app.get("/now")
def date_now():

    return {"date": datetime.now().strftime("%m-%d")}


@app.get("/daily_job")
async def daily_job():
    log.info("TEST")
    news = dailyNews()

    log.info(news)

    return PlainTextResponse(content=news.render_message())


@bot.event
async def on_ready():
    print("START")


@bot.event
async def on_message(message):
    print(message)
