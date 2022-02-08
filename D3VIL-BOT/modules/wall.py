import asyncio
from aiohttp import ClientSession
from Python_ARQ import ARQ
import random
from pyrogram import filters
from D3VIL-BOT import pbot as bot

api_key = ('DZBUPV-KNPRIS-YYTDAI-EEHZSK-ARQ') # get it from @arqrobot
api_url = "https://thearq.tech"
session = ClientSession()
arq = ARQ(api_url, api_key, session)


@bot.on_message(filters.command('wall'))
async def main(_,message):
        wall_ = message.text.replace(message.text.split(' ')[0], '')
        results = await arq.wall(wall_)
        wallpaper = results.result
        x = random.choice(wallpaper)
        print(x.url_image)
        await message.reply_photo(photo=x.url_image, caption="Preview")
        await message.reply_document(x.url_image)
        await session.close()
