from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("š zoneunlimited š ", url="https://t.me/zoneunlimited")],
        [InlineKeyboardButton(
            "š zoneunlimited chat š", url="https://t.me/zoneunlimitedchat")]
    ])
    welcomed = f"š Hello There{message.from_user.first_name}\n\nšāāļø I am youtube downloader bot š„,I can\n\nšµ Downloading All **song**\nš· Downloading All **Video**\nā­ļø **Inline search**\nšŗ Group Supported\nšÆ** 24 horse active**\n\nšæ Developer : @bimsaramalinga\n\nš„ š  @zoneunlimited  š Corporation Ā©ļø"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
