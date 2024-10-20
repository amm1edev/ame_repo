# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: trysamp
# Author: shadowhikka
# Commands:
# .try
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
# meta banner: https://i.imgur.com/aGGx93G.jpeg

import random

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils


@loader.tds
class TrySampMod(loader.Module):
    strings = {"name": "TrySamp"}

    async def trycmd(self, message: Message):
        tryrandom = random.choice(["Удачно", "Не удачно", "Не удачно", "Удачно"])
        args = utils.get_args_raw(message)
        await utils.answer(
            message, f"<b>{tryrandom} | {args}</b>" if args else f"<b>{tryrandom}</b>"
        )
