# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: CringeGallery
# Description: Very cringe gallery
# Author: skillzmeow
# Commands:
# .cringe
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 1)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @smeowcodes

import random

from telethon.tl.types import Message

from .. import loader, utils

photos = [
    {"photo": "https://i.imgur.com/i0UTQLT.jpeg"},
    {"photo": "https://i.imgur.com/Fmn6wHw.jpeg"},
    {"photo": "https://i.imgur.com/MgkuEHA.jpeg"},
    {"photo": "https://i.imgur.com/ELyQajS.jpeg"},
    {"photo": "https://i.imgur.com/rRboNJN.jpeg"},
    {"photo": "https://i.imgur.com/Zh1h4BA.jpeg"},
    {"photo": "https://i.imgur.com/QJoFN4y.jpeg"},
    {"photo": "https://i.imgur.com/V8ueKR8.jpeg"},
    {"photo": "https://i.imgur.com/VpUSpwB.jpeg"},
    {"photo": "https://i.imgur.com/w779DYC.jpeg"},
    {"photo": "https://i.imgur.com/5ugBW8K.jpeg"},
    {"photo": "https://i.imgur.com/0KKT8Pl.jpeg"},
    {"photo": "https://i.imgur.com/atsqbE6.jpeg"},
    {"photo": "https://i.imgur.com/DFA63zo.jpeg"},
    {"photo": "https://i.imgur.com/gnH95SY.jpeg"},
    {"photo": "https://i.imgur.com/GH4pJHy.jpeg"},
    {"photo": "https://i.imgur.com/EN83r6y.jpeg"},
    {"photo": "https://i.imgur.com/lA7nkkj.jpeg"},
    {"photo": "https://i.imgur.com/EUmuz0S.jpeg"},
    {"photo": "https://i.imgur.com/ZTrulfG.jpeg"},
    {"photo": "https://i.imgur.com/3EcbnQj.jpeg"},
    {"photo": "https://i.imgur.com/6cOOiqa.jpeg"},
    {"photo": "https://i.imgur.com/MqrCnD7.jpeg"},
    {"photo": "https://i.imgur.com/Z4uZZHx.jpeg"},
]


async def random_photo() -> str:
    a = random.choice(photos)
    return a["photo"]


class CringeGalleryMod(loader.Module):
    "Very cringe gallery"
    strings = {"name": "CringeGallery"}

    async def cringecmd(self, message: Message):
        "мяу"
        await self.inline.gallery(
            message,
            random_photo,
        )
