# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Try
# Author: D4n13l3k00
# Commands:
# .try
# ---------------------------------------------------------------------------------

# .------.------.------.------.------.------.------.------.------.------.
# |D.--. |4.--. |N.--. |1.--. |3.--. |L.--. |3.--. |K.--. |0.--. |0.--. |
# | :/\: | :/\: | :(): | :/\: | :(): | :/\: | :(): | :/\: | :/\: | :/\: |
# | (__) | :\/: | ()() | (__) | ()() | (__) | ()() | :\/: | :\/: | :\/: |
# | '--'D| '--'4| '--'N| '--'1| '--'3| '--'L| '--'3| '--'K| '--'0| '--'0|
# `------`------`------`------`------`------`------`------`------`------'
#
#                     Copyright 2023 t.me/D4n13l3k00
#           Licensed under the Creative Commons CC BY-NC-ND 4.0
#
#                    Full license text can be found at:
#       https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
#
#                           Human-friendly one:
#            https://creativecommons.org/licenses/by-nc-nd/4.0

# meta developer: @D4n13l3k00

import random

from .. import loader, utils  # type: ignore


@loader.tds
class TryMod(loader.Module):
    """Try"""

    strings = {"name": "Try"}

    @loader.owner
    async def trycmd(self, message):
        """.try действие"""
        do = utils.get_args_raw(message)
        rnd = random.choice(
            [
                "Удачно",
                "Удачно",
                "Неудачно",
                "Неудачно",
                "Удачно",
                "Неудачно",
                "Удачно",
                "Неудачно",
                "Удачно",
                "Неудачно",
            ]
        )
        await message.edit(f"<b>{do}</b>\n\n<code>{rnd}</code>")
