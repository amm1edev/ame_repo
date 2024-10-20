# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: HentaiManga
# Author: shadowhikka
# Commands:
# .manga
# ---------------------------------------------------------------------------------

# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyright 2023 t.me/shadow_modules
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# meta developer: @shadow_modules, @toxicuse
# meta banner: https://i.imgur.com/8UYznku.jpeg

import requests
from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall  # type: ignore


@loader.tds
class HentaiMangaMod(loader.Module):
    strings = {
        "name": "HentaiManga",
        "message": (
            "<b>Title:</b> <code>{title}</code>\n<b>Pages:</b> {total}\n<b>Tags:</b> {"
            " tags}"
        ),
        "time": "<b>Wait...</b>",
        "warnform": (
            "<b>⚠️ Attention!</b>\n<b>😰 This module is 18+\n✉️In many chats it is"
            " prohibited</b>\n<b>✅ If you agree with what you can getban - click on the"
            " button below</b>"
        ),
        "yes": "✅ Yes",
        "no": "❌ No",
    }
    strings_ru = {
        "message": (
            "<b>Название:</b> <code>{title}</code>\n<b>Страниц:</b>"
            " {total}\n<b>Теги:</b> {tags}"
        ),
        "time": "<b>Ожидайте...</b>",
        "warnform": (
            "<b>⚠️ Внимание!</b>\n<b>😰 Данный модуль 18+\n✉️Во многих чатах он"
            " запрещен</b>\n<b>✅ Если вы согласны с тем что можете получить бан -"
            " нажмите на кнопку ниже</b>"
        ),
        "yes": "✅ Да",
        "no": "❌ Нет",
    }

    async def manga(self):
        """Manga handler"""
        return (
            await utils.run_sync(
                requests.get, "https://janda.sinkaroid.org/3hentai/random"
            )
        ).json()["data"]

    async def mangacmd(self, message: Message):
        """Рандомная хентай-манга"""
        if not self.db.get(__name__, "warn", False):
            await self.inline.form(
                message=message,
                text=self.strings("warnform"),
                reply_markup=[
                    [
                        {
                            "text": self.strings("yes"),
                            "callback": self.inline__callAnswer,
                            "args": ("yes",),
                        },
                    ],
                    [
                        {
                            "text": self.strings("no"),
                            "callback": self.noren,
                            "args": (message,),
                        },
                    ],
                ],
            )
            return
        await utils.answer(message, self.strings("time"))
        mang = await self.manga()
        await self.inline.gallery(
            caption=self.strings("message").format(
                title=mang["title"].replace("[", "").replace("]", ""),
                total=mang["total"],
                tags=", ".join(mang["tags"]),
            ),
            message=message,
            next_handler=mang["image"],
        )

    async def inline__callAnswer(self, call: InlineCall, value: str):
        self.db.set(__name__, "warn", True)
        await call.delete()

    @loader.owner
    async def noren(self, call: InlineCall, message):
        await self.invoke("unloadmod", "HentaiManga", message.peer_id)
