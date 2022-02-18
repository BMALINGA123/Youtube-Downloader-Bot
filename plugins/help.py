from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Send YouTube Url.... 🍀"
    await message.reply_text(helptxt)
