import os
import time
import pathlib
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon import sync, events
from telethon.helpers import TotalList

load_dotenv()

n = 0
ss = 1000
# количество песен в группе

current_dir = pathlib.Path.cwd()

directory = str(current_dir) + "\data"

api_id = os.getenv("API_ID")
# ваш api_id
api_hash = os.getenv("API_HASH")
session = str("anon")
client = TelegramClient(session, api_id, api_hash)

client.start()

while True:

    msgs = client.get_messages('kz_music_base', limit=ss)
    for msg in msgs:
        if msg.media is not None:
            client.download_media(message=msg, file=directory)

    time.sleep(3)
    n = n + 1
    print("Скачано ")
    time.sleep(2)
    if n == 1:
        break
