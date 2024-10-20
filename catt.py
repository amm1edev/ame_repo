# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: catt
# Author: Ijidishurka
# Commands:
# .catt
# ---------------------------------------------------------------------------------

import random

from telethon.tl.types import Message

from .. import loader


@loader.tds
class catt(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "catt"}

    async def cattcmd(self, message: Message):
        """Скидывает видео с котиком (работает в чатах где отключено медиa)"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/radiofmonline/{random.randint(282, 283)}">­</a>',
        )
