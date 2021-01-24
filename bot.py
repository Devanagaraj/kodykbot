from __future__ import unicode_literals
from pyrogram import Client, filters
import wikipedia
import os
import pyjokes
from quoters import Quote

app = Client(
    "my_bot",
        api_id=YOURAPIID,
        api_hash="YOURAPIHASH",
        bot_token="YOURBOTTOKEN",
)

@app.on_message(filters.command(["hello"]))
async def hello(_, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

@app.on_message(filters.command(["start"]))
async def start(_, message):
    await message.reply_text('''
        Hello NoobCoder, these are some commands you can try,
        /areuded To Check if the bot is Alive
        /creator Creator's GitHub Profile
        /sourcecode Link to GitHub Repo
        /website Creator's Website
        /wikipedia Search For Articles in Wikipedia
        /quote Get Quotes
        /crackjoke Get A Geeky Joke
        /stackoverflow Search For Answers in StackOverFlow
        ''')

@app.on_message(filters.command(["howztheworld"]))
async def howzwrld(_, message):
    await message.reply_text("The world is not perfect but it aint that bad...")

@app.on_message(filters.command(["creator"]))
async def creator(_, message):
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

@app.on_message(filters.command(["website"]))
async def website(_, message):
    await message.reply_text("nice-panda-91.telebit.io")

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

@app.on_message(filters.command(['cancelshutdown']) & filters.user(["kody_k"]))
async def cancelshutdown(_, message):
    await message.reply_text("Shutting Down Servers Cancelled")
    os.system("sudo shutdown -c")

@app.on_message(filters.command(['crackjoke']))
async def crackjoke(_, message):
    joke = pyjokes.get_joke(language="en", category="neutral")
    await message.reply_text(joke)

@app.on_message(filters.command(['quote']))
async def quoter(_, message):
    quote = Quote.print()
    await message.reply_text(quote)

@app.on_message(filters.command(['stackoverflow']))
async def stackoverflow(_, message):
        try:
            stfquery = message.text.split(None,1)[1]
            await message.reply_text("Searching for Answers...")
            stfresult = os.popen('howdoi ' + stfquery ).read()
            await message.reply_text(stfresult)
        except:
            await message.reply_text("Found Nothing...")

app.run()



