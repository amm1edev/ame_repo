# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: urlshortener
# Description: Сократитель ссылок
# Author: Fl1yd
# Commands:
# .lgt
# ---------------------------------------------------------------------------------


import os

from .. import loader, utils


def register(cb):
    cb(URLShortenerMod())


class URLShortenerMod(loader.Module):
    """Сократитель ссылок"""

    strings = {"name": "URLShortener"}

    async def lgtcmd(self, message):
        """Сократить ссылку с помощью сервиса verylegit.link"""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit("Нет аргументов.")
        link = os.popen(f"curl verylegit.link/sketchify -d long_url={args}").read()
        await message.edit(f"Ссылка:\n> {link}")
