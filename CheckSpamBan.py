# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: CheckSpamBan
# Author: Codwizer
# Commands:
# .spamban
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Name: CheckSpamBan
# Description: Check spam ban for your account.
# Author: @hikka_mods
# ---------------------------------------------------------------------------------

# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikka_mods
# scope: CheckSpamBan
# scope: CheckSpamBan 0.0.1
# ---------------------------------------------------------------------------------

from telethon.tl.types import Message

from .. import loader, utils
from ..utils import answer


@loader.tds
class SpamBanCheckMod(loader.Module):
    """Check spam ban for your account."""

    strings = {
        "name": "CheckSpamBan",
    }

    @loader.command()
    async def spamban(self, message: Message):
        """- checks your account for spam ban via @SpamBot bot."""
        async with self._client.conversation("@SpamBot") as conv:
            msg = await conv.send_message("/start")
            r = await conv.get_response()
            if r.text == "Ваш аккаунт свободен от каких-либо ограничений.":
                text = "<b>Все прекрасно!\nУ вас нет спам бана.</b>"
            else:
                response_lines = r.text.split("\n")
                kk = response_lines[2]
                ll = response_lines[4]
                text = (
                    "<b>К сожалению ваш аккаунт получил"
                    f" спам-бан...\n\n{kk}\n\n{ll}</b>"
                )
            await msg.delete()
            await r.delete()
            await answer(message, text)
