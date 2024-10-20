# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: GasolineUa
# Description: Gasoline price viewer taken from https://auto.ria.com/uk/toplivo/
# Author: skillzmeow
# Commands:
# .lin
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 2)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes
# requires: requests beautifulsoup4 tabulate lxml
# scope: inline
# meta pic: https://siasky.net/XAArZx4f9mnJtcZpS1M8HSmPgK7xDTDC9NGLCwH9k0mJcQ
# meta banner: https://siasky.net/fAMzBfMaahm2JTF3ULfrNQHu9R_V5MDP9tiZa-nrVPsqMQ

import random

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineQuery


def gassearch():
    response = requests.get("https://auto.ria.com/uk/toplivo/")
    soup = BeautifulSoup(response.text, "lxml")
    benz = soup.find_all("div", class_="t-row")
    price = []
    names = ["A-95+  ", "A-95 ", "A-92 ", "ДП ", "Газ "]
    for gasoline in benz:
        a = gasoline.find("div", class_="t-cell bold size18")
        if a:
            price.append(a.get_text() + "₴")
    data = [list(gas) for gas in zip(names, price)]

    return (
        f"<b>Паливо</b>  <b>Ціна/л</b><code>{tabulate(data, headers=['', ''])}</code>"
    )


class GasolineUaMod(loader.Module):
    """Gasoline price viewer taken from https://auto.ria.com/uk/toplivo/"""

    strings = {
        "name": "GasolineUa",
    }

    async def lincmd(self, message: Message):
        "See the price of gasoline"
        m = random.randint(0, 5)
        if m == 4:
            markup = [[{"text": "💞 More modules", "url": "https://t.me/smeowcodes"}]]
        else:
            markup = []
        await self.inline.form(
            message=message,
            text=gassearch(),
            reply_markup=markup,
        )

    @loader.inline_everyone
    async def lin_inline_handler(self, query: InlineQuery):
        "lincmd inline version"
        return {
            "title": "GasolinPrice",
            "description": "meow",
            "message": gassearch(),
        }
