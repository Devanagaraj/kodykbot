from pyrogram import Client, filters

app = Client(
    "my_bot",
	api_id=12345,
	api_hash="0123456789abcdef0123456789abcdef",
	bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
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

app.run()
