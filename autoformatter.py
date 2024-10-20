# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: autoformatter
# Author: sqlmerr
# Commands:
# .textformat
# ---------------------------------------------------------------------------------

# ░██████╗░██████╗░██╗░░░░░███╗░░░███╗███████╗██████╗░██████╗░
# ██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔════╝██╔══██╗██╔══██╗
# ╚█████╗░██║██╗██║██║░░░░░██╔████╔██║█████╗░░██████╔╝██████╔╝
# ░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗
# ██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║
# ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
# ---------------------------------------------------------------------------------------------
# Name: AutoFormatter
# Description: Automatically formats the text of your messages | Автоматически форматирует текст ваших сообщений | Check The Config | Загляните в конфиг
# Author: sqlmerr
# Commands:
# .textformat
# ---------------------------------------------------------------------------------------------

# версия модуля
# meta banner: https://github.com/sqlmerr/sqlmerr/blob/main/assets/hikka_mods/sqlmerrmodules_autoformatter.png?raw=true
# meta developer: @sqlmerr_m
# only hikka

# импортируем нужные библиотеки
import asyncio
import logging
import re

from telethon import events, functions, types
from telethon.tl.types import ChatAdminRights, Message

from .. import loader, utils

logger = logging.getLogger(__name__)


# сам класс модуля
@loader.tds
class AutoFormatter(loader.Module):
    """Automatically formats the text of your messages | Check The Config"""

    # нужные переменные
    strings = {
        "name": "AutoFormatter",
        "status": "Module enabled or disabled",
        "format": "Text format. Where {} is the original message text",
        "type": "Formatting Type",
        "exceptions": "This is exceptions, this text is not formated",
        "disabled": "Module is now disabled",
        "enabled": "Module is now enabled",
    }
    strings_ru = {
        "status": "Включен или выключен модуль",
        "format": "Формат текста. Где {} это исходный текст сообщения",
        "type": "Тип форматирования",
        "exceptions": "Это исключения, этот текст не будет форматироваться",
        "disabled": "Модуль сейчас выключен",
        "enabled": "Модуль сейчас включен",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "status",
                False,
                lambda: self.strings("status"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "format",
                "<b>{}</b>",
                lambda: self.strings("format"),
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "exceptions",
                [],
                lambda: self.strings("exceptions"),
                validator=loader.validators.Series(loader.validators.String()),
            ),
            loader.ConfigValue(
                "type",
                "send_new",
                lambda: self.strings("type"),
                validator=loader.validators.Choice(["send_new", "edit"]),
            ),
        )

    @loader.watcher(
        only_messages=True,
        no_commands=True,
        no_stickers=True,
        no_docs=True,
        no_audios=True,
        no_videos=True,
        no_photos=True,
        no_forwards=True,
    )
    async def watcher(self, message):
        if not self.config["status"]:
            return

        reply = await message.get_reply_message()
        exc = self.config["exceptions"]
        if message.from_id == self._tg_id:
            f = self.config["format"]
            text = message.text
            if exc != [None]:
                for e in exc:
                    if str(e).strip() == text.strip():
                        return
            else:
                if f in text:
                    return

            if self.config["type"] == "send_new":
                await message.delete()
                if reply:
                    await self.client.send_message(
                        message.to_id, f"{f.format(text)}", reply_to=reply
                    )
                else:
                    await self.client.send_message(message.to_id, f"{f.format(text)}")
            elif self.config["type"] == "edit":
                await utils.answer(message, f"{f.format(text)}")

    @loader.command(ru_doc="Включить/выключить модуль")
    async def textformat(self, message: Message):
        """Turn on/off The Module"""
        self.config["status"] = not self.config["status"]
        enable = self.strings("enabled")
        disable = self.strings("disabled")
        status = (
            f"<emoji document_id=5447644880824181073>⚠️</emoji> {enable}"
            if self.config["status"]
            else f"<emoji document_id=5447644880824181073>⚠️</emoji> {disable}"
        )

        await utils.answer(message, "<b>{}</b>".format(status))
