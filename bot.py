from __future__ import unicode_literals
from pyrogram import Client, filters
import wikipedia
import os

app = Client(
    "my_bot",
        api_id=REPLACE_WITH_YOUR_API_ID,
        api_hash="REPLACE_WITH_YOUR_API_HASH",
        bot_token="REPLACE_WITH_YOUR_BOT_TOKEN",
)

@app.on_message(filters.command(["hello"]))
async def hello(_, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

@app.on_message(filters.command(["howztheworld"]))
async def howzwrld(_, message):
    await message.reply_text("The world is not perfect but it aint that bad...")

@app.on_message(filters.command(["whomadeu"]))
async def whomadeu(_, message):
    await message.reply_text("https://github.com/Kody-K/")

@app.on_message(filters.command(["sourcecode"]))
async def whomadeu(_, message):
    await message.reply_text("https://github.com/Kody-K/kodykbot")

@app.on_message(filters.command(["killyourself"]))
async def killyourself(_, message):
    await message.reply_text(f"same 2 you {message.from_user.mention}")

@app.on_message(filters.command(["areuded"]))
async def areuded(_, message):
    await message.reply_text("i am alive, go to hell")

@app.on_message(filters.command(['wikipedia']))
async def wikisearch(_, message):
        wikiquery = message.text.replace("wikipedia ", '')
        try:
            await message.reply_text("Searching Wikipedia...")
            wikiresult = wikipedia.summary(wikiquery, sentences = 4)
            await message.reply_text(wikiresult)
        except:
            await message.reply_text("Found Nothing...")

@app.on_message(filters.command(['shutdown']) & filters.user(["kody_k"]))
async def shutdown(_, message):
    await message.reply_text("Shutting Down Servers in 60s...")
    os.system("sudo shutdown")

@app.on_message(filters.command(['cancelshutdown']))
async def cancelshutdown(_, message):
    await message.reply_text("Shutting Down Servers Cancelled")
    os.system("sudo shutdown -c")

app.run()
