# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: tagall
# Description: Тэгает всех в чате.
# Author: Fl1yd
# Commands:
# .tagall
# ---------------------------------------------------------------------------------


import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(TagAllMod())


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


class TagAllMod(loader.Module):
    """Тэгает всех в чате."""

    strings = {"name": "TagAll"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "DEFAULT_MENTION_MESSAGE",
            "говно залупное\n                пашет.",
            "Default message of mentions",
        )
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    async def tagallcmd(self, message):
        """Используй .tagall <текст (по желанию)>."""
        arg = utils.get_args_raw(message)
        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append(
                '<a href="tg://user?id=' + str(user.id) + '">\u206c\u206f</a>'
            )
        chunkss = list(chunks(notifies, 5))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(
                message.to_id,
                (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg)
                + "\u206c\u206f".join(chunk),
            )
