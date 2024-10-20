# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: TelethonChatManager
# Author: DarkModules
# Commands:
# .trus  | .teng | .task    | .tlearn | .tofftop
# .tlogs | .trtd | .treport | .tv1    | .tspam
# ---------------------------------------------------------------------------------

# The MIT License (MIT)
# Copyright (c) 2022 penggrin

# meta developer: @penggrinmods
# scope: hikka_only

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class TelethonChatManager(loader.Module):
    """Basic Telethon Chat Manager"""

    strings = {
        "name": "TelethonChatManager",
    }

    def list_to_str(self, a=None):
        if (a is None) or (len(a) < 1):
            return ""

        return " ".join(str(b) for b in a)

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "delete_cmds",
                True,
                lambda: "Delete the messages TelethonChat-Manager sends?",
                validator=loader.validators.Boolean(),
            ),
        )

    async def __telethoncommand(
        self, command: str, message, force_reply=None, delete_result=True, use_args=True
    ):
        reply = await message.get_reply_message() or force_reply
        if use_args:
            args = self.list_to_str(utils.get_args(message))
        else:
            args = ""
        if reply:
            result = await reply.reply(f"{command} {args}")
        else:
            result = await message.respond(f"{command} {args}")
        await message.delete()
        if delete_result and self.config["delete_cmds"]:
            await result.delete()
        # return result

    @loader.command(ru_doc="- Подсказать пользователю что русский чат существует")
    async def truscmd(self, message):
        """- Say to a user that russian chat exists"""
        await utils.answer(
            message,
            "Just so you know, there is a Russian Telethon Chat\n@TelethonRussian",
        )

    @loader.command(
        ru_doc=(
            "- Уведомить пользователя что в этом чате нужно общатся только на"
            " английском"
        )
    )
    async def tengcmd(self, message):
        """- Say to a user that they should speak english"""
        await utils.answer(message, "Please speak English!")

    @loader.command(ru_doc="- Уведомить пользователя о том что его вопрос хуета")
    async def taskcmd(self, message):
        """- Say to a user that they should learn how to ask questions"""
        await self.__telethoncommand("#ask", message)

    @loader.command(
        ru_doc="- Уведомить пользователя о том что он нихуя не шарит в пайтоне"
    )
    async def tlearncmd(self, message):
        """- Say to a user that they need to learn python"""
        await self.__telethoncommand("#learn", message)

    @loader.command(ru_doc="- Уведомить пользователя о том что он тут нельзя оффтопить")
    async def tofftopcmd(self, message):
        """- Say to a user that you cant offtop here"""
        await self.__telethoncommand("#ot", message)

    @loader.command(
        ru_doc="- Уведомить пользователя о том что ему нужно включить логгинг"
    )
    async def tlogscmd(self, message):
        """- Say to a user that they need to enable logging"""
        await self.__telethoncommand("#logs", message)

    @loader.command(
        ru_doc="- Уведомить пользователя о том что ему нужно прочитать документацию"
    )
    async def trtdcmd(self, message):
        """- Say to a user that they need to read the docs"""
        await self.__telethoncommand("#rtd", message)

    @loader.command(ru_doc="<user OR reply> - Пожаловаться на пользователя")
    async def treportcmd(self, message):
        """<user OR reply> - Report a user"""
        await self.__telethoncommand("#report", message)

    @loader.command(
        ru_doc="- Уведомить пользователя о том что то что ему нужно нету в V1"
    )
    async def tv1cmd(self, message):
        """- Say to a user that the thing he wants is not in V1 yet"""
        await self.__telethoncommand("#v1", message)

    @loader.command(ru_doc="- Уведомить пользователя о том что спамерам тут не рады")
    async def tspamcmd(self, message):
        """- Say to a user that spammers are not welcomed here"""
        await self.__telethoncommand("#spam", message)
