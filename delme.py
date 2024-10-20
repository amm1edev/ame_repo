# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: delme
# Description: Удаляет все сообщения
# Author: KeyZenD
# Commands:
# .delme | .delmenow
# ---------------------------------------------------------------------------------


from .. import loader, utils


class DelmeMod(loader.Module):
    """Удаляет все сообщения"""

    strings = {"name": "DelMe"}

    @loader.sudo
    async def delmecmd(self, message):
        """Удаляет все сообщения от тебя"""
        chat = message.chat
        if chat:
            args = utils.get_args_raw(message)
            if args != str(message.chat.id + message.sender_id):
                await message.edit(
                    "<b>Если ты точно хочешь это сделать, то напиши:</b>\n<code>.delme"
                    f" {message.chat.id+message.sender_id}</code>"
                )
                return
            await delete(chat, message, True)
        else:
            await message.edit("<b>В лс не чищу!</b>")

    @loader.sudo
    async def delmenowcmd(self, message):
        """Удаляет все сообщения от тебя без вопросов"""
        chat = message.chat
        if chat:
            await delete(chat, message, False)
        else:
            await message.edit("<b>В лс не чищу!</b>")


async def delete(chat, message, now):
    if now:
        all = (await message.client.get_messages(chat, from_user="me")).total
        await message.edit(f"<b>{all} сообщений будет удалено!</b>")
    else:
        await message.delete()
    _ = not now
    async for msg in message.client.iter_messages(chat, from_user="me"):
        if _:
            await msg.delete()
        else:
            _ = "_"
    (
        await message.delete()
        if now
        else "хули мусара хули мусара хули, едем так как ехали даже в хуй не дули"
    )
