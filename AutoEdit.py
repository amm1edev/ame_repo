# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AutoEdit
# Author: dorotorothequickend
# Commands:
# .autoedit
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroAutoEdit.png
# meta developer: @DorotoroMods

import asyncio

from .. import loader, utils


@loader.tds
class AutoEdit(loader.Module):
    """Редактирует каждое ваше сообщение в определенное время на выбранный вами текст.\n Настройка через .config AutoEdit"""

    strings = {
        "name": "AutoEdit",
        "timechoice": "Время, за которое будет редактироваться сообщение.(в секундах)",
        "editmsg": "Текст, на который будет редактироваться ваше сообщение.",
    }

    @loader.watcher(out=True)
    async def watcher(self, message):
        if self.get("autoedit"):
            if message.text == "<b><i>AutoEdit on.</i></b>":
                return
            if message.text == "@DorotoroMods":
                return
            if message.text == "@AstroModules":
                return

            await asyncio.sleep(self.config["timechoice"])
            await message.edit(self.config["editmsg"])

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "timechoice", "10", doc=lambda: self.strings("timechoice")
            ),
            loader.ConfigValue(
                "editmsg",
                "<b>========\nЗасекречено</b>",
                doc=lambda: self.strings("editmsg"),
            ),
        )

    @loader.command()
    async def autoedit(self, message):
        "- включить/выключить AutoEdit."
        if self.get("autoedit") == True:
            self.set("autoedit", False)
            await utils.answer(message, "<b><i>AutoEdit off.</i></b>")
            return
        elif self.get("autoedit") == False or self.get("autoedit") is None:
            self.set("autoedit", True)
            await utils.answer(message, "<b><i>AutoEdit on.</i></b>")
