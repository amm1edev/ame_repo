# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: InlineButton
# Author: Codwizer
# Commands:
# Failed to parse
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Name: InlineButton
# Description: Create inline button
# Author: @hikka_mods
# ---------------------------------------------------------------------------------

# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @hikka_mods
# scope: InlineButton
# scope: InlineButton 0.0.1
# ---------------------------------------------------------------------------------
import asyncio

from .. import loader, utils
from ..inline.types import InlineQuery
from ..utils import rand


@loader.tds
class InlineButtonMod(loader.Module):
    """Create inline button"""

    strings = {
        "name": "InlineButton",
    }

    async def crinl_inline_handler(self, query: InlineQuery):
        """- создать inline кнопку\nНапример: @username_bot crinl Текст сообщения, Текст кнопки, Ссылка в кнопке"""

        args = utils.get_args_raw(query.query)
        if args:
            args_list = args.split(",")
            if len(args_list) == 3:
                message = args_list[0].strip()
                name = args_list[1].strip()
                url = args_list[2].strip()

            return {
                "title": "Создай сообщение с Inline Кнопкой",
                "description": f"{message}, {name}, {url}",
                "message": message,
                "reply_markup": [{"text": name, "url": url}],
            }
