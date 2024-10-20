# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MeowHomework
# Description: No description
# Author: skillzmeow
# Commands:
# .stbl | .hlang | .gt
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 1)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#  ну и пошла нахуй блять dae
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @skillzmeow

import random as r

from telethon.tl.types import Message

from .. import loader, utils

dayz = "пн вт ср чт пт сб"
u_days = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота"]
r_days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
sdays = ["пн", "вт", "ср", "чт", "пт", "сб"]


class HomeworkMod(loader.Module):
    strings = {"name": "MeowHomework"}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def stblcmd(self, msg: Message):
        """день недели | урок1, урок2"""
        args = utils.get_args_raw(msg)
        s = args.split(" | ")
        self.db.set("day", s[0].lower(), s[1])
        await utils.answer(msg, "День успешно установлен!")

    async def hlangcmd(self, msg: Message):
        """ru или ua"""
        # lang = self.db.get("day", "language", "")
        args = utils.get_args_raw(msg)
        if args.lower() == "ru" or args.lower() == "ua":
            self.db.set("day", "language", args)
            await utils.answer(msg, "Язык успешно установлен")
        else:
            await utils.answer(msg, 'Используй аргумент "RU" или "UA"')

    async def gtcmd(self, msg: Message):
        """день недели"""
        lang = self.db.get("day", "language", "")
        args = utils.get_args_raw(msg)
        if args:
            args = args.lower()
            if args in dayz:
                f = sdays.index(args)
                argz = r_days if lang == "" or lang == "ru" else u_days
                args = args.replace(sdays[f], argz[f])
            table = self.db.get("day", args, "")
            spl = table.split(", ")
            num = 1
            list_lessons = []
            for les in spl:
                lesson = str.capitalize(les)
                list_lessons.append("> <code>{}. {}</code>".format(num, lesson))
                num += 1
            await utils.answer(
                msg,
                "🔍 <b>{}:</b>\n{}".format(
                    str.capitalize(args), "\n".join(list_lessons)
                ),
            )
