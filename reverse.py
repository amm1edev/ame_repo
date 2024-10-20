# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: reverse
# Description: Реверс текста.
# Author: Fl1yd
# Commands:
# .rev
# ---------------------------------------------------------------------------------


from telethon.errors import MessageEmptyError

from .. import loader, utils


def register(cb):
    cb(ReverseMod())


class ReverseMod(loader.Module):
    """Реверс текста."""

    strings = {"name": "Reverse"}

    async def revcmd(self, message):
        """Используй .rev <текст или реплай>."""
        try:
            text = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            if not text and not reply:
                return await message.edit("Нет текста или реплая.")
            if reply:
                return await message.edit(f"{reply.raw_text}"[::-1])
            if text:
                return await message.edit(f"{text}"[::-1])
        except MessageEmptyError:
            return await message.edit("Это не текст.")
