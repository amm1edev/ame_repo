# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AntiRacism
# Description: Delete racists messages
# Author: skillzmeow
# Commands:
# .antiracism
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 1)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes

from telethon.tl.types import Message

from .. import loader, utils


class AntiRacismMod(loader.Module):
    """delete racists messages"""

    strings = {
        "name": "AntiRacism",
        "enabled": "🐈 AntiRacism enabled",
        "disabled": "🐈‍⬛ AntiRacism disabled",
    }
    strings_ru = {
        "enabled": "🐈 Антирасизм включен",
        "disabled": "🐈‍⬛ Антирасизм выключен",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def antiracismcmd(self, message: Message):
        "acivate/deactivate antiracism"
        status = self.db.get(
            "anti",
            "status",
        )
        if status == "":
            self.db.set("anti", "status", False)
        if status == False:
            self.db.set("anti", "status", True)
            await utils.answer(message, f"<b>{self.strings('enabled')}</b>")
        else:
            self.db.set("anti", "status", False)
            await utils.answer(message, f"<b>{self.strings('disabled')}</b>")

    async def watcher(self, message: Message):
        text = message.text
        word = [
            "негр",
            "негры",
            "негра",
            "негров",
            "негроид",
            "негроиды",
            "негроида",
            "негроидов",
            "нигга",
            "нигги",
            "негрики",
            "негриков",
            "nigga",
            "nigger",
            "niga",
            "niger",
            "niggers",
            "nigers",
        ]
        status = self.db.get(
            "anti",
            "status",
        )
        if status == False:
            return
        if status == True:
            for i in word:
                s = text.lower().find(i)
                if s != -1:
                    await message.delete()
