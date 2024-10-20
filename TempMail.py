# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: TempMail
# Description: Временная почта by @blazeftg
# Author: blazedzn
# Commands:
# .getmail | .lookmail | .readmail
# ---------------------------------------------------------------------------------


import asyncio

import requests

from .. import loader, utils


@loader.tds
class TempMailMod(loader.Module):
    """Временная почта by @blazeftg"""

    strings = {"name": "TempMail"}

    async def getmailcmd(self, message):
        """.getmail
        Получить адрес временной почты
        """
        response = requests.get(
            "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
        )
        await message.edit(
            "Ваш адрес электронной почты: " + f"<code>{str(response.json()[0])}</code>"
        )

    async def lookmailcmd(self, message):
        """.lookmail <адрес эл. почты>
        Получить все сообщения на почте
        """
        user_i = utils.get_args_raw(message)
        output_mess = ""
        filtered = user_i.split("@")
        name = filtered[0]
        domain = ""
        try:
            domain = filtered[1]
        except IndexError:
            output_mess = "Введи адрес почты, ебалай"
        response = requests.get(
            "https://www.1secmail.com/api/v1/?action=getMessages&login={name}&domain={domain}"
            .format(name=name, domain=domain)
        )
        if response.json() == []:
            output_mess = "На почте нету писем или же ты не правильно ввёл её адрес"
        else:
            for i in range(len(response.json())):
                output_mess += (
                    "Письмо №"
                    + f"<code>{str(i+1)}</code>"
                    + "\nСообщение от: "
                    + f"<code>{str(response.json()[i]['from'])}</code>"
                    + "\nТема: "
                    + f"<code>{str(response.json()[i]['subject'])}</code>"
                    + "\nДата получения: "
                    + f"<code>{str(response.json()[i]['date'])}</code>"
                    + "\nID письма: "
                    + f"<code>{str(response.json()[i]['id'])}</code>"
                    + "\n\n"
                )
        await message.edit(output_mess)

    async def readmailcmd(self, message):
        """.readmail <адрес эл. почты> <ID сообщения>
        Прочитать сообщение на почте с конкретным ID
        """
        user_i = utils.get_args_raw(message)
        filtered = user_i.split()
        try:
            email = filtered[0]
            id = filtered[1]
            filtered_email = email.split("@")
            name = filtered_email[0]
            domain = filtered_email[1]
            response = requests.get(
                "https://www.1secmail.com/api/v1/?action=readMessage&login={name}&domain={domain}&id={message_id}"
                .format(name=name, domain=domain, message_id=id)
            )
            await message.edit(
                "Дата получения: "
                + f"<code>{str(response.json()['date'])}</code>"
                + "\nОт: "
                + f"<code>{str(response.json()['from'])}</code>"
                + "\nТема: "
                + f"<code>{str(response.json()['subject'])}</code>"
                + "\nТекст письма: "
                + str(response.json()["textBody"])
            )
        except:
            await message.edit("Неправильный адрес почты или ID сообщения")
