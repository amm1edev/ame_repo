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
# yuki pr
import random as r

from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall


class YukiMod(loader.Module):
    strings = {
        "name": "YukiPr",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def yukicmd(self, message: Message):
        "узнать информацию об юки"
        yuki = (
            "<b>{} yuki</b>\n"
            "🏋<em> вес {} кг\n\n"
            "🍌 подрочил {} раз\n"
            "🦣 заскамился {} раз\n"
            "🛁 принял ванну {} раз\n"
            "🚶 нагулял {} км\n\n"
            "🍕 съел {} кг пицци\n"
            "🍼 выпил {} литров молочка</em>"
        )
        droch = self.db.get("yuki", "droch", "")
        if droch == "":
            droch = 0
        scam = self.db.get("yuki", "scam", "")
        if scam == "":
            scam = 0
        shower = self.db.get("yuki", "shower", "")
        if shower == "":
            shower = 0
        walk = self.db.get("yuki", "walk", "")
        if walk == "":
            walk = 0
        eat = self.db.get("yuki", "eat", "")
        if eat == "":
            eat = 0
        water = self.db.get("yuki", "water", "")
        if water == "":
            water = 0
        ves = self.db.get("yuki", "ves", "")
        if ves == "":
            ves = 15
        if int(ves) >= 50 and int(ves) <= 75:
            photo = "https://i.imgur.com/sL8ZfVa.jpeg"
        if int(ves) >= 30 and int(ves) <= 35:
            photo = "https://i.imgur.com/hNk7Oqc.jpeg"
        if int(ves) >= 35 and int(ves) <= 50:
            photo = "https://i.imgur.com/dltH1Rz.jpeg"
        if int(ves) <= 30:
            photo = "https://i.imgur.com/NivjXG1.jpeg"

        stat = "👦 милашка"

        await self.inline.form(
            message=message,
            text=yuki.format(stat, ves, droch, scam, shower, walk, eat, water),
            reply_markup=[[{"text": "пр юки", "url": "pornhub.com"}]],
            **({"photo": photo}),
        )

    async def groomingcmd(self, message: Message):
        "поухаживать за юки"
        await self.inline.form(
            message=message,
            text=f"<b>Что будем делать с юки?</b>",
            reply_markup=[
                [
                    {"text": "😇 ухаживать", "callback": self.grooming},
                ],
            ],
        )

    async def droch(self, call: InlineCall):
        yuka = self.db.get("yuki", "droch", "")
        if yuka == "":
            self.db.set("yuki", "droch", 1)
        if int(yuka) >= 1:
            s = int(yuka) + 1
            self.db.set("yuki", "droch", s)
        await call.edit(
            text=f"<b>💪 писька юки подрочена</b>",
            reply_markup=[
                [{"text": "🔄 вернуться назад", "callback": self.grooming}],
            ],
        )

    async def scam(self, call: InlineCall):
        scam = self.db.get("yuki", "scam", "")
        if scam == "":
            scam = 0
        s = r.randint(1, 100)

        if s == 5 or s == 15 or s == 25 or s == 50 or s == 75:
            x = int(scam) + 1
            self.db.set("yuki", "scam", x)
            await call.edit(
                text=f"<b>🦧 юки заскамлен как нубяра</b>",
                reply_markup=[
                    [
                        {"text": "🔄 вернуться назад", "callback": self.grooming},
                    ],
                ],
            )

        else:
            await call.edit(text="<b>🤗 ты не смог скамнуть юки</b>")

    async def walk(self, call: InlineCall):
        walk = self.db.get("yuki", "walk", "")
        if walk == "":
            self.db.set("yuki", "walk", 0)
        pr = int(self.db.get("yuki", "walk", "")) + 1
        self.db.set("yuki", "walk", pr)
        await call.edit(
            text=f"<b>👬 ты выгулял юки\n</b>",
            reply_markup=[
                [
                    {"text": "🔄 вернуться назад", "callback": self.grooming},
                ],
            ],
        )

    async def shower(self, call: InlineCall):
        shower = self.db.get("yuki", "shower", "")
        if shower == "":
            self.db.set("yuki", "shower", 0)
        pr = int(self.db.get("yuki", "shower", "")) + 1
        self.db.set("yuki", "shower", pr)
        await call.edit(
            text="<b>🧼 ты искупал юки и искупил все свои грехи</b>",
            reply_markup=[
                [
                    {"text": "🔄 вернуться назад", "callback": self.grooming},
                ],
            ],
        )

    async def eat(self, call: InlineCall):
        eat = self.db.get("yuki", "eat", "")
        ves = self.db.get("yuki", "ves", "")

        if eat == "":
            self.db.set("yuki", "eat", 0)
        d = r.randint(1, 6)
        if ves == "":
            self.db.set("yuki", "ves", 15)
        v = self.db.get("yuki", "ves", "")
        if d == 4:
            f = int(v) + 1
            self.db.set("yuki", "ves", f)
            f_text = "<b>🍔 вы покормили юки, он поправился на 1 кг</b>"
        else:
            f_text = "<b>🍔 вы покормили юки</b>"
        d = int(eat) + 1
        self.db.set("yuki", "eat", d)

        await call.edit(
            text=f_text,
            reply_markup=[
                [
                    {"text": "🔄 вернуться назад", "callback": self.grooming},
                ],
            ],
        )

    async def water(self, call: InlineCall):
        water = self.db.get("yuki", "water", "")
        if water == "":
            self.db.set("yuki", "water", 0)
        pr = int(self.db.get("yuki", "water", "")) + 1
        self.db.set("yuki", "water", pr)
        await call.edit(
            text="<b>🥛 ты напоил юки, теперь он не хочет пить</b>",
            reply_markup=[
                [
                    {"text": "🔄 вернуться назад", "callback": self.grooming},
                ],
            ],
        )

    async def grooming(self, call: InlineCall):
        "поухаживать за юки"
        await call.edit(
            text=f"<b>Что будем делать с юки?</b>",
            reply_markup=[
                [
                    {"text": "👼 подрочить", "callback": self.droch},
                    {"text": "🦣 заскамить", "callback": self.scam},
                ],
                [
                    {"text": "🧍‍♂️ выгулять", "callback": self.walk},
                    {"text": "🚿 помыть", "callback": self.shower},
                ],
                [
                    {"text": "🌮 покормить", "callback": self.eat},
                    {"text": "🍼 дать воды", "callback": self.water},
                ],
            ],
        )
