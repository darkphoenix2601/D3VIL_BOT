import os
import sys
from pyrogram import filters
from sys import version as pyver
from D3VIL-BOT import OWNER_ID
from D3VIL-BOT import pbot as app


@app.on_message(filters.command("install") & filters.user(OWNER_ID))
async def install_module(_, message):
    if not message.reply_to_message:
        await message.reply_text("Reply To A .py File To Install It.")
        return
    if not message.reply_to_message.document:
        await message.reply_text("Reply To A .py File To Install It.")
        return
    document = message.reply_to_message.document
    if document.mime_type != "text/x-python":
        await message.reply_text("INVALID_MIME_TYPE, Reply To A Correct .py File.")
        return
    m = await message.reply_text("**Installing Module**")
    await message.reply_to_message.download(f"./D3VIL-BOT/modules/{document.file_name}")
    await m.edit("**Restarting**")
    os.execvp(
        f"python{str(pyver.split(' ')[0])[:3]}",
        [f"python{str(pyver.split(' ')[0])[:3]}", "-m", "D3VIL-BOT"],
    )
