# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Facts
# Author: kamolgks
# Commands:
# .ifacts
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
# *            © Copyright 2023
# *
# *         https://t.me/shitmodules
# *
# 🔒 Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0/

# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

# scope: hikka_only
# scope: hikka_min 1.6.2

# meta pic: https://raw.githubusercontent.com/kamolgks/assets/main/Facts.jpeg
# meta banner: https://raw.githubusercontent.com/kamolgks/assets/main/Facts.jpg

# meta developer: @shitmodules

import random
from asyncio import sleep

from hikkatl.types import Message  # type: ignore

from .. import loader, utils  # type: ignore

channel = "interesnie_fac"


@loader.tds
class Facts(loader.Module):
    """interesting facts by @shitmodules"""

    strings = {
        "name": "Facts",
        "wait": (
            "<emoji document_id=5472146462362048818>💡</emoji>"
            "<b>Looking for something interesting for you...</b>"
        ),
    }

    strings_ru = {
        "wait": (
            "<emoji document_id=5472146462362048818>💡</emoji>"
            "<b>Ищу для тебя что-то интересное...</b>"
        ),
    }

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.messages = await self.client.get_messages(channel, limit=None)

    @loader.command(ru_doc="> Поищу для тебя какую нибудь интересную информацию)")
    async def ifacts(self, message: Message):
        """
        > I'll look for some interesting information for you)
        """
        wtf = random.choice(self.messages)
        msg = await utils.answer(message, self.strings["wait"])
        await sleep(0.4)
        await msg.delete()
        await utils.answer(message, wtf)
