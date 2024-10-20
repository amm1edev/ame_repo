# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: ss
# Author: Ijidishurka
# Commands:
# .ss
# ---------------------------------------------------------------------------------

import random
from asyncio import sleep

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class ss(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "ss"}

    async def sscmd(self, message: Message):
        """Скидывает медиа по ссылке (работает там где отключено медиа)"""
        text = utils.get_args_raw(message)
        if not text:
            for ss in ["<b>Нету ссылки -_-</b>"]:
                await message.edit(ss)
                await sleep(0.5)
        else:
            await message.delete()
            await message.respond(
                f'<a href="{text}">­</a>',
            )
