# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: DrochBot
# Description: Автоматизирует работу с @DrochBot (автоматическая дрочка и др.)
# Author: SkillsAngels
# Commands:
# .droch | .dick | .case
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 7)
#
#
# _           _            _ _
# | |         | |          (_) |
# | |     ___ | |_ ___  ___ _| | __
# | |    / _ \| __/ _ \/ __| | |/ /
# | |___| (_) | || (_) \__ \ |   <
# \_____/\___/ \__\___/|___/_|_|\_\
#
#              © Copyright 2022
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikkaftgmods
# meta banner: https://i.imgur.com/awltLuz.jpeg


import asyncio

from .. import loader, utils


class DrochBotMod(loader.Module):
    """Автоматизирует работу с @DrochBot (автоматическая дрочка и др.)"""

    strings = {"name": "DrochBot"}

    async def drochcmd(self, message):
        """Включается команда `/drochnut`. Чтобы остановить, `Дрочка стоп`."""
        self.set("droch", True)
        while self.get("droch"):
            await message.reply("/drochnut")
            await asyncio.sleep(0.1)
            await utils.answer(
                message,
                "Следующая команда будет произведена через 1 час и 5 минут.",
            )
            await asyncio.sleep(3960)

    async def dickcmd(self, message):
        """Включается команда `/drochnut`. Чтобы остановить, `Хуй стоп`."""
        self.set("dick", True)
        while self.get("dick"):
            await message.reply("/dick")
            await asyncio.sleep(0.1)
            await utils.answer(
                message,
                "Следующая команда будет произведена через 6 часов.",
            )
            await asyncio.sleep(21600)

    async def casecmd(self, message):
        """Включается команда `/case`. Чтобы остановить, `кейс стоп`."""
        self.set("case", True)
        while self.get("case"):
            await message.reply("/case")
            await asyncio.sleep(0.1)
            await utils.answer(
                message,
                "Следующая команда будет произведена через 24 часa.",
            )
            await asyncio.sleep(86400)

    async def watcher(self, message):
        if not getattr(message, "out", False):
            return

        if message.raw_text.lower() == "дрочка стоп":
            self.set("droch", False)
            await utils.answer(message, "<b>Дрочка остановлена.</b>")
        if message.raw_text.lower() == "хуй стоп":
            self.set("dick", False)
            await utils.answer(message, "<b>Рост хуя остановлен.</b>")
        if message.raw_text.lower() == "кейс стоп":
            self.set("case", False)
            await utils.answer(message, "<b>Открытие кейсов остановлено<b>")
