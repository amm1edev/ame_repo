# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: IrisLab
# Author: SkillsAngels
# Commands:
# .lab | .victims | .upg | .g | .sv
# .d   | .list    | .ic 
# ---------------------------------------------------------------------------------

import contextlib

__version__ = (0, 0, 2)

# _           _            _ _
# | |         | |          (_) |
# | |     ___ | |_ ___  ___ _| | __
# | |    / _ \| __/ _ \/ __| | |/ /
# | |___| (_) | || (_) \__ \ |   <
# \_____/\___/ \__\___/|___/_|_|\_\
#
#              © Copyright 2022
#
#         developed by @lotosiiik, @byateblan

# █ █ ▀ █▄▀ ▄▀█ █▀█ ▀    ▄▀█ ▀█▀ ▄▀█ █▀▄▀█ ▄▀█
# █▀█ █ █ █ █▀█ █▀▄ █ ▄  █▀█  █  █▀█ █ ▀ █ █▀█
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikkaftgmods
# meta banner: https://i.imgur.com/2KZ38Pv.jpeg
# meta pic: https://i.imgur.com/QntqxyH.jpeg

import asyncio
import logging
import re

from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class IrisLabMod(loader.Module):
    """Показывает лаб/жертв. Возможны задержки на получение инф-ции"""

    strings = {
        "name": "IrisLab",
        "saved": "💾 <b>Заметка с именем </b><code>{}</code><b> сохранена</b>.",
        "no_reply": "🚫 <b>Требуется реплай на контент заметки.</b>",
        "no_name": "🚫 <b>Укажите имя заметки.</b>",
        "no_note": "🚫 <b>Данная заметка не найдена или она не существует.</b>",
        "available_notes": "💾 <b>Текущие заметки:</b>\n",
        "no_notes": "😔 <b>У тебя пока что нет заметок</b>",
        "deleted": "🙂 <b>Заметка с именем </b><code>{}</code> <b>удалена</b>",
        "lab_data": {
            "d": "(.*) Досье лаборатории (.*)",
            "s": "(.*) Руководитель: (.*)",
            "с": "(.*) В составе Корпорации (.*)",
            "n": "(.*) Имя патогена: (.*)",
            "p": "(.*) Готовых патогенов: (.*) из (.*)",
            "q": "(.*) Квалификация учёных: (.*)",
            "np": "(.*) Новый патоген: (.*)",
            "inf": "(.*) Заразность: (.*)",
            "imn": "(.*) Иммунитет: (.*)",
            "m": "(.*) Летальность: (.*)",
            "ss": "(.*) Служба безопасности: (.*)",
            "be": "(.*) Био-опыт: (.*)",
            "br": "(.*) Био-ресурс: (.*)",
            "so": "(.*) Спецопераций: (.*)",
            "prev": "(.*) Предотвращены: (.*)",
            "i": "(.*) Заражённых: (.*)",
            "dis": "(.*) Своих болезней: (.*)",
            "f": "<b> Руководитель в состоянии горячки",
        },
    }

    async def client_ready(self, client, db):
        db.set("Iris", "chat_biowar", "@iris_black_bot")

        self.client = client
        self.db = db
        self._notes = self.get("victims_list", {})

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

    async def labcmd(self, message):
        """Модуль который выдаст вам статистику вашей лаборатории (лаб)"""
        bot = "@iris_black_bot"
        lab = await self.message_q(".Лаб", bot, mark_read=True, delete=True)
        args_raw = utils.get_args_raw(message)
        if not args_raw:
            return await utils.answer(message, lab.text)

        data, text = self.strings("lab_data"), []
        flags = "".join(args_raw.split(" ")).split("-")
        if "" in flags:
            flags.remove("")
        for flag in flags:
            search = re.search(data[flag], lab.text) if flag in data else None
            if search:
                if flag == "be":
                    num = search.group().split(":")[-1].replace(" ", "")
                    if num[-1] == "k":
                        num = (
                            int(num[:-1].replace(",", "")) * 100 / 100 * 10
                            if "," in num
                            else int(num[:-1]) * 1000 / 100 * 10
                        )
                    elif num[:-1] != "k":
                        num = int(num) / 100 * 10
                    text.append(f"{search.group()} | {num}")
                elif flag == "d":
                    text.append(search.group()[:-1])
                else:
                    text.append(search.group())
            elif flag == "parametrs":
                text = """
d: Имя лаборатории
s: Руководитель
с: Корпорация

n: Имя патогена
p: Готовых патогенов
q: Квалификация учёных 👨‍🔬
np: Новый патоген через... ⏱

inf: Заразность 
imn: Иммунитет 🛡️
m: Летальность ☠️
ss: Служба безопасности 

be: Био-опыт ☣️
br: Био-ресурс 🧬
so: Спецопераций 😷
prev: Предотвращены 🥽

i: заражённых 🤒
dis: Своих болезней 🤒

f: Горячка руководителя 
v: Ежедневная премия(ежа) 💸"""
                return await utils.answer(message, text)
            elif flag == "v":
                await asyncio.sleep(3)
                bot = "@iris_black_bot"
                victims = await self.message_q(
                    "Мои жертвы", bot, mark_read=True, delete=True
                )
                result = re.search(
                    r"""(.*) Ежедневная премия: (.*)""", victims.text
                ).group()
                text.append(result)
            elif flag in data:
                app_text = (
                    "✅ Все патогены приготовлены" if flag == "np" else "❌ Горячки нету"
                )
                text.append(app_text)
            else:
                text.append(f"Параметр -{flag} не указан.")
            return await utils.answer(message, "\n".join(text))

    async def victimscmd(self, message):
        """Комманда показывает ваши жертвы"""
        bot = "@iris_black_bot"
        victims = await self.message_q(
            "Мои жертвы",
            bot,
            mark_read=True,
            delete=True,
        )

        args_raw = utils.get_args_raw(message)

        if not args_raw:
            await utils.answer(message, victims.text)

    async def upgcmd(self, message):
        """Увеличивает зз/имун и тд.Как использовать(Пример) .upg летальность (число 1-5)"""
        args = utils.get_args(message)
        bot = "@iris_black_bot"
        characteristics = (
            "заразность",
            "летальность",
            "иммунитет",
            "безопасность",
            "разработка",
            "патоген",
        )
        if len(args) != 2:
            await utils.answer(message, "Указано больше или меньше двух параметров")
        elif args[0].lower() not in characteristics:
            await utils.answer(message, "Данного улучшения не существует")
        elif not args[1].isdigit():
            await utils.answer(message, "Второй параметр не является числом")
        elif int(args[1]) > 5 or int(args[1]) < 0:
            await utils.answer(message, "Уровень указан вне допустимого диапазона")
        else:
            upgrade = await self.message_q(
                f"++{args[0].lower()} {args[1]}",
                bot,
                mark_read=True,
                delete=True,
            )

            args_raw = utils.get_args_raw(message)

            await utils.answer(message, upgrade.text)

    async def gcmd(self, message: Message):
        """<name> - показывает заметку"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_name"))
            return

        asset = self._get_note(args)
        if not asset:
            await utils.answer(message, self.strings("no_note"))
            return

        await self._client.send_message(
            message.peer_id,
            await self._db.fetch_asset(asset["id"]),
            reply_to=getattr(message, "reply_to_msg_id", False),
        )

        if message.out:
            await message.delete()

    async def svcmd(self, message):
        """<name> - для сохранения заметки"""
        args = utils.get_args_raw(message)
        folder = "victims_list"

        reply = await message.get_reply_message()
        if not (reply and args):
            await utils.answer(message, self.strings("no_reply"))
            return
        if folder not in self._notes:
            self._notes[folder] = {}
            logger.warning(f"Created new folder {folder}")

        asset = await self._db.store_asset(reply)

        type_ = "☣️"

        self._notes[folder][args] = {"id": asset, "type": type_}

        self.set("victims_list", self._notes)

        await utils.answer(message, self.strings("saved").format(args, folder))

    def _get_note(self, name: str):
        for notes in self._notes.values():
            for note, asset in notes.items():
                if note == name:
                    return asset

    def _del_note(self, name: str):
        for category, notes in self._notes.copy().items():
            for note in notes.copy():
                if note == name:
                    del self._notes[category][note]

                if not self._notes[category]:
                    del self._notes[category]

                self.set("victims_list", self._notes)
                return True

        return False

    async def dcmd(self, message: Message):
        """<name> - удаляет заметку"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_name"))
            return

        asset = self._get_note(args)
        if not asset:
            await utils.answer(message, self.strings("no_note"))
            return

        with contextlib.suppress(Exception):
            await (await self._db.fetch_asset(asset["id"])).delete()

        self._del_note(args)

        await utils.answer(message, self.strings("deleted").format(args))

    async def listcmd(self, message: Message):
        """[folder] - показывает все заметки"""
        args = utils.get_args_raw(message)

        if not self._notes:
            await utils.answer(message, self.strings("no_notes"))
            return

        result = self.strings("available_notes")
        if not args or args not in self._notes:
            for category, notes in self._notes.items():
                result += f"\n🔸 <b>{category}</b>\n"
                for note, asset in notes.items():
                    result += f"    {asset['type']} <code>{note}</code>\n"

            await utils.answer(message, result)
            return

        for note, asset in self._notes[args].items():
            result += f"{asset['type']} <code>{note}</code>\n"

        await utils.answer(message, result)

    async def iccmd(self, message: Message):
        """Комманда котрая вычисляет сколько 🧬Био-ресурсов или же ic☣️ нужно\nПример: .ic <характеристика> <уровень С> <уровень До>"""
        args = utils.get_args(message)
        if (
            not args
            or len(args) != 3
            or not args[1].isdigit()
            or not args[2].isdigit()
            or int(args[2]) == int(args[1])
            or int(args[2]) < int(args[1])
        ):
            await utils.answer(
                message,
                (
                    "🚫| <b>Чтобы использовать калькулятор напишите .ic <навык> <уровень"
                    " С> <уровень До></b>"
                ),
            )
            return

        skill, from_lvl, to_lvl = args
        from_lvl, to_lvl = int(from_lvl), int(to_lvl)
        amount = (
            await self._client.inline_query(
                "@hikkaftgbot", f"{skill}#{from_lvl}#{to_lvl}"
            )
        )[0].title

        if not amount.isdigit():
            await utils.answer(message, amount)
            return

        amount = f"{int(amount):,}".replace(",", " ")

        await utils.answer(
            message,
            (
                f"🍀| Чтобы увеличить навык «{skill}» с {from_lvl} до {to_lvl} уровня"
                f" потребуется: {amount} био-ресурсов🧬 или же ic☣️"
            ),
        )

    async def listcmd(self, message):
        """Помощь по ирис лабу."""

        hi = (
            "🍀| <b>Флаги которые помогут узнать отдельную часть"
            ' лаборатории:</b>\n\n"d": "Досье лаборатории ",\n"s": "Руководитель:'
            ' ",\n"с": "В составе Корпорации ",\n"n": "Имя патогена: ",\n"p": "Готовых'
            ' патогенов: ",\n"q": "Квалификация учёных: ",\n"np": "Новый патоген:'
            ' ",\n"inf": "Заразность: ",\n"imn": "Иммунитет: ",\n"m": "Летальность:'
            ' ",\n"ss": "Служба безопасности: ",\n"be": "Био-опыт: ",\n"br":'
            ' "Био-ресурс: ",\n"so": " Спецопераций: ",\n"prev": " Предотвращены:'
            ' ",\n"i": " Заражённых: ",\n"dis": "Своих болезней: ",\n"f": "Руководитель'
            ' в состоянии горячки"\n\n <b>Пример использования флагов: .lab v or .lab'
            " np</b>"
        )

        await utils.answer(message, f"{hi}")
