# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MineEVO-logging
# Author: sqlmerr
# Commands:
# .mlogging
# ---------------------------------------------------------------------------------

# ░██████╗░██████╗░██╗░░░░░███╗░░░███╗███████╗██████╗░██████╗░
# ██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔════╝██╔══██╗██╔══██╗
# ╚█████╗░██║██╗██║██║░░░░░██╔████╔██║█████╗░░██████╔╝██████╔╝
# ░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗
# ██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║
# ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
# ---------------------------------------------------------------------------------------------
# Name: MineEVO-logs
# Description: Полезный модуль для логгирования в боте @mine_evo_bot | Для работы поставьте в конфиге ваш ник
# Author: sqlmerr
# Commands:
# .mlogging
# ---------------------------------------------------------------------------------------------

# версия модуля
__version__ = (1, 0, 0)
# meta developer: @sqlmerr_m
# only hikka

# импортируем нужные библиотеки
import asyncio
import logging
import re

from telethon import events, functions, types
from telethon.tl.types import ChatAdminRights, Message

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


# сам класс модуля
@loader.tds
class MineEVO_logs(loader.Module):
    """Полезный модуль для логгирования в боте @mine_evo_bot | Для работы поставьте в конфиге ваш ник | И загляните в конфиг"""

    # нужные переменные
    strings = {
        "name": "MineEVO-logging",
        "status": "Включен ли модуль или нет",
        "nickname": "Ваш ник в боте (важно)",
        "logging": "То, что будет логгироваться",
    }

    async def client_ready(self):
        # создается чат
        self._mineevologs_channel, _ = await utils.asset_channel(
            self._client,
            "MineEVO-logs - чат",
            (
                "Не пишите сюда. Этот чат предназначет для модуля MineEVO-logs от"
                " @sqlmerr_m"
            ),
            silent=True,
            archive=True,
            _folder="hikka",
        )
        # в этот чат добавляется бот @mine_evo_bot
        await self.client(
            functions.channels.InviteToChannelRequest(
                self._mineevologs_channel, ["@mine_evo_bot"]
            )
        )
        # и этому боту выдаются права админа, для корректной работы бота
        await self.client(
            functions.channels.EditAdminRequest(
                channel=self._mineevologs_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(
                    ban_users=True, post_messages=True, edit_messages=True
                ),
                rank="MineEVO-logs",
            )
        )

    # функция, связанная с ООП и нужная для создания конфига
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "status",
                False,
                lambda: self.strings("status"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "logging",
                ["выкопанные_кейсы", "передачи_кейсов_тебе", "передачи_кейсов_от_тебя"],
                lambda: self.strings("logging"),
                validator=loader.validators.MultiChoice(
                    [
                        "выкопанные_кейсы",
                        "переводы_тебе",
                        "переводы_от_тебя",
                        "передачи_кейсов_тебе",
                        "передачи_кейсов_от_тебя",
                    ]
                ),
            ),
        )

    # .mlogging
    @loader.command()
    async def mlogging(self, message: Message):
        """Включить/выключить логгирование"""
        self.config["status"] = not self.config["status"]
        status = (
            "Логгирование включено <emoji document_id=5409048419211682843>💲</emoji>"
            if self.config["status"]
            else (
                "Логгирование выключено <emoji"
                " document_id=5409048419211682843>💲</emoji>"
            )
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

    @loader.watcher(only_messages=True, chat_id=5522271758)
    async def watcher(self, message: Message):
        if self.config["status"]:
            mined_cases = False
            perevod_me = False
            perevod_to = False
            peredacha_me = False
            peredacha_to = False
            for o in self.config["logging"]:
                if o == "выкопанные_кейсы":
                    mined_cases = True
                elif o == "переводы_тебе":
                    perevod_me = True
                elif o == "переводы_от_тебя":
                    perevod_to = True
                elif o == "передачи_кейсов_тебе":
                    peredacha_me = True
                elif o == "передачи_кейсов_от_тебя":
                    peredacha_to = True

            if mined_cases:
                if (
                    "✉️ Ты нашел(ла) конверт." in message.raw_text
                    or "🧧 Ты нашел(ла) редкий конверт." in message.raw_text
                    or "📦 Ты нашел(ла) Кейс!" in message.raw_text
                    or "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text
                    or "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text
                    or "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text
                    or "💫" in message.raw_text
                ):
                    await message.forward_to(self._mineevologs_channel)
                    # await self.client.send_message(self._mineevologs_channel, message.text)
            if perevod_me:
                if "перевел(а) тебе" in message.raw_text:
                    await message.forward_to(self._mineevologs_channel)
            if perevod_to:
                if "перевел(а) игроку" in message.raw_text:
                    await message.forward_to(self._mineevologs_channel)
            if peredacha_me:
                if "передал(а) тебе" in message.raw_text:
                    await message.forward_to(self._mineevologs_channel)
            if peredacha_to:
                if "передал(а) игроку" in message.raw_text:
                    await message.forward_to(self._mineevologs_channel)
