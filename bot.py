import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7239366223:AAHXc0KGwVCKnzeEAgX_G0FrUCSRpYUAyEQ")

API_ID = int(os.environ.get("API_ID", "20763817"))

API_HASH = os.environ.get("API_HASH", "07186e8f2ffe607e99eedf7eaa5e630b")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
