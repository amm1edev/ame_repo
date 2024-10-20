# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: allwithvoice
# Description: Перевод текста в гс и наоборот
# Author: Sad0ff
# Commands:
# .vw | .vm | .t
# ---------------------------------------------------------------------------------


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils


def register(cb):
    cb(allwithvoiceMod())


class allwithvoiceMod(loader.Module):
    """Перевод текста в гс и наоборот"""

    strings = {"name": "allwithvoice"}

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def vwcmd(self, event):
        """.vw <reply>\nчтобы все работало как я задумывал, смените голос (если хотите) на женский у @Maksobot\n@offsd подпишись-пожалеешь"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
            if not reply_message.text:
                return
        chat = "@Maksobot"
        await event.edit("<code>Извиняемся...</code>")
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=613929575)
                )
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply("<code>Разблокируй </code>@Maksobot")
                return
            if response.text:
                await event.edit("<code>Бот принял ислам, попробуйте снова</code>")
                return
            await event.delete()
            if reply_and_text:
                await event.client.send_message(
                    event.chat_id, response.message, reply_to=reply_message.id
                )
            else:
                await event.client.send_message(event.chat_id, response.message)

    async def vmcmd(self, event):
        """.vm <reply>"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        global reply_and_text
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                await event.edit(".vm")
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
        chat = "@aleksobot"
        await event.edit("<code>Извиняемся...</code>")
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=616484527)
                )
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply("<code>Разблокируй </code>@aleksobot")
                return
            await event.delete()
            if reply_and_text:
                await event.client.send_file(
                    event.chat_id, response.voice, reply_to=reply_message.id
                )
            else:
                await event.client.send_file(event.chat_id, response.voice)

    async def tcmd(self, message):
        """.t <reply on voice>\nчтобы оно работало, включите в боте тихий режим командой /silent"""
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("Ответь на голосовое сообщение")
            return
        try:
            voice = reply.voice
        except:
            await message.edit("Поддерживает только голосовые сообщения!!!")
            return
        chat = "@voicybot"
        await message.edit("<code>Извиняемся...</code>")
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=259276793)
                )
                await message.client.send_file(chat, voice)
                response = await response
            except YouBlockedUserError:
                await message.reply("<code>Разблокируй бота</code> @voicybot")
                return
            await message.delete()
            await message.client.send_message(message.to_id, response.text)
