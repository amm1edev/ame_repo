# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: заёбушка
# Description: Заебет любого
# Author: KeyZenD
# Commands:
# .заебу
# ---------------------------------------------------------------------------------


from asyncio import sleep

from .. import loader, utils


def register(cb):
    cb(ЗаёбушкаMod())


class ЗаёбушкаMod(loader.Module):
    """Заебет любого"""

    strings = {"name": "Заёбушка"}

    async def заебуcmd(self, message):
        """.заебу <колличество> <реплай на того, кого заебать>"""
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>А кого заёбывать-то?</b>")
            return
        id = reply.sender_id
        args = utils.get_args(message)
        count = 50
        if args:
            if args[0].isdigit():
                if int(args[0]) < 0:
                    count = 50
                else:
                    count = int(args[0])
        txt = '<a href="tg://user?id={}">Заёбушка :3</a>'.format(id)
        await message.delete()
        for _ in range(count):
            await sleep(0.3)
            msg = await message.client.send_message(message.to_id, txt)
            await sleep(0.3)
            await msg.delete()
