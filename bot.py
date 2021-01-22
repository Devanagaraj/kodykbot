from __future__ import unicode_literals
from pyrogram import Client, filters
import youtube_dl
import glob
import os
ydl_opts = {"format": "bestaudio"}

app = Client(
    "my_bot",
        api_id=id,
        api_hash="hash",
        bot_token="token",
)

@app.on_message(filters.command(["hello"]))
async def start(_, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

@app.on_message(filters.command(["howztheworld"]))
async def start(_, message):
    await message.reply_text("The world is not perfect but it aint that bad...")

@app.on_message(filters.command(["whomadeu"]))
async def start(_, message):
    await message.reply_text("kodyk spent 10 mins breaking his fingers on the keyboard")

@app.on_message(filters.command(["killyourself"]))
async def start(_, message):
    await message.reply_text(f"same 2 you {message.from_user.mention}")

@app.on_message(filters.command(["areuded"]))
async def start(_, message):
    await message.reply_text("i am alive, go to hell")

@app.on_message(filters.command(['ytdldownload']))
async def start(_, message):
        text = message.text.replace("/ytdldownload ", '')
        await message.reply_text("Downloading From Kritarth's Very Slow Internet Connection...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(text, download=False)
                audio_file = ydl.prepare_filename(info_dict)
                ydl.process_info(info_dict)
                os.rename(audio_file, "music.webm")
        await message.reply_audio("music.webm")
        os.system("rm -r ~/Kode/kodykbot/*.webm")
app.run()
