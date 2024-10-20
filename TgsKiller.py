# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: TgsKiller
# Description: Хуярит
# Author: KeyZenD
# Commands:
# .tgs
# ---------------------------------------------------------------------------------


import logging
import os
from random import choice, randint

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class TgsKillerMod(loader.Module):
    """Хуярит"""

    strings = {"name": "TgsKiller"}

    @loader.unrestricted
    async def tgscmd(self, message):
        """хуярит стикеры"""
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("Реплай на стикер анимированный")
            return
        if not reply.file:
            await message.edit("Реплай на стикер анимированный")
            return
        if not reply.file.name.endswith(".tgs"):
            await message.edit("Реплай на стикер анимированный")
            return
        await message.edit("///Пахуярили нахуй!///")
        await reply.download_media("tgs.tgs")
        os.system("lottie_convert.py tgs.tgs json.json")
        with open("json.json", "r") as f:
            stick = f.read()
            f.close()

        for i in range(1, randint(6, 10)):
            stick = choice(
                [
                    stick.replace(f"[{i}]", f"[{(i+i)*3}]"),
                    stick.replace(f".{i}", f".{i}{i}"),
                ]
            )

        with open("json.json", "w") as f:
            f.write(stick)
            f.close()

        os.system("lottie_convert.py json.json tgs.tgs")
        await reply.reply(file="tgs.tgs")
        os.remove("tgs.tgs")
        os.remove("json.json")
        await message.delete()
