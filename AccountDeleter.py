# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AccountDeleter
# Author: dorotorothequickend
# Commands:
# .delacc
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroAccountDeleter.png
# meta developer: @DorotoroMods

import asyncio
import os

from telethon import functions
from telethon.tl.functions.account import UpdateProfileRequest

from .. import loader, utils


@loader.tds
class AccountDeleter(loader.Module):
    strings = {"name": "AccountDeleter"}

    @loader.command()
    async def delacc(self, m):
        "- удаляет ваш аккаунт (просто меняет вашу аватарку и ник)."
        text = "Удаление аккаунта через..."
        await utils.answer(
            m, f"{text} <b>10</b> <emoji document_id=5296432770392791386>✈️</emoji>"
        )
        asyncio.sleep(0.5)
        await utils.answer(
            m, f"{text} <b>6</b> <emoji document_id=5296432770392791386>✈️</emoji>"
        )
        asyncio.sleep(0.7)
        await utils.answer(
            m, f"{text} <b>3</b> <emoji document_id=5296432770392791386>✈️</emoji>"
        )
        asyncio.sleep(1)
        await utils.answer(
            m, f"{text} <b>1</b> <emoji document_id=5296432770392791386>✈️</emoji>"
        )
        asyncio.sleep(0.8)
        photo = "https://0x0.st/oJqh.jpg"
        photo_ = await self.client.send_file("me", photo)
        avatar = await self.client.upload_file(
            await self.client.download_file(photo_, bytes)
        )
        await self.client(functions.photos.UploadProfilePhotoRequest(avatar))
        await photo_.delete()
        await self._client(
            functions.account.UpdateProfileRequest(
                first_name="Deleted Account",
                last_name="",
                about="Аккаунт удалён. Вся информация на https://telegram.org/faq",
            )
        )
        await utils.answer(
            m,
            (
                "<b>Ваш аккаунт полностью удалён. <emoji"
                " document_id=6325592348529003273>😦</emoji></b>"
            ),
        )
