import os

import cloudmersive_virus_api_client
from telethon.tl import functions, types
from telethon.tl.types import DocumentAttributeFilename, MessageMediaDocument

from D3VIL-BOT.conf import get_str_key
from D3VIL-BOT.events import register
from D3VIL-BOT import telethn as tbot


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


VIRUS_API_KEY = get_str_key("VIRUS_API_KEY", required=False)
configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key["Apikey"] = VIRUS_API_KEY
api_instance = cloudmersive_virus_api_client.ScanApi(
    cloudmersive_virus_api_client.ApiClient(configuration)
)
allow_executables = True
allow_invalid_files = True
allow_scripts = True
allow_password_protected_files = True


@register(pattern="^/scanit$")
async def virusscan(event):
    if event.fwd_from:
        return
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        else:
            return
    if not event.reply_to_msg_id:
        await event.reply("Reply to a file to scan it.")
        return

    c = await event.get_reply_message()
    try:
        c.media.document
    except Exception:
        await event.reply("Thats not a file.")
        return
    h = c.media
    try:
        k = h.document.attributes
    except Exception:
        await event.reply("Thats not a file.")
        return
    if not isinstance(h, MessageMediaDocument):
        await event.reply("Thats not a file.")
        return
    if not isinstance(k[0], DocumentAttributeFilename):
        await event.reply("Thats not a file.")
        return
    try:
        virus = c.file.name
        await event.client.download_file(c, virus)
        gg = await event.reply("Scanning the file ...")
        fsize = c.file.size
        if not fsize <= 3145700:  # MAX = 3MB
            await gg.edit("File size exceeds 3MB")
            return
        api_response = api_instance.scan_file_advanced(
            c.file.name,
            allow_executables=allow_executables,
            allow_invalid_files=allow_invalid_files,
            allow_scripts=allow_scripts,
            allow_password_protected_files=allow_password_protected_files,
        )
        if api_response.clean_result is True:
            await gg.edit("This file is safe ✔️\nNo virus detected 🐞")
        else:
            await gg.edit("This file is Dangerous ☠️️\nVirus detected 🐞")
        os.remove(virus)
    except Exception as e:
        print(e)
        os.remove(virus)
        await gg.edit("Some error occurred.")
        return


_mod_name_ = "Virus Scan"
_help_ = """
 - /scanit: Scan a file for virus (MAX SIZE = 3MB)
 """
