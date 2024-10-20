# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: FixReply
# Author: DarkModules
# Commands:
# .fixreply
# ---------------------------------------------------------------------------------

# The MIT License (MIT)
# Copyright (c) 2022 penggrin

# meta developer: @penggrinmods
# scope: hikka_only

import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class FixReplyMod(loader.Module):
    """Fixes ya replies"""

    strings = {
        "name": "FixReply",
        "no_message": "❎ I see no messages!",
        "no_reply": "❎ I see no reply!",
    }
    strings_ru = {
        "no_message": "❎ Чел ты ничего не писал!",
        "no_reply": "❎ Чел ты забыл ответить на нужное сообщение!",
    }

    lastMessage = None

    @loader.watcher(out=True, only_messages=True, no_commands=True)
    async def newMessage(self, message):
        self.lastMessage = message

    @loader.command(
        ru_doc=(
            "- Ответьте на сообщение этой командой чтобы починить ответ на своём"
            " последнем сообщении"
        )
    )
    async def fixreplycmd(self, message):
        """- Respond to a message to fix your last message reply"""
        reply = await message.get_reply_message()

        if not self.lastMessage:
            await utils.answer(message, self.strings("no_message"))
            return

        if not reply:
            await utils.answer(message, self.strings("no_reply"))
            return

        await utils.answer(message, self.lastMessage.raw_text)
        await self.lastMessage.delete()
