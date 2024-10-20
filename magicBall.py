# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: magicBall
# Author: Ijidishurka
# Commands:
# .ball
# ---------------------------------------------------------------------------------

import logging
import random
from random import choice, randint

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(magic_ball())


class magic_ball(loader.Module):
    """Волшебный шар by @modwini"""

    strings = {"name": "Magic Ball"}

    async def ballcmd(self, message):
        """Используй ball <вопрос>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit("<b>Нет вопроса после команды 0_0 </b>")
            return
        else:
            list = ["да", "нет"]
            list2 = ["Я думаю", "Наверное", "Скорее всего", "Точно"]
            ball = (
                f"🗣️<code>{text}</code>\n"
                + f"<b>🔮{random.choice(list2)} {random.choice(list)}</b>"
            )

            await message.edit(ball)
