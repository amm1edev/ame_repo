# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: CryptoSteal
# Author: DarkModules
# Commands:
# .cryptosteal
# ---------------------------------------------------------------------------------

# The MIT License (MIT)
# Copyright (c) 2023 penggrin

# █▀█ █▀▀ █▄░█ █▀▀ █▀▀ █▀█ █ █▄░█
# █▀▀ ██▄ █░▀█ █▄█ █▄█ █▀▄ █ █░▀█

# meta developer: @penggrinmods
# scope: hikka_only

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CryptoStealMod(loader.Module):
    """Automatically claims cryptobot checks"""

    strings = {
        "name": "CryptoSteal",
        "disabled": "❌ Disabled",
        "enabled": "✅ Enabled",
        "status_now": "👌 Crypto-Steal was <b>{}</b>!",
        "config_status": "Are we ready to steal?",
        "config_allow_every_bot": "If disabled will only steal CryptoBot checks",
    }

    strings_ru = {
        "disabled": "❌ Выключен",
        "enabled": "✅ Включён",
        "status_now": "👌 Crypto-Steal теперь <b>{}</b>!",
        "config_status": "Готовы ли мы тырить?",
        "config_allow_every_bot": (
            "Если выключено то я буду тырить только CryptoBot чеки"
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "status",
                True,
                lambda: self.strings("config_status"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "allow_every_bot",
                False,
                lambda: self.strings("config_status"),
                validator=loader.validators.Boolean(),
            ),
        )

    @loader.watcher(only_messages=True, only_inline=True)
    async def watcher(self, message):
        text = message.raw_text.lower()

        if not self.config["status"]:
            return
        if not (("check for " in text) or ("чек на " in text)):
            return
        url = message.buttons[0][0].url.split("?start=")

        if (not ("CryptoBot" in url[0])) and (not self.config["allow_every_bot"]):
            logger.debug("Ignoring not CryptoBot")
            return
        await self.client.send_message(url[0], f"/start {url[1]}")
        logger.info("Sent check get request, hopefully we got it")

    async def cryptostealcmd(self, message):
        """Toggle Crypto-Steal"""

        self.config["status"] = not self.config["status"]
        status = (
            self.strings("enabled")
            if self.config["status"]
            else self.strings("disabled")
        )

        await utils.answer(message, self.strings("status_now").format(status))
