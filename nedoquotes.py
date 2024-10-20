# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: nedoquotes
# Description: Генератор всратых цитат by @ShittyQuoteBot
# Author: Fl1yd
# Commands:
# .nq
# ---------------------------------------------------------------------------------


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils


def register(cb):
    cb(NedoQuotesMod())


class NedoQuotesMod(loader.Module):
    """Генератор всратых цитат by @ShittyQuoteBot"""

    strings = {"name": "NedoQuotes"}

    async def nqcmd(self, message):
        """Используй: .nq <текст или реплай>."""
        chat = "@ShittyQuoteBot"
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая.</b>")
            return
        await message.edit("<b>Минуточку...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(
                        events.NewMessage(incoming=True, from_users=1389323591)
                    )
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @ShittyQuoteBot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(
                        events.NewMessage(incoming=True, from_users=1389323591)
                    )
                    await message.client.send_message(
                        chat, f"{reply.raw_text} (с) {user.first_name}"
                    )
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @ShittyQuoteBot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<b> {response.text}</b>")
            await message.delete()
        if response.media:
            await message.client.send_file(
                message.to_id, response.media, reply_to=reply.id if reply else None
            )
            await message.delete()
