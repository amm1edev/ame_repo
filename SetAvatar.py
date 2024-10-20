# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: SetAvatar
# Description: Fast avatar set by @skillzmeow
# Author: skillzmeow
# Commands:
# .ava
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 1)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @smeowcodes

from telethon.errors.rpcerrorlist import PhotoCropSizeSmallError
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.types import Message

from .. import loader, utils


class SetAvatarMod(loader.Module):
    """Fast avatar set by @skillzmeow"""

    strings = {"name": "SetAvatar"}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def avacmd(self, msg: Message):
        """use URL or reply to media"""
        args = utils.get_args_raw(msg)
        reply = await msg.get_reply_message()
        if reply and reply.media and not args:
            avatar = await self.client.upload_file(
                await self.client.download_file(reply.media, bytes)
            )
            await self.client(UploadProfilePhotoRequest(avatar))
            await utils.answer(msg, "<b>✅ Avatar successfully installed</b>")
        if not args and not reply:
            await utils.answer(
                msg, "😿 <b>No reference in the arguments or reply with media</b>"
            )
        if reply and not reply.media:
            await utils.answer(msg, "🤕 <b>Media not consists in reply</b>")
        if args:
            try:
                try:
                    photo = await self.client.send_file(
                        msg.sender.username,
                        args,
                        caption="<b>MODULE BY @skillzmeow</b>",
                    )
                    avatar = await self.client.upload_file(
                        await self.client.download_file(photo, bytes)
                    )
                    await self.client(UploadProfilePhotoRequest(avatar))
                    await utils.answer(msg, "<b>✅ Avatar successfully installed</b>")
                    await photo.delete()
                except PhotoCropSizeSmallError:
                    await utils.answer(msg, "📷 <b>Photo is too small!")
            except ValueError:
                await utils.answer(msg, "📛 <b>Invalid URL</b>")
