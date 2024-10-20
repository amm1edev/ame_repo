# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Ava
# Author: D4n13l3k00
# Commands:
# .ava | .delava | .delavas
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


import os

from telethon import functions, types

from .. import loader, utils  # type: ignore


@loader.tds
class AvaMod(loader.Module):
    """Установка/удаление аватарок через команды"""

    strings = {
        "name": "AvatarMod",
        "need_pic": "<b>[Avatar]</b> Нужно фото",
        "downloading": "<b>[Avatar]</b> Скачиваю",
        "installing": "<b>[Avatar]</b> Устанавливаю",
        "deleting": "<b>[Avatar]</b> Удаляю",
        "ok": "<b>[Avatar]</b> Готово",
        "no_avatar": "<b>[Avatar]</b> Нету аватарки/ок",
    }

    async def avacmd(self, m: types.Message):
        ".ava <reply_to_photo> - Установить аватар"
        client = m.client
        reply = await m.get_reply_message()
        if not reply and not reply.photo:
            return await utils.answer(m, self.strings("need_pic"))

        m = await utils.answer(m, self.strings("downloading"))
        photo = await client.download_media(message=reply.photo)
        up = await client.upload_file(photo)
        m = await utils.answer(m, self.strings("installing"))
        await client(functions.photos.UploadProfilePhotoRequest(up))
        await utils.answer(m, self.strings("ok"))
        os.remove(photo)

    async def delavacmd(self, m: types.Message):
        "Удалить текущую аватарку"
        client = m.client
        ava = await client.get_profile_photos("me", limit=1)
        if len(ava) > 0:
            m = await utils.answer(m, self.strings("deleting"))
            await client(functions.photos.DeletePhotosRequest(ava))
            await utils.answer(m, self.strings("ok"))
        else:
            await utils.answer(m, self.strings("no_avatar"))

    async def delavascmd(self, m: types.Message):
        "Удалить все аватарки"
        client = m.client
        ava = await client.get_profile_photos("me")
        if len(ava) > 0:
            m = await utils.answer(m, self.strings("deleting"))
            await client(
                functions.photos.DeletePhotosRequest(
                    await m.client.get_profile_photos("me")
                )
            )
            await utils.answer(m, self.strings("ok"))
        else:
            await utils.answer(m, self.strings("no_avatar"))
