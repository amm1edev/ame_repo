# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: voicy
# Author: Ijidishurka
# Commands:
# .v
# ---------------------------------------------------------------------------------

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils


def register(cb):
    cb(voiceActing())


class voiceActing(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "voiceActing"}

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def vcmd(self, event):
        """.v <text> Вы можете сменить голос в боте @BigVoicyBot"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        global reply_and_text
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                await event.edit(".v")
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
        chat = "@BigVoicyBot"
        await event.edit("<code>Асуждаю...</code>")
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=656917446)
                )
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply("<code>Разблокируй </code>@AlpacaVoiceBot")
                return
            await event.delete()
            if reply_and_text:
                await event.client.send_file(
                    event.chat_id, response.voice, reply_to=reply_message.id
                )
            else:
                await event.client.send_file(event.chat_id, response.voice)
