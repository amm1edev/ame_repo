# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: UrlShot
# Author: vsecoder
# Commands:
# .shoturl | .adminshortinfo | .adminshortdel
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
# meta pic: https://img.icons8.com/bubbles/512/surgical-scissors.png

__version__ = (2, 0, 0)

import logging
import re

import requests

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class UrlShotMod(loader.Module):
    """
    Module for short url as API
    """

    strings = {
        "name": "UrlShotMod",
        "shorted": (
            "<b>✔️ Original:</b> {}\n<b>✂️ Shorted:</b> {}\n<b>⌨️ Admin secret:</b>"
            " <code>{}</code>"
        ),
        "usage_short": "<b>Usage:</b> .shoturl <link> or reply link",
        "shorting": "<b>✂️ Shorting...</b>",
        "usage_admin": "<b>Usage:</b> .adminshort <admin secret>",
        "gettings": "<b>🌘 Getting info...</b>",
        "deleting": "<b>🗑 Deleting...</b>",
        "info": (
            "<b>✔️ Original:</b> {}\n<b>✂️ Shorted:</b> {}\n<b>🔋 Is active:</b>"
            " {}\n<b>👥 Clicks:</b> {}"
        ),
        "usage_del": "<b>Usage:</b> .adminshortdel <admin secret>",
    }
    strings_ru = {
        "shorted": (
            "<b>✔️ Оригинал:</b> {}\n<b>✂️ Сокращённая:</b> {}\n<b>⌨️ Админ код:</b>"
            " <code>{}</code>"
        ),
        "usage_short": "<b>Команда:</b> .shoturl <ссылка> или в ответ на ссылку",
        "shorting": "<b>✂️ Сокращается...</b>",
        "usage_admin": "<b>Команда:</b> .adminshort <код админа>",
        "gettings": "<b>🌘 Получение информации...</b>",
        "deleting": "<b>🗑 Удаление...</b>",
        "info": (
            "<b>✔️ Оригинал:</b> {}\n<b>✂️ Сокращённая:</b> {}\n<b>🔋 Статус:</b>"
            " {}\n<b>👥 Переходы:</b> {}"
        ),
        "usage_del": "<b>Команда:</b> .adminshortdel <admin secret>",
    }

    async def client_ready(self, client, db):
        self._client = client

    async def shoturlcmd(self, message):
        """
        <url> or reply link - Add handler
        """
        args = utils.get_args_raw(message)
        url = None

        reply = await message.get_reply_message()
        if reply:
            regex = re.search("(?P<url>https?://[^\s]+)", reply.text)
            if regex:
                url = regex.group("url")

        if args:
            url = args

        if not url:
            await message.edit(self.strings["usage_short"])
            return

        await message.edit(self.strings["shorting"])

        try:
            body = {"target_url": url}
            r = requests.post("https://l.vsecoder.me/url", json=body)
            data = r.json()
            admin = data["admin_url"].replace("https://l.vsecoder.me/admin/", "")
            await message.edit(self.strings["shorted"].format(url, data["url"], admin))
        except Exception as e:
            await message.edit(f"<b>Error:</b> {e}")
            logger.error(e)

    async def adminshortinfocmd(self, message):
        """
        <admin secret> - get url shorted info
        """

        args = utils.get_args_raw(message)
        if not args:
            await message.edit(self.strings["usage_admin"])
            return

        await message.edit(self.strings["gettings"])

        try:
            r = requests.get(f"https://l.vsecoder.me/admin/{args}")
            data = r.json()
            await message.edit(
                self.strings["info"].format(
                    data["target_url"], data["url"], data["is_active"], data["clicks"]
                )
            )
        except Exception as e:
            await message.edit(f"<b>Error:</b> {e}")
            logger.error(e)

    async def adminshortdelcmd(self, message):
        """
        <admin secret> - delete url shorted
        """

        args = utils.get_args_raw(message)
        if not args:
            await message.edit(self.strings["usage_del"])
            return

        await message.edit(self.strings["deleting"])

        try:
            r = requests.delete(f"https://l.vsecoder.me/admin/{args}")
            data = r.json()
            await message.edit(f"<b>{data['detail']}</b>")
        except Exception as e:
            await message.edit(f"<b>Error:</b> {e}")
            logger.error(e)
