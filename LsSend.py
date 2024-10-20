# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: LsSend
# Description: Отправка смс в лс по юзеру пользователя.
# Author: trololo65
# Commands:
# .send
# ---------------------------------------------------------------------------------


# meta developer: @trololo_1

from .. import loader, utils


@loader.tds
class LsSendMod(loader.Module):
    """Отправка смс в лс по юзеру пользователя."""

    strings = {"name": "LsSend"}

    async def sendcmd(self, message):
        """.send {юзер} {текст или реплай}"""
        try:
            reply = await message.get_reply_message()
            text = utils.get_args_raw(message)

            id = str(text.split(" ")[0])
            check = []
            for i in text.split(" "):
                check.append(i)
            if len(check) <= 1:
                send = reply
            else:
                send = str(text.split(" ", maxsplit=1)[1])
            if send:
                await message.client.send_message(id, send)
                await message.edit("<b>Сообщение успешно отправлено!</b>")
            else:
                await message.edit("<b>Не было сделано реплая или нет текста.</b>")
        except:
            await message.edit(
                "<b>Неверный юзер, юзера нет вообще, либо ещё какая то ошибка.</b>"
            )
