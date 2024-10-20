# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: DelTimer
# Author: D4n13l3k00
# Commands:
# .deltm
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


import re
from asyncio import sleep

from .. import loader, utils  # type: ignore


@loader.tds
class DelTmMod(loader.Module):
    strings = {"name": "Delete Timer"}

    @loader.owner
    async def deltmcmd(self, m):
        "<реплай> <секунды>\nУдалить сообщение в реплае через указанное время"
        reply = await m.get_reply_message()
        if not reply:
            return await m.edit("reply...")
        r = re.compile(r"^\d+$")
        time = utils.get_args_raw(m)
        if r.match(time):
            await m.delete()
            await sleep(int(time))
            await reply.delete()
        else:
            await m.edit("shit...")
            return
