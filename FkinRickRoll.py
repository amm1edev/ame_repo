# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: FkinRickRoll
# Author: dorotorothequickend
# Commands:
# .rickvid | .rickbait
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
# 						Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroFkinRickRoll.png
# meta developer: @DorotoroMods

from telethon.tl.functions.account import UpdateProfileRequest

from .. import loader, utils


@loader.tds
class FuckingRickRoll(loader.Module):
    """Лучший способ зарикроллить собеседника."""

    strings = {"name": "FkinRickRoll"}

    @loader.command()
    async def rickvid(self, message):
        "- стандартный RickRoll."
        if message.out:
            await message.delete()
        photo = await self._client.send_file(
            message.to_id,
            "https://siasky.net/AAAszL8plrdwyskshNBDBNBQx7IeQGVajIVq305Xd7w4vg",
            caption="<b><i>You've been Rickrolled!</i></b>",
        )
        upload = await self._client.upload_file(
            await self._client.download_file(photo, bytes)
        )
        await self._client(UploadProfilePhotoRequest(upload))

    @loader.command()
    async def rickbait(self, message):
        "- отправляет видео с океаном, в конце которого вашего собеседника ждет RickRoll."
        if message.out:
            await message.delete()
        photo = await self._client.send_file(
            message.to_id,
            "https://siasky.net/_Al0XoSpEfN-aZlzdzQX2jc92xCKjlVHAC1uvcvDrRg7fw",
        )
        upload = await self._client.upload_file(
            await self._client.download_file(photo, bytes)
        )
        await self._client(UploadProfilePhotoRequest(upload))
