# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: RandomMemes
# Author: shadowhikka
# Commands:
# .randmemes
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

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils

# meta developer: @shadow_modules
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/nw5hP8P.jpeg


@loader.tds
class RandomMemesMod(loader.Module):
    strings = {"name": "RandomMemes"}
    memes_bot = "@ffmemesbot"

    async def on_dlmod(self):
        await utils.dnd(self._client, self.memes_bot, True)

    async def randmemescmd(self, message: Message):
        async with self._client.conversation(self.memes_bot) as conv:
            await conv.send_message("/start")
            phtmem = await conv.get_response()
            await conv.mark_read()
            await message.delete()
            await utils.answer(message, phtmem)
