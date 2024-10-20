# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU GPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: YTsearch
# Description: Поиск видео на ютубе
# Author: KeyZenD
# Commands:
# .yt
# ---------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

#   Friendly Telegram (telegram userbot)
#   Copyright (C) 2018-2020 The Authors

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#   если не подписан на t.me/keyzend
#   твоя мама шлюха
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

from telethon.tl.types import DocumentAttributeFilename
from youtube_search import YoutubeSearch

from .. import loader, utils  # pylint: disable=relative-beyond-top-level

logger = logging.getLogger(__name__)


def register(cb):
    cb(YTsearchod())


@loader.tds
class YTsearchMod(loader.Module):
    """Поиск видео на ютубе"""

    strings = {"name": "YTsearch"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def ytcmd(self, message):
        """текст или реплай"""
        text = utils.get_args_raw(message)
        if not text:
            reply = await message.get_reply_message()
            if not reply:
                await message.delete()
                return
            text = reply.raw_text
        results = YoutubeSearch(text, max_results=10).to_dict()
        out = f"Найдено по запросу: {text}"
        for r in results:
            out += f'\n\n<a href="https://www.youtube.com/{r["link"]}">{r["title"]}</a>'
        await message.edit(out)
