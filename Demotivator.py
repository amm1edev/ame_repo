# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Demotivator
# Author: D4n13l3k00
# Commands:
# .dmt
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


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils  # type: ignore


@loader.tds
class dmt228Mod(loader.Module):
    """Демотиватор 228 @super_rjaka_demotivator_bot"""

    strings = {"name": "Демотиватор 228"}

    @loader.owner
    async def dmtcmd(self, message):
        """.dmt [текст по желанию] <reply to video, photo or gif>"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            return await message.edit("<b>Reply to media</b>")
        try:
            media = reply.media
        except Exception:
            return await message.edit("<b>Only media</b>")
        chat = "@super_rjaka_demotivator_bot"
        await message.edit("<b>Демотивируем...</b>")
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1016409811)
                )
                mm = await message.client.send_file(chat, media, caption=args)
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                return await message.reply(
                    "<b>Разблокируй @super_rjaka_demotivator_bot</b>"
                )
            await message.delete()
            await response.delete()
            await message.client.send_file(
                message.to_id,
                response.media,
                reply_to=await message.get_reply_message(),
            )
