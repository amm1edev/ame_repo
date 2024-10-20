# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: report
# Description: Репорт
# Author: Fl1yd
# Commands:
# .report
# ---------------------------------------------------------------------------------


from telethon import functions

from .. import loader, utils


def register(cb):
    cb(ReportMod())


class ReportMod(loader.Module):
    """Репорт"""

    strings = {"name": "Report"}

    async def reportcmd(self, message):
        """Репорт пользователя за спам."""
        reply = await message.get_reply_message()
        if reply:
            await message.client(
                functions.messages.ReportSpamRequest(peer=reply.sender.id)
            )
            await message.edit("<b>Ты получил репорт за спам!</b>")
        else:
            return await message.edit("<b>Кого я должен зарепортить?</b>")
