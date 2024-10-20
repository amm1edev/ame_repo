# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: farmMoo
# Description: Для автоматического фарминга мубота.\n отправляет мус, кликает, затем мук, кликает. и всё по циклу.
# Author: trololo65
# Commands:
# .mbfon | .mbfoff
# ---------------------------------------------------------------------------------


# for more info: https://murix.ru/files/ftg
# by xadjilut, 2021
# Изменил для мубота @trololo_1

import asyncio

from .. import loader, utils


@loader.tds
class FarmMooBotMod(loader.Module):
    """Для автоматического фарминга мубота.\n отправляет мус, кликает, затем мук, кликает. и всё по циклу."""

    strings = {
        "name": "FarmMooBot",
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.moo = 1606812809
        if not self.db.get(self.name, "status", False):
            self.db.set(
                self.name,
                "status",
                {"status": False, "time": None, "btn1": None, "btn2": None},
            )

    async def mbfoncmd(self, message):
        """Запустить автофарминг.\n.mbfon {интервал отправки} {первая кнопка} {вторая кнопка} | кнопки указывать по очередности."""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, "Где аргументы?")
        args = args.split(" ")
        if not args[0].isdigit() or not args[1].isdigit() or not args[2].isdigit():
            return await utils.answer(
                message,
                (
                    "Один или более аргументов указан не корректно. Вводите только"
                    " числовые значения!!"
                ),
            )
        status = self.db.get(self.name, "status", False)
        if status["time"]:
            return await utils.answer(message, "Уже запущено.")
        self.db.set(
            self.name,
            "status",
            {"status": True, "time": args[0], "btn1": args[1], "btn2": args[2]},
        )
        await self.client.send_message(self.moo, "мус")
        await utils.answer(message, "Запущено.")

    async def mbfoffcmd(self, message):
        """Остановить автофармин."""
        self.db.set(
            self.name,
            "status",
            {"status": False, "time": None, "btn1": None, "btn2": None},
        )
        await utils.answer(message, "Остановлено.")

    async def watcher(self, message):
        try:
            chat = utils.get_chat_id(message)
            if chat != self.moo:
                return
            args = self.db.get(self.name, "status", False)
            if not args:
                return
            if not args["status"] or message.sender_id != self.moo or message.sticker:
                return
            try:
                if (
                    not "🐮" in message.text
                    and "<strong>" in message.text
                    and args["status"]
                ):
                    await message.click(int(args["btn1"]) - 1)
                await asyncio.sleep(3)
                if (
                    args["status"]
                    and not "🐮" in message.text
                    and "<strong>" in message.text
                ):
                    await self.client.send_message(self.moo, "мук")
            except:
                if args["status"]:
                    await self.client.send_message(self.moo, "мус")
                if (
                    not "🐮" in message.text
                    and "<strong>" in message.text
                    and args["status"]
                ):
                    await message.click(int(args["btn1"]) - 1)
            try:
                if "🐮" in message.text or args["status"]:
                    await message.click(int(args["btn2"]) - 1)
            except:
                if args["status"]:
                    await self.client.send_message(self.moo, "мук")
                if "🐮" in message.text and args["status"]:
                    await message.click(int(args["btn2"]) - 1)
            await asyncio.sleep(int(args["time"]))
            if args["status"] and "🐮" in message.text:
                await self.client.send_message(self.moo, "мус")
        except:
            pass
