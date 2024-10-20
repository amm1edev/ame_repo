# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Cat
# Author: Ijidishurka
# Commands:
# .cat
# ---------------------------------------------------------------------------------

# meta developer: @modwini
import io

import requests
from PIL import Image

from .. import loader


@loader.tds
class CatModule(loader.Module):
    """Отправляет случайное фото котика."""

    strings = {"name": "Cat"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def catcmd(self, message):
        """Отправляет случайное фото котика."""
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)
        if response.status_code == 200:
            img_url = response.json()[0]["url"]
            response = requests.get(img_url)
            img = Image.open(io.BytesIO(response.content))

            if img.mode == "P":
                img = img.convert("RGB")
            output = io.BytesIO()
            img.save(output, format="JPEG")
            output.seek(0)
            await self.client.send_file(message.to_id, output, reply_to=message)
