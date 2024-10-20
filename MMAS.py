# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MMAS
# Author: GD-alt
# Commands:
# .mmas | .mmaslimit
# ---------------------------------------------------------------------------------

# `7MMM.     ,MMF'`7MMM.     ,MMF'   `7MMM.     ,MMF'              `7MM
# MMMb    dPMM    MMMb    dPMM       MMMb    dPMM                  MM
# M YM   ,M MM    M YM   ,M MM       M YM   ,M MM  ,pW"Wq.    ,M""bMM  ,pP"Ybd
# M  Mb  M' MM    M  Mb  M' MM       M  Mb  M' MM 6W'   `Wb ,AP    MM  8I   `"
# M  YM.P'  MM    M  YM.P'  MM mmmmm M  YM.P'  MM 8M     M8 8MI    MM  `YMMMa.
# M  `YM'   MM    M  `YM'   MM       M  `YM'   MM YA.   ,A9 `Mb    MM  L.   I8
# .JML. `'  .JMML..JML. `'  .JMML.   .JML. `'  .JMML.`Ybmd9'   `Wbmd"MML.M9mmmP'
#
# (c) 2023 — licensed under Apache 2.0 — https://www.apache.org/licenses/LICENSE-2.0

# meta pic: https://img.icons8.com/stickers/344/block.png
# meta developer: @mm_mods

__version__ = "1.0.0"

import asyncio
import logging

import telethon as tt
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MMASMod(loader.Module):
    """Protects your account from spam if anyone accessed your account/session."""

    strings = {
        "name": "MMAS",
        "found": "<b>Spam found!</b>\nText: <code>{}</code>",
        "limit_set": "<b>Limit set to {}</b>",
        "limit_get": "<b>Limit is {}</b>",
        "on": "<b>Enabled.</b>",
        "off": "<b>Disabled.</b>",
    }

    strings_ru = {
        "name": "MMAS",
        "found": "<b>Спам найден!</b>\nТекст: <code>{}</code>",
        "limit_set": "<b>Лимит установлен на {}</b>",
        "limit_get": "<b>Лимит равен {}</b>",
        "on": "<b>Включено.</b>",
        "off": "<b>Выключено.</b>",
        "_cls_doc": (
            "Защищает ваш аккаунт от спама, если кто-то получил доступ к вашей учетной"
            " записи/сеансу."
        ),
        "_cmd_doc_mmas": "Включить/выключить модуль.",
        "_cmd_doc_mmaslimit": (
            "Получить или установить лимит одинаковых сообщений, отправленных вами."
        ),
    }

    strings_de = {
        "name": "MMAS",
        "found": "<b>Spam gefunden!</b>\nText: <code>{}</code>",
        "limit_set": "<b>Limit auf {} gesetzt</b>",
        "limit_get": "<b>Limit ist {}</b>",
        "on": "<b>Aktiviert.</b>",
        "off": "<b>Deaktiviert.</b>",
        "_cls_doc": (
            "Schützt dein Konto vor Spam, wenn jemand auf dein Konto/zur Sitzung"
            " zugreift."
        ),
        "_cmd_doc_mmas": "Aktiviere/Deaktiviere das Modul.",
        "_cmd_doc_mmaslimit": (
            "Erhalte oder setze das Limit für die Anzahl der gleichen Nachrichten, die"
            " du gesendet hast."
        ),
    }

    strings_tr = {
        "name": "MMAS",
        "found": "<b>Spam bulundu!</b>\nMetin: <code>{}</code>",
        "limit_set": "<b>Sınır {} olarak ayarlandı</b>",
        "limit_get": "<b>Sınır {}</b>",
        "on": "<b>Açık.</b>",
        "off": "<b>Kapalı.</b>",
        "_cls_doc": "Hesabınızı kimse erişemezse spam koruması.",
        "_cmd_doc_mmas": "Modülü aç/kapat.",
        "_cmd_doc_mmaslimit": (
            "Aynı mesajı kaç kere gönderdiğinizi alın veya ayarlayın."
        ),
    }

    async def client_ready(self, client, db):
        self._client = client
        self._db = db
        if not self.get("limit", False):
            self.set("limit", 5)
        if not self.get("on", False):
            self.set("on", True)
        if not self.get("lat", False):
            self.set("lat", "")
        if not self.get("count", False):
            self.set("count", 0)
        if not self.get("logged", False):
            self.set("logged", False)

    async def mmascmd(self, message: Message):
        """Toggle the module."""
        if self.get("on", False):
            self.set("on", False)
            await utils.answer(message, self.strings("off"))
        else:
            self.set("on", True)
            await utils.answer(message, self.strings("on"))

    async def mmaslimitcmd(self, message: Message):
        """Get or set the limit of same messages sent by you."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(
                message, self.strings("limit_get").format(self.get("limit"))
            )
            return
        try:
            if int(args) < 2:
                await utils.answer(message, self.strings("limit_set").format(2))
                self.set("limit", 2)
                return
            self.set("limit", int(args))
            await utils.answer(
                message, self.strings("limit_set").format(self.get("limit"))
            )
        except ValueError:
            await utils.answer(
                message, self.strings("limit_get").format(self.get("limit"))
            )

    async def watcher(self, message: Message):
        if not self.get("on", False):
            return
        if not message.text:
            return
        if not message.out:
            return
        if message.raw_text != self.get("lat", False):
            self.set("lat", message.raw_text)
            self.set("count", 1)
            return
        else:
            self.set("count", self.get("count") + 1)
            if self.get("count") >= self.get("limit"):
                await message.delete()
                if not self.get("logged", False):
                    self.set("logged", True)
                    logging.warning(self.strings("found").format(message.raw_text))
                return
