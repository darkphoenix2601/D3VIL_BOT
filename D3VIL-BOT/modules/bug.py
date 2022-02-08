from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from D3VIL-BOT import pbot as Client
from D3VIL-BOT import (
    OWNER_ID as owner,
    SUPPORT_CHAT as log,
)
from D3VIL-BOT.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username}")
    else:
        chat_username = ("Private Group")


    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "http://telegra.ph//file/2aa79f97f436845d44dbd.mp4"
    
    bug_report = f"""
**#BUG**
**From User : ** **{mention}**
**User ID : ** **{user_id}**
**Group : ** **{chat_username}**
**Bug Report : ** **{bugs}**
**Event Stamp : ** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("❎ <b>This command only works in groups.</b>")
        return

    if user_id == owner:
        if bugs:
            await msg.reply_text(
                f"❎ <b>How can be owner bot reporting bug idiot??</b>",
            )
            return
        else:
            await msg.reply_text(
                f"❎ <b>Owner noob!</b>",
            )
    elif user_id != owner:
        if bugs:
            await msg.reply_text(
                f"<b>Bug Report : {bugs}</b>\n\n"
                "✅ <b>The bug was successfully reported to the support group!</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Close", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                log,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Bug", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "❌ Close", callback_data=f"close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"❎ <b>No bug to Report!</b>",
            )
        
    

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(Client, CallbackQuery):
    await CallbackQuery.message.delete()


__mod_name__ = "Bug"
