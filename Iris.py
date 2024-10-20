# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Iris
# Author: SkillsAngels
# Commands:
# .farmon | .farmoff | .farm | .bag | .irish
# .give  
# ---------------------------------------------------------------------------------

version = (0, 0, 2)

# for more info: https://murix.ru/files/ftg
# by xadjilut, 2021

# модуль частично не мой | This module is not half mine.

# _           _            _ _
# | |         | |          (_) |
# | |     _ | |_ _  _ _| |
# | |    / _ \| / _ \/ | | |/ /
# | |_| (_) | || (_) \ \ |   <
# \_/\_/ \\_/|_/_|_|\_\
#
#              © Copyright 2022
#
#         developed by @lotosiiik, @byateblan

# meta developer: @hikkaftgmods
# meta banner: https://te.legra.ph/file/a428776824470e0bdccb6.jpg
# meta pic: https://te.legra.ph/file/98192f1f7953275baead5.jpg

import random
from datetime import timedelta

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class IrisMod(loader.Module):
    """Для автоматического фарминга коинов в ирисботе"""

    strings = {
        "name": "Iris",
        "farmon": (
            "<i>✅Отложенка создана, автофарминг запущен, всё начнётся через 20"
            " секунд...</i>"
        ),
        "farmon_already": "<i>Уже запущено</i>",
        "farmoff": "<i>❌Автофарминг остановлен.\n☢️Надюпано:</i> <b>%coins% i¢</b>",
        "farm": "<i>☢️Надюпано:</i> <b>%coins% i¢</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id
        self.iris = 5443619563

    async def farmoncmd(self, message):
        """Запустить автофарминг"""
        status = self.db.get(self.name, "status", False)
        if status:
            return await message.edit(self.strings["farmon_already"])
        self.db.set(self.name, "status", True)
        await self.client.send_message(
            self.iris, "Фарма", schedule=timedelta(seconds=20)
        )
        await message.edit(self.strings["farmon"])

    async def farmoffcmd(self, message):
        """Остановить автофарминг"""
        self.db.set(self.name, "status", False)
        coins = self.db.get(self.name, "coins", 0)
        if coins:
            self.db.set(self.name, "coins", 0)
        await message.edit(self.strings["farmoff"].replace("%coins%", str(coins)))

    async def farmcmd(self, message):
        """Вывод кол-ва коинов, добытых этим модулем"""
        coins = self.db.get(self.name, "coins", 0)
        await message.edit(self.strings["farm"].replace("%coins%", str(coins)))

    async def watcher(self, event):
        if not isinstance(event, Message):
            return
        chat = utils.get_chat_id(event)
        if chat != self.iris:
            return
        status = self.db.get(self.name, "status", False)
        if not status:
            return
        if event.raw_text == "Фарма":
            return await self.client.send_message(
                self.iris, "Фарма", schedule=timedelta(minutes=random.randint(1, 20))
            )
        if event.sender_id != self.iris:
            return
        if "НЕЗАЧЁТ!" in event.raw_text:
            args = [int(x) for x in event.raw_text.split() if x.isnumeric()]
            randelta = random.randint(20, 60)
            if len(args) == 4:
                delta = timedelta(
                    hours=args[1], minutes=args[2], seconds=args[3] + randelta
                )
            elif len(args) == 3:
                delta = timedelta(minutes=args[1], seconds=args[2] + randelta)
            elif len(args) == 2:
                delta = timedelta(seconds=args[1] + randelta)
            else:
                return
            sch = (
                await self.client(
                    functions.messages.GetScheduledHistoryRequest(self.iris, 1488)
                )
            ).messages
            await self.client(
                functions.messages.DeleteScheduledMessagesRequest(
                    self.iris, id=[x.id for x in sch]
                )
            )
            return await self.client.send_message(self.iris, "Фарма", schedule=delta)
        if "ЗАЧЁТ" in event.raw_text or "УДАЧА" in event.raw_text:
            args = event.raw_text.split()
            for x in args:
                if x[0] == "+":
                    return self.db.set(
                        self.name,
                        "coins",
                        self.db.get(self.name, "coins", 0) + int(x[1:]),
                    )

    async def message_q(
        self,
        text: str,
        user_id: int,
        mark_read: bool = False,
        delete: bool = False,
    ):
        """Отправляет сообщение и возращает ответ"""
        async with self.client.conversation(user_id) as conv:
            msg = await conv.send_message(text)
            response = await conv.get_response()
            if mark_read:
                await conv.mark_read()

            if delete:
                await msg.delete()
                await response.delete()

            return response

    @loader.command()
    async def give(self, message):
        """Передает ириски/голд на другой акк"""
        bot = "@iris_black_bot"
        args = utils.get_args_raw(message)
        nmb = int(args.split(" ")[1])
        if message.is_reply:
            replied_to = await message.get_reply_message()
            player = "@" + str(replied_to.from_id)
        else:
            player = args.split(" ")[2]
        dada = ""
        if args.split(" ")[0] == "голд":
            dada = " голд"
        elif args.split(" ")[0] == "ириски" or args[0] == "ирис":
            dada = ""
        else:
            return await utils.answer(
                message, "❌| Ошибка,что-бы передать требуется написать ириски или голд."
            )

        text = f"Передать{dada} {nmb} {player}"
        try:
            text += f'\n{args.split(" | ")[1]}'
        except IndexError:
            pass

        givs = await self.message_q(
            text,
            bot,
            mark_read=True,
            delete=True,
        )

        await utils.answer(message, givs.text)

    @loader.command()
    async def baghis(self, message):
        """Информация где побывали ваши ириски"""
        bot = "@iris_black_bot"
        text = f"где мои ириски"
        givs = await self.message_q(
            text,
            bot,
            mark_read=True,
            delete=True,
        )

        await utils.answer(message, givs.text)

    @loader.command()
    async def bagcmd(self, message):
        """Показывает ваш мешок"""

        bot = "@iris_black_bot"
        bags = await self.message_q(
            "Мешок",
            bot,
            delete=True,
        )

        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, bags.text)

    async def irishcmd(self, message):
        """Помощь по модулю Iris"""
        ihelp = (
            "🍀| <b>Помощь по командам:</b>\n\n .farmon - Включает авто фарм.\n .farmoff"
            " - Выключает авто фарм.\n .farm - Показывает сколько вы нафармили.\n .bag"
            " - Показывает ваш ммешок\n .give - передаёт ириски/голд\n\n"
            " <b>Пример:</b>\n .give {ириски или голд} {число} {юзер}. - без причины.\n"
            " .give {ириски или голд} {число} {юзер} | {причина}"
        )
        await utils.answer(message, ihelp)
