# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: print
# Description: Аналог модуля typewriter
# Author: KeyZenD
# Commands:
# .print
# ---------------------------------------------------------------------------------


from asyncio import sleep

from .. import loader, utils


@loader.tds
class PrintMod(loader.Module):
    """Аналог модуля typewriter"""

    strings = {"name": "print"}

    @loader.owner
    async def printcmd(self, message):
        """.print <text or reply>"""
        text = utils.get_args_raw(message)
        if not text:
            reply = await message.get_reply_message()
            if not reply or not reply.message:
                await message.edit("<b>Текста нет!</b>")
                return
            text = reply.message
        out = ""
        for ch in text:
            out += ch
            if ch not in [" ", "\n"]:
                await message.edit(out + "\u2060")
                await sleep(0.3)
