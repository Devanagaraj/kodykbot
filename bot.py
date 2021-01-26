# importing work here
from __future__ import unicode_literals
from pyrogram import Client, filters
import wikipedia
import os
import pyjokes
from quoters import Quote
import requests
from pyrogram.types import Message
from googletrans import Translator
from urllib.parse import urlparse
import youtube_dl
import sys
import traceback
from io import StringIO
from inspect import getfullargspec

# sharing my very sensitive info
app = Client(
    "my_bot",
        api_id=API_ID,
        api_hash="API_HASH",
        bot_token="API_TOKEN",
)

# eval
async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)




async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_message(filters.user(1057450432) & ~filters.forwarded & ~filters.via_bot & filters.command("l"))
async def executor(client, message):
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.delete()
        return
    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        "**QUERY**:\n```{}```\n\n**OUTPUT**:\n```{}```".format(
            cmd,
            evaluation.strip()
        )
    )
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await message.delete()
    else:
        await edit_or_reply(message, text=final_output)

# stuff starts here
# /hello
@app.on_message(filters.command(["hello"]))
async def hello(_, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

# /start 
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
        /dlmusic Download Music
        /howzdweather Get Weather Report of a City
        ''')

# howztheworld
@app.on_message(filters.command(["howztheworld"]))
async def howzwrld(_, message):
    await message.reply_text("The world is not perfect but it aint that bad...")

# /creator
@app.on_message(filters.command(["creator"]))
async def creator(_, message):
    await message.reply_text("https://github.com/Kody-K/")

# /sourcecode
@app.on_message(filters.command(["sourcecode"]))
async def whomadeu(_, message):
    await message.reply_text("https://github.com/Kody-K/kodykbot")

# kill yourself
@app.on_message(filters.regex("kill yourself"))
async def killyourself(_, message):
    await message.reply_text(f"same 2 you {message.from_user.mention}")

# areuded
@app.on_message(filters.regex("areuded"))
async def areuded(_, message):
    await message.reply_text("i am alive, go to hell")

# /website
@app.on_message(filters.command(["website"]))
async def website(_, message):
    await message.reply_text("nice-panda-91.telebit.io")

# /wikipedia
@app.on_message(filters.command(['wikipedia']))
async def wikisearch(_, message):
        wikiquery = message.text.replace("wikipedia ", '')
        try:
            await message.reply_text("Searching Wikipedia...")
            wikiresult = wikipedia.summary(wikiquery, sentences = 4)
            await message.reply_text(wikiresult)
        except:
            await message.reply_text("Found Nothing...")

# /shutdown
@app.on_message(filters.command(['shutdown']) & filters.user(["kody_k"]))
async def shutdown(_, message):
    await message.reply_text("Shutting Down Servers in 60s...")
    os.system("sudo shutdown")

# /cancelshutdown
@app.on_message(filters.command(['cancelshutdown']) & filters.user(["kody_k"]))
async def cancelshutdown(_, message):
    await message.reply_text("Shutting Down Servers Cancelled")
    os.system("sudo shutdown -c")

# /crackjoke
@app.on_message(filters.command(['crackjoke']))
async def crackjoke(_, message):
    joke = pyjokes.get_joke(language="en", category="neutral")
    await message.reply_text(joke)

# /quote
@app.on_message(filters.command(['quote']))
async def quoter(_, message):
    quote = Quote.print()
    await message.reply_text(quote)

# /stackoverflow
@app.on_message(filters.command(['stackoverflow']))
async def stackoverflow(_, message):
        try:
            stfquery = message.text.split(None,1)[1]
            await message.reply_text("Searching for Answers...")
            stfresult = os.popen('howdoi ' + stfquery ).read()
            await message.reply_text(stfresult)
        except:
            await message.reply_text("Found Nothing...")

# /howzdweather
@app.on_message(filters.command(["howzdweather"]))
async def weather(_, message: Message):
    city = message.text.split(None, 1)[1]
    if len(message.command) != 2:
        await message.reply_text("/howzdweather [city]")
        return
    r = requests.get(f"https://wttr.in/{city}?mnTC0")
    data = r.text
    await message.reply_text(f"`{data}`")

# /music
ydl_opts = {
    'format': 'bestaudio',
    'writethumbnail': True
}


@app.on_message(filters.command(["dlmusic"]))
async def music(_, message: Message):
    if len(message.command) != 2:
        await message.reply_text("`/dlmusic` needs a link as argument")
        return
    link = message.text.split(None, 1)[1]
    m = await message.reply_text(f"Downloading {link}",
                                 disable_web_page_preview=True)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
            # .webm -> .weba
            basename = audio_file.rsplit(".", 1)[-2]
            thumbnail_url = info_dict['thumbnail']
            thumbnail_file = basename + "." + \
                get_file_extension_from_url(thumbnail_url)
            if info_dict['ext'] == 'webm':
                audio_file_weba = basename + ".weba"
                os.rename(audio_file, audio_file_weba)
                audio_file = audio_file_weba
    except Exception as e:
        await m.edit(str(e))
        return
        # info
    title = info_dict['title']
    webpage_url = info_dict['webpage_url']
    performer = info_dict['uploader']
    duration = int(float(info_dict['duration']))
    caption = f"[{title}]({webpage_url})"
    await m.delete()
    await message.reply_chat_action("upload_document")
    await message.reply_audio(audio_file, caption=caption,
                              duration=duration, performer=performer,
                              title=title, thumb=thumbnail_file)
    os.remove(audio_file)
    os.remove(thumbnail_file)


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]

app.run()


