# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: k&ktext
# Description: K&K Text by @ktxtBot
# Author: Fl1yd
# Commands:
# .kkt
# ---------------------------------------------------------------------------------


from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils


def register(cb):
    cb(KKTextMod())


class KKTextMod(loader.Module):
    """K&K Text by @ktxtBot"""

    strings = {"name": "K&K Text"}

    async def kktcmd(self, message):
        """Используйте .kkt <текст или реплай>."""
        try:
            text = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            chat = "@ktxtBot"
            if not text and not reply:
                await message.edit("<b>Нет текста или реплая.</b>")
                return
            if text:
                await message.edit("<b>Минуточку...</b>")
                async with message.client.conversation(chat) as conv:
                    try:
                        response = conv.wait_event(
                            events.NewMessage(incoming=True, from_users=700914652)
                        )
                        await message.client.send_message(chat, text)
                        response = await response
                    except YouBlockedUserError:
                        await message.reply("<b>Разблокируй бота @ktxtBot.</b>")
                        return
                    if not response.text:
                        await message.edit(
                            "<Бот ответил не текстовым форматом, попробуйте ещё"
                            " раз.</b>"
                        )
                        return
                    await message.delete()
                    await message.client.send_message(message.to_id, response.text)
            if reply:
                await message.edit("<b>Минуточку...</b>")
                async with message.client.conversation(chat) as conv:
                    try:
                        response = conv.wait_event(
                            events.NewMessage(incoming=True, from_users=700914652)
                        )
                        await message.client.send_message(chat, reply)
                        response = await response
                    except YouBlockedUserError:
                        await message.reply("<b>Разблокируй бота @ktxtBot.</b>")
                        return
                    if not response.text:
                        await message.edit(
                            "<Бот ответил не текстовым форматом, попробуйте ещё"
                            " раз.</b>"
                        )
                        return
                    await message.delete()
                    await message.client.send_message(message.to_id, response.text)
        except TimeoutError:
            return await message.edit(
                "<b>Истекло время ожидания. Либо бот сдох, либо текст слишком большой,"
                " и бот не отвечает.</b>"
            )
