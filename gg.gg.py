# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU GPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: gg
# Description: Сокращение ссылок через сервис gg.gg
# Author: KeyZenD
# Commands:
# .gg
# ---------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

#   Friendly Telegram (telegram userbot)
#   Copyright (C) 2018-2020 @DneZyeK | sub to @KeyZenD

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

import telethon
from requests import post

from .. import loader, utils

logger = logging.getLogger(__name__)


async def register(cb):
    cb(WhoIsMod())


@loader.tds
class GGdotGGMod(loader.Module):
    """Сокращение ссылок через сервис gg.gg"""

    strings = {
        "name": "gg.gg",
        "some_rong": (
            "<b>Ты делаешь что-то не так!\nНапиши</b> <code>.help gg.gg</code> <b>для"
            " информации.</b>"
        ),
    }

    async def client_ready(self, client, db):
        self.client = client

    async def ggcmd(self, message):
        """.gg <длинная ссылка или реплай на ссылку>"""
        m_text = utils.get_args_raw(message)
        if not m_text:
            reply = await message.get_reply_message()
            if not reply:
                await utils.answer(message, self.strings["some_rong"])
                return
            long_url = reply.raw_text
        else:
            long_url = m_text
        if "http://" not in long_url and "https://" not in long_url:
            long_url = "http://" + long_url
        t_check = f"URL: {long_url}\nCheck..."
        await utils.answer(message, t_check)
        check = post(
            "http://gg.gg/check",
            data={
                "custom_path": None,
                "use_norefs": "0",
                "long_url": long_url,
                "app": "site",
                "version": "0.1",
            },
        ).text
        if check != "ok":
            await utils.answer(message, check)
            return
        await utils.answer(message, "Create...")
        short = post(
            "http://gg.gg/create",
            data={
                "custom_path": None,
                "use_norefs": "0",
                "long_url": long_url,
                "app": "site",
                "version": "0.1",
            },
        ).text
        await utils.answer(message, short)
