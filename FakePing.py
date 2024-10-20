# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: FakePing
# Author: Ijidishurka
# Commands:
# .pinj
# ---------------------------------------------------------------------------------

import logging
import random
import time
from asyncio import sleep
from random import choice, randint

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(fake_ping())


class fake_ping(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "fake ping v4"}

    async def pinjcmd(self, message):
        """Используй .pinj <цифры>."""
        text = utils.get_args_raw(message)
        if not text:
            for pinj in ["<code>🐻 Nofin...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)

            named_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", named_tuple)

            await message.edit(
                "<b>⏱ Скорость отклика"
                f" Telegram:</b>\n<code>{random.randint(10, 1999)}.{random.randint(10, 99)}</code>"
                f" <b>ms</b>\n<b>😎 Прошло с последней перезагрузки: {time_string}</b>"
            )
            return
        else:
            for pinj in ["<code>🐻 Nofin...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)

            named_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", named_tuple)

            pinj = (
                f"<b>⏱ Скорость отклика Telegram:</b>\n<code>{text}</code>"
                f" <b>ms</b>\n<b>😎 Прошло с последней перезагрузки: {time_string}</b>"
            )

            await message.edit(pinj)
