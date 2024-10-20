# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: crename
# Author: thomasmod
# Commands:
# .rename
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 0)

#            ▀█▀  █ █ █▀█  █▀▄▀█  ▄▀█ █▀
#             █  █▀█ █▄█ █ ▀  █ █▀█ ▄█
#            https://t.me/netuzb
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://te.legra.ph/file/a2c350d63b964fa70903c.png
# meta banner: https://te.legra.ph/file/9adde024646b7662f12fe.jpg
# meta developer: @wilsonmods
# scope: hikka_only
# scope: hikka_min 1.3.2

import asyncio
import logging

from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils

wilson_fire = "🔥 "
wilson_warn = "🚨 "
wilson_wait = "🕒 "
wilson_done = "✅ "


class ReanemerMod(loader.Module):
    """Rename file name"""

    strings = {
        "name": "✍️ Fast-Rename",
        "wilson_no_reply": wilson_warn + "<b>Reply to file?</b>",
        "wilson_no_name": wilson_fire + "<b>What's the name?</b>",
        "wilson_wait": wilson_wait + "<b>Please, wait...</b>",
        "wilson_load": wilson_fire + "<b>Loading »»</b>",
        "wilson_down": wilson_fire + "<b>Downloading »»</b>",
        "wilson_done": wilson_done + "<b>Done</b>",
    }

    strings_ru = {
        "wilson_no_reply": wilson_warn + "<b>А ответ на файл?</b>",
        "wilson_no_name": wilson_fire + "<b>Как назвать?</b>",
        "wilson_wait": wilson_wait + "<b>Пожалуйста, подождите...</b>",
        "wilson_load": wilson_fire + "<b>Загрузка »»</b>",
        "wilson_down": wilson_fire + "<b>Скачивание »»</b>",
        "wilson_done": wilson_done + "<b>Готов</b>",
    }

    strings_uz = {
        "wilson_no_reply": wilson_warn + "<b>Faylga javob tariqasida?</b>",
        "wilson_no_name": wilson_fire + "<b>Qanday nom?</b>",
        "wilson_wait": wilson_wait + "<b>Iltimos, kuting...</b>",
        "wilson_load": wilson_fire + "<b>Yuborilmoqda »»</b>",
        "wilson_down": wilson_fire + "<b>Yuklanmoqda »»</b>",
        "wilson_done": wilson_done + "<b>Tayyor</b>",
    }

    async def renamecmd(self, message):
        """> rename [name.format]"""

        await message.edit(f"{self.strings('wilson_wait')}")
        reply = await message.get_reply_message()
        if not reply or not reply.file:
            await message.edit(self.strings["wilson_no_reply"])
            return
        name = utils.get_args_raw(message)
        if not name:
            await message.edit(self.strings["wilson_no_name"])
            return
        fn = reply.file.name
        if not fn:
            fn = ""
        fs = reply.file.size

        [
            (
                await message.edit(f"<b>{self.strings('wilson_down')} {fn}</b>")
                if fs > 500000
                else ...
            )
        ]
        file = await reply.download_media(bytes)
        [
            (
                await message.edit(
                    f"<b>{self.strings('wilson_load')}</b> <code>{name}</code>"
                )
                if fs > 500000
                else ...
            )
        ]
        await message.client.send_file(
            message.to_id,
            file,
            force_document=True,
            reply_to=reply,
            attributes=[DocumentAttributeFilename(file_name=name)],
            caption=f"{self.strings('wilson_done')} | <code>{name}</code>",
        )
        await message.delete()
