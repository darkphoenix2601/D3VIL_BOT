from telethon import events, Button, custom
import re, os
from D3VIL-BOT.events import register
from D3VIL-BOT import telethn as tbot
from D3VIL-BOT import telethn as tgbot
PHOTO = "https://telegra.ph/file/0d239215b8e4382f970ab.mp4"
@register(pattern=("/alive"))
async def awake(event):
 Miss_Akshi = event.sender.first_name
 Miss_Akshi = "β‘ I,m Miss_Akshiπ \n\n"
 Miss_Akshi += "β‘ I'm Working with awesome speed**\n\n"
 Miss_Akshi += "**β‘Miss_Akshi : 1.0 LATEST**\n\n"
 Miss_Akshi += "**β‘ ππΊ π°πΈπ―π¦π³ : [ππ΄π©πΆπ](t.me/Professer_Ashu)\n\n"
 Miss_Akshi += "**β‘ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("ππΆπ±π±π°π³π΅π₯", "https://t.me/Miss_AkshiV1_Support"), Button.url("ππ±π₯π’π΅π¦π΄", "https://t.me/Miss_AkshiV1_Updates")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
