# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AnonymUploader
# Author: kamolgks
# Commands:
# .aupl
# ---------------------------------------------------------------------------------

__version__ = (0, 0, 1)
# *
# *              $$\       $$\   $$\                                   $$\           $$\
# *              $$ |      \__|  $$ |                                  $$ |          $$ |
# *     $$$$$$$\ $$$$$$$\  $$\ $$$$$$\   $$$$$$\$$$$\   $$$$$$\   $$$$$$$ |$$\   $$\ $$ | $$$$$$\   $$$$$$$\
# *    $$  _____|$$  __$$\ $$ |\_$$  _|  $$  _$$  _$$\ $$  __$$\ $$  __$$ |$$ |  $$ |$$ |$$  __$$\ $$  _____|
# *    \$$$$$$\  $$ |  $$ |$$ |  $$ |    $$ / $$ / $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |\$$$$$$\
# *     \____$$\ $$ |  $$ |$$ |  $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$   ____| \____$$\
# *    $$$$$$$  |$$ |  $$ |$$ |  \$$$$  |$$ | $$ | $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |
# *    \_______/ \__|  \__|\__|   \____/ \__| \__| \__| \______/  \_______| \______/ \__| \_______|\_______/
# *
# *
# *            © Copyright 2022/2023
# *
# *         https://t.me/shitmodules
# *
# 🔒 Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0/

# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

# scope: hikka_only
# scope: hikka_min 1.6.2

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/AnonUploader.jpg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/AnonymUploader.jpg

# meta developer: @shitmodules

import io
import logging
import random
import re

import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AnonymUploader(loader.Module):
    """Anonymous files upload via anonfiles.com"""

    strings = {
        "name": "AnonymUploader",
        "uploading": "🚀 <b>Uploading...</b>",
        "noargs": "🚫 <b>No file specified</b>",
        "bot_blocked": "🚫 <b>Unban @anonfiles_com_bot</b>",
    }

    strings_ru = {
        "uploading": "🚀 <b>Загрузка...</b>",
        "noargs": "🚫 <b>Файл не указан</b>",
        "bot_blocked": "🚫 <b>Разблокируй @anonfiles_com_bot</b>",
    }

    async def get_media(self, message: Message):
        reply = await message.get_reply_message()
        m = None
        if reply and reply.media:
            m = reply
        elif message.media:
            m = message
        elif not reply:
            await utils.answer(message, self.strings("noargs"))
            return False

        if not m:
            file = io.BytesIO(bytes(reply.raw_text, "utf-8"))
            file.name = "file.txt"
        else:
            file = io.BytesIO(await self._client.download_media(m, bytes))
            file.name = (
                m.file.name
                or (
                    "".join(
                        [
                            random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
                            for _ in range(16)
                        ]
                    )
                )
                + m.file.ext
            )

        return file

    @loader.command()
    async def auplcmd(self, message: Message):
        """> <reply to file> - Anonymous file Uploader"""
        chat = "@anonfiles_com_bot"
        message = await utils.answer(message, self.strings("uploading"))
        file = await self.get_media(message)

        async with self._client.conversation(chat) as conv:
            try:
                m = await conv.send_message(file=file)
                response = await conv.get_response()
            except YouBlockedUserError:
                await utils.answer(message, self.strings("bot_blocked"))
                return

            await m.delete()
            await response.delete()

            await self.client.delete_dialog(chat)

            try:
                url = (
                    re.search(
                        r'<meta property="og:image" data-react-helmet="true"',
                        r' content="(.*?)"',
                        (await utils.run_sync(requests.get, response.raw_text)).text,
                    )
                    .group(1)
                    .split("?")[0]
                )
            except Exception:
                url = response.raw_text

        await utils.answer(message, f"<b>🪄Your file uploaded: <code>{url}</code></b>")
