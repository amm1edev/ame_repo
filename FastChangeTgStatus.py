# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: FastChangeTgStatus
# Author: sqlmerr
# Commands:
# .statuschange | .statuslist | .statusadd | .statusclear
# ---------------------------------------------------------------------------------

# ░██████╗░██████╗░██╗░░░░░███╗░░░███╗███████╗██████╗░██████╗░
# ██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔════╝██╔══██╗██╔══██╗
# ╚█████╗░██║██╗██║██║░░░░░██╔████╔██║█████╗░░██████╔╝██████╔╝
# ░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗
# ██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║
# ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
# ---------------------------------------------------------------------------------------------
# Name: FastChangeTgStatus
# Description: Change your status fast. For premium users | Изменяйте ваш статус быстро. Только для премиум пользователей
# Author: sqlmerr
# Commands:
# .statuschange | .statuslist | .statusadd
# ---------------------------------------------------------------------------------------------

# meta developer: @sqlmerr_m


# импортируем нужные библиотеки
import asyncio
import logging
import re

from telethon import errors, events, functions, types
from telethon.tl.types import Message, MessageEntityCustomEmoji

from .. import loader, utils

logger = logging.getLogger(__name__)


# сам класс модуля
@loader.tds
class FCTS(loader.Module):
    """Change your status fast. Only for premium users | Изменяйте ваш статус быстро. Только для премиум пользователей"""

    # нужные переменные
    strings = {
        "name": "FastChangeTgStatus",
        "no_args": "<b>You didn't enter any arguments!</b>",
        "status_changed": "<b>Your status successfully changed to {}!</b>",
        "status_is_none": "<b>This status does not exist!</b>",
        "list": (
            "<emoji document_id=5836898273666798437>⭐️</emoji> <b>List of your"
            " statuses</b>:"
        ),
        "emoji_added": "<b>Emoji added to status list successfully</b>",
        "indexerror": (
            "<emoji document_id=5447644880824181073>⚠️</emoji> <b>You have entered too"
            " few arguments!</b>"
        ),
    }
    strings_ru = {
        "no_args": "<b>Вы не ввели аргументы!</b>",
        "status_changed": "<b>Ваш статус успешно изменен на {}!</b>",
        "status_is_none": "<b>Такого статуса не существует!</b>",
        "list": (
            "<emoji document_id=5836898273666798437>⭐️</emoji> <b>Список ваших"
            " статусов</b>:"
        ),
        "emoji_added": "<b>Эмодзи успешно добавлен в список статусов</b>",
        "indexerror": (
            "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Вы ввели слишком мало"
            " аргументов!</b>"
        ),
    }

    async def client_ready(self):
        if not self._client.hikka_me.premium:
            raise loader.LoadError(
                "This module is for Telegram Premium only!"
            )  # Немного взял кода из модуля TgStatus от @hikarimods
        self.default = {
            "sleep": "5875318886433295705",
            "game": "5877201954714684742",
            "heart": "5875452644599795072",
            "do not disturb": "5877477244938489129",
            "plane": "5877464772353460958",
            "home": "5877506824378257176",
        }

    @loader.command(
        ru_doc=(
            "[имя статуса] - поставить этот статус | .statuslist для просмотра ваших"
            " установленных статусов"
        )
    )
    async def statuschange(self, m):
        "[status name] - set this status | .statuslist to view your downloaded statuses"
        args = utils.get_args_raw(m)
        if not args:
            return await utils.answer(m, self.strings("no_args"))
        default = self.default
        s = self.get("s", default)
        status = s.get(args)
        if status is None:
            return await utils.answer(m, self.strings("status_is_none"))
        await self._client.set_status(int(status))
        await utils.answer(m, self.strings("status_changed").format(args))

    @loader.command(ru_doc="Посмотреть список всех статусов")
    async def statuslist(self, m):
        "See list of all your statuses"
        s = self.get("s", self.default)
        statuses = f"{self.strings('list')}\n"
        for j in s:
            emoji = f"<emoji document_id={s.get(j)}>▫️</emoji>"
            statuses += f"• {emoji} {j}\n"
        await utils.answer(m, statuses)

    @loader.command(ru_doc="[эмодзи] [короткое имя] Добавить кастомный статус")
    async def statusadd(self, m):
        "[emoji] [short name] Add a custom status"
        s = self.get("s", self.default)
        args = utils.get_args_raw(m).split()
        if not args:
            return await utils.answer(m, self.strings("no_args"))
        try:
            # emoji = m.text.split()[1]
            name = args[1]
        except IndexError:
            return await utils.answer(m, self.strings("indexerror"))

        for emoji in m.entities:
            if isinstance(emoji, MessageEntityCustomEmoji):
                e = str(emoji.document_id)

        s[name] = e

        self.set("s", s)
        await utils.answer(m, self.strings("emoji_added"))

    @loader.command(ru_doc="Очистить все кастомные статусы")
    async def statusclear(self, m):
        "Clear all custom statuses"
        self.set("s", self.default)
        await utils.answer(m, "<emoji document_id=5206607081334906820>✔️</emoji>")
