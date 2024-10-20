# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: catchargs
# Description: Случайный картинка по аргументам из @pic.
# Author: Fl1yd
# Commands:
# .pic
# ---------------------------------------------------------------------------------


from random import choice as какаша

from .. import loader, utils


def register(cb):
    cb(PicMod())


class PicMod(loader.Module):
    """Случайный картинка по аргументам из @pic."""

    strings = {"name": "Pic"}

    async def piccmd(self, event):
        try:
            args = utils.get_args_raw(event)
            if not args:
                await event.edit("<b>Нет аргумента после команды.</b>")
                return
            await event.edit(f"<b>Лови {args}!</b>")
            reslt = await event.client.inline_query("pic", args)
            await reslt[reslt.index(какаша(reslt))].click(event.to_id)
        except Exception as e:
            await event.edit(str(e))
            return
