# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: HetaSearcher
# Description: Search a modules in @hikkamods_bot
# Author: skillzmeow
# Commands:
# .heta
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 2)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes
# meta pic: https://i.imgur.com/Q6TkhP2.jpeg
# meta banner: https://i.imgur.com/gwScaJj.jpeg

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils


class HetaSearcherMod(loader.Module):
    """search a modules in @hikkamods_bot"""

    strings = {"name": "HetaSearcher", "mod": "<b>👇 Probably this module</b>"}
    string_ru = {"mod": "<b>👇 Вероятно, это этот модуль</b>"}

    async def hetacmd(self, event):
        "<module name>"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("hikkamods_bot", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("mod"))
