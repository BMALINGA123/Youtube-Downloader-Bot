from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍀 zoneunlimited 🍀 ", url="https://t.me/zoneunlimited")],
        [InlineKeyboardButton(
            "🍀 zoneunlimited chat 🍀", url="https://t.me/zoneunlimitedchat")]
    ])
    welcomed = f"🍀 Hello There{message.from_user.first_name}\n\n🙋‍♂️ I am youtube downloader bot 🎥,I can\n\n🎵 Downloading All **song**\n🌷 Downloading All **Video**\n⭕️ **Inline search**\n🌺 Group Supported\n🎯** 24 horse active**\n\n🌿 Developer : @bimsaramalinga\n\n🔥 🍀  @zoneunlimited  🍀 Corporation ©️"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
