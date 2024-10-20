# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: VulgarStories
# Author: shadowhikka
# Commands:
# .vstor
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

# meta developer: @shadow_modules
# meta banner: https://i.imgur.com/GqPSdtT.jpeg

import random

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils


@loader.tds
class VulgarStories(loader.Module):
    strings = {
        "name": "VulgarStories",
        "warning": (
            "⛔️ <b>I do not recommend using this module.</b>\n🍆 <b>In many chat rooms,"
            " all sorts of vulgar stories are prohibited.</b>"
        ),
    }
    strings_ru = {
        "warning": (
            "⛔️ <b>Не советую использовать этот модуль</b>\n🍆 <b>Во многих чатах"
            " запрещены всякие пошлые истории</b>"
        ),
    }

    async def client_ready(self):
        self.messages = await self.client.get_messages("pirsikowe", limit=100)
        if not self.get("warning_stories", False):
            await self.inline.bot.send_message(
                self._tg_id,
                text=self.strings("warning"),
            )
        self.set("warning_stories", True)

    async def vstorcmd(self, message: Message):
        """Vulgar Stories for geys."""
        persik = random.choice(self.messages)
        await utils.answer(message, persik)
