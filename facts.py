# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: facts
# Author: AmoreForever
# Commands:
# .afacts
# ---------------------------------------------------------------------------------

# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Facts.jpg
# channel @facti_p

import datetime
import random
from asyncio import sleep

from telethon import functions

from .. import loader, utils

chat = "@faktiru"


class FactsMod(loader.Module):
    """More Interesting Facts"""

    strings = {
        "name": "Facts",
        "wait": "<emoji document_id=5472146462362048818>💡</emoji> Searching...",
    }

    strings_ru = {"wait": "<emoji document_id=5472146462362048818>💡</emoji> Поиск..."}

    @loader.command(ru_docs="Интересные Факты")
    async def afactscmd(self, message):
        """Intersting Facts"""
        reply = await message.get_reply_message()
        await utils.answer(message, self.strings["wait"])
        result = await message.client(
            functions.messages.GetHistoryRequest(
                peer=chat,
                offset_id=0,
                offset_date=datetime.datetime.now(),
                add_offset=random.randint(0, 1000),
                limit=1,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )
        await sleep(0.30)
        await message.delete()
        await message.client.send_message(
            message.to_id,
            result.messages[0],
            reply_to=reply.id if reply else None,
        )
