# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: ascii
# Author: vsecoder
# Commands:
# .ascii
# ---------------------------------------------------------------------------------

"""
                                _             
  __   _____  ___  ___ ___   __| | ___ _ __   
  \ \ / / __|/ _ \/ __/ _ \ / _` |/ _ \ '__|  
   \ V /\__ \  __/ (_| (_) | (_| |  __/ |     
    \_/ |___/\___|\___\___/ \__,_|\___|_|     

    Copyleft 2022 t.me/vsecoder                                                            
    This program is free software; you can redistribute it and/or modify 

"""
# meta developer: @vsecoder_m
# meta pic: https://img.icons8.com/color/344/asc.png
# requires: Pillow
# meta banner: https://chojuu.vercel.app/api/banner?img=https://img.icons8.com/color/344/asc.png&title=AsciiMod&description=Module%20for%20convert%20image%20to%20ascii

__version__ = (0, 0, 1)

import logging

import imgkit
from image2ascii.core import Image2ASCII
from PIL import Image

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AsciiMod(loader.Module):
    """Module for convert image to ascii"""

    strings = {
        "name": "AsciiMod",
        "loading_image": "⏳ Downloading image...",
        "converting_image": "⏳ Converting image...",
        "save_image": "⏳ Saving image...",
        "os_error": (
            "❗️ Install 'wkhtmltopdf'\n\n.terminal sudo apt install wkhtmltopdf"
        ),
        "type_error": "❗️ Unknown image format!",
        "another_error": "❗️ Unknown error, please check logs!\n\n{}",
        "complete": "🖍 Look:",
    }

    strings_ru = {
        "loading_image": "⏳ Скачивается изображение...",
        "converting_image": "⏳ Конвертируется изображение...",
        "save_image": "⏳ Сохраняется изображение...",
        "os_error": (
            "❗️ Установите 'wkhtmltopdf'\n\n.terminal sudo apt install wkhtmltopdf"
        ),
        "type_error": "❗️ Неизвестный формат изображения!",
        "another_error": "❗️ Неизвестная ошибка, пожайлуйста проверьте логи!\n\n{}",
        "complete": "🖍 Смотри:",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "background",
                "black",
                lambda m: "Background",
            ),
            loader.ConfigValue(
                "color",
                "white",
                lambda m: "Color",
            ),
        )
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    @loader.unrestricted
    @loader.ratelimit
    async def asciicmd(self, message):
        """
        <reply_to_image> - convert image to ascii
        """
        try:
            reply = await message.get_reply_message()

            await utils.answer(message, self.strings("loading_image"))
            f = await self._client.download_media(message=reply, file="test.png")
            await utils.answer(message, self.strings("converting_image"))
            r = Image2ASCII("test.png").render()

            background = self.config["background"]
            color = self.config["color"]

            im = Image.open("test.png")
            width, height = im.size

            options = {"crop-w": width, "crop-h": height, "encoding": "UTF-8"}

            ascii = "".join(
                str(line).replace(" ", "&nbsp;") + "<br>" for line in str(r).split("\n")
            )

            await utils.answer(message, self.strings("save_image"))

            with open("test.html", "w") as f:
                f.write(
                    f'<html style="background: {background}; color:'
                    f' {color}"><code>{ascii}</code></html>'
                )

            try:
                imgkit.from_file("test.html", "out.jpg", options=options)

                await self._client.send_file(
                    utils.get_chat_id(message),
                    open("out.jpg", "rb"),
                )
                await utils.answer(message, self.strings("complete"))
            except OSError:
                await utils.answer(message, self.strings("os_error"))
        except TypeError:
            await utils.answer(message, self.strings("type_error"))
        except Exception as e:
            await utils.answer(message, self.strings("another_error").format(e))
