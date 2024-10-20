# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: gsbl
# Description: Фановый, мемный модуль.
# Author: Fl1yd
# Commands:
# .gsbl
# ---------------------------------------------------------------------------------


import io
import os

from gsbl.stick_bug import StickBug
from PIL import Image

from .. import loader


def register(cb):
    cb(GSBLMod())


class GSBLMod(loader.Module):
    """Фановый, мемный модуль."""

    strings = {"name": "Get-Stick-Bugged-Lol"}

    async def gsblcmd(self, event):
        """Используй .gsbl <реплай на картинку/стикер>."""
        try:
            reply = await event.get_reply_message()
            if not reply:
                return await event.edit("Нет реплая на картинку/стикер.")
            await event.edit("Минуточку...")
            im = io.BytesIO()
            await event.edit("Скачиваю...")
            await event.client.download_file(reply, im)
            await event.edit("Обрабатываю...")
            im = Image.open(im)
            sb = StickBug(im)
            sb.save_video("get_stick_bugged_lol.mp4")
            await event.edit("Отправляю...")
            await event.client.send_file(
                event.to_id, open("get_stick_bugged_lol.mp4", "rb"), reply_to=reply
            )
            os.remove("get_stick_bugged_lol.mp4")
            await event.delete()
        except:
            return await event.edit("Это не картинка/стикер.")
