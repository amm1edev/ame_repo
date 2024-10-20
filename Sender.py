# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Sender
# Description: No description
# Author: SekaiYoneya
# Commands:
# .snd
# ---------------------------------------------------------------------------------


# @Sekai_Yoneya

import re

from telethon.errors import ChannelInvalidError

from .. import loader, utils


@loader.tds
class SenderMod(loader.Module):
    strings = {"name": "Sender"}

    @loader.owner
    async def sndcmd(self, m):
        """.snd <канал/чат/id> <reply>
        Отправить сообщение в чат/канал(без авторства)
        """
        args = utils.get_args_raw(m)
        reply = await m.get_reply_message()
        if not args:
            return await m.edit("[Sender] Укажите канал/чат")
        try:
            this = await m.client.get_input_entity(
                int(args) if re.match(r"-{0,1}\d+", args) else args
            )
        except ChannelInvalidError as e:
            return await m.edit("[Sender] Такого канала/чата не существует!")
        except Exception as e:
            return await m.edit("[Sender] Неизвестная мне ошибка:\n" + " ".join(e.args))
        ok = await m.client.send_message(this, reply)
        await m.edit("[Sender] Сообщение отправлено!")
