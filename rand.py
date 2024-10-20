# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: rand
# Author: Ijidishurka
# Commands:
# .kr
# ---------------------------------------------------------------------------------

import random

from telethon.tl.types import Message

from .. import loader


@loader.tds
class кругляш(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "кругляш"}

    async def krcmd(self, message: Message):
        """Кидает рандом видео сообщение из канала @kruglishik"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/kruglishik/{random.randint(6, 44)}">­</a>',
        )
