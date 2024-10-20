# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: stickerdumper
# Description: Description for module
# Author: HitaloSama
# Commands:
# .getstkr
# ---------------------------------------------------------------------------------


from asyncio import sleep
from io import BytesIO

from .. import loader, utils


@loader.tds
class StickerDumperMod(loader.Module):
    """Description for module"""

    strings = {"name": "StickerDumper"}

    async def getstkrcmd(self, message):
        f = BytesIO()
        f.name = "sticker.jpg"
        reply = await message.get_reply_message()
        await reply.download_media(f)
        f.seek(0)
        await utils.answer(message, f)
