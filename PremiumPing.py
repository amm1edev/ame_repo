# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: PremiumPing
# Author: Ijidishurka
# Commands:
# .pinj
# ---------------------------------------------------------------------------------

import logging
import random
import time
from asyncio import sleep
from random import choice, randint

from telethon.tl.functions.channels import JoinChannelRequest

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(Premiumfake_ping())


class Premiumfake_ping(loader.Module):
    """Фейк пинг с премиум эмодзи"""

    strings = {"name": "Premium fake ping"}

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
                "<emoji document_id=6321050180095313397>⏱</emoji> <b>Скорость отклика"
                " Telegram:</b>"
                f" <code>{random.randint(10, 1999)}.{random.randint(10, 99)}</code>"
                " <b>ms</b>\n<emoji document_id=5377371691078916778>😎</emoji>"
                f" <b>Прошло с последней перезагрузки: {time_string}</b>"
            )
            return
        else:
            for pinj in ["<code>🐻 Nofin...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)

            named_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", named_tuple)

            pinj = (
                "<emoji document_id=6321050180095313397>⏱</emoji> <b>Скорость отклика"
                f" Telegram:</b> <code>{text}</code> <b>ms</b>\n<emoji"
                " document_id=5377371691078916778>😎</emoji> <b>Прошло с последней"
                f" перезагрузки: {time_string}</b>"
            )

            await message.edit(pinj)
