# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: searchpic
# Author: AmoreForever
# Commands:
# .spic
# ---------------------------------------------------------------------------------

# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Searchpic.jpg
# meta developer: @amoremods

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class SearchPic(loader.Module):
    strings = {"name": "SearchPic"}

    @loader.unrestricted
    async def spiccmd(self, message: Message):
        """Search picture"""
        text = utils.get_args_raw(message)
        await self.inline.form(
            message=message,
            text=f"🎑 Your pic found\n✍ Input argument: {text}",
            reply_markup=[
                [
                    {
                        "text": "Pic here",
                        "url": f"https://yandex.uz/images/touch/search/?text={text}",
                    }
                ],
                [{"text": "Close", "action": "close"}],
            ],
            **({"photo": f"https://yandex.uz/images/touch/search/?text={text}"}),
        )
