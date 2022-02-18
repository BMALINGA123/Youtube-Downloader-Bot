from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍀 zoneunlimited 🍀 ", url="https://t.me/zoneunlimited")],
        [InlineKeyboardButton(
            "🍀 zoneunlimited chat 🍀", url="https://t.me/zoneunlimitedchat")]
    ])
    welcomed = f"🍀 Hello There{message.from_user.first_name}\n\n🙋‍♂️ I am YOUTUBE DOWNLOADER BOT 🎥,I can\n\n🎵 Downloading All song\n🌷 Downloading All Video\n\n⭕️ Inline search\n🌺 Group Supported\n🎯 24 horse active\n\n🔥 Bot Commands 🔥\n/song\n/video\n\n🌿 Developer : @chamod_deshan\n\n🔥 [🍀  zoneunlimited  🍀](https://t.me/zoneunlimited) Corporation ©️"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
