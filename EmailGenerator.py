# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: EmailGenerator
# Description: Email Generator by @blazeftg
# Author: blazedzn
# Commands:
# .fakemail
# ---------------------------------------------------------------------------------


import asyncio
import random
import string

import requests

from .. import loader, utils


@loader.tds
class EmailGeneratorMod(loader.Module):
    """Email Generator by @blazeftg"""

    strings = {"name": "EmailGenerator"}

    async def fakemailcmd(self, message):
        """.fakemail <опционально, имя почтового ящика>
        Генерирует почтовый ящик с твоим именем, если оно указано
        """
        await message.edit(f"<b>Создаю почту...</b>")
        response = requests.get("https://api.namefake.com/")
        name = utils.get_args_raw(message)
        if name == "":
            n = random.randint(5, 10)
            letters = string.ascii_lowercase
            name = "".join(random.choice(letters) for i in range(n))
        else:
            pass
        email_link = "https://emailfake.com/{domain}/{name}".format(
            domain=str(response.json()["email_d"]), name=name
        )
        await message.edit(
            "\nАдрес почты: "
            + f"<code>{str(name) + '@' + str(response.json()['email_d'])}</code>"
            + "\n"
            + f"<a href={email_link}>Линк на почту</a>"
        )
