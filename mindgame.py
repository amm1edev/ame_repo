# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: mindgame
# Author: hikariatama
# Commands:
# .mindgame
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.dan.tatar/mindgame_icon.png
# meta banner: https://mods.hikariatama.ru/badges/mindgame.jpg
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

import random

import grapheme
from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall

EMOJIES = utils.chunks(
    list(
        grapheme.graphemes(
            "😌☺️😞😔🧑‍🏫👨‍🏫👨‍💻🧑‍💻"
            "🤵‍♂️🤵👩‍🚀🧑‍🚀👨‍🚒🧑‍🚒👨‍⚖️🧑‍⚖️"
            "🧟🧟‍♀️🦹🦹‍♀️🌇🌆🦸🦸‍♂️"
            "🧙🧙‍♀️🧚🧚‍♂️👯‍♀️👯👭👫"
            "👨‍👩‍👦👨‍👩‍👧👨‍🏭🧑‍🏭👳👳‍♂️🧑👨"
            "🕵️🕵️‍♂️🧑‍🌾👨‍🌾👨‍⚕️🧑‍⚕️🕵️🕵️‍♂️"
            "👨‍🍳🧑‍🍳🧑‍🔬👨‍🔬🧝‍♀️🧝‍♂️💏👨‍❤️‍💋‍👨"
        )
    ),
    2,
)


@loader.tds
class MindGameMod(loader.Module):
    """Train your brain and mind"""

    strings = {
        "name": "MindGame",
        "header": (
            "🎮 <b>Find an emoji, that differs from others</b>\n<i>You've completed {}"
            " levels!</i>"
        ),
    }

    strings_ru = {
        "header": (
            "🎮 <b>Найди эмодзи, который отличается от других</b>\n<i>Ты прошел {}"
            " уровней!</i>"
        )
    }

    _ratelimit = []

    def generate_markup(self, counter: int) -> list:
        fail_emoji, next_step_emoji = random.choice(EMOJIES)
        markup = [
            {"text": fail_emoji, "callback": self._incorrect} for _ in range(8**2 - 1)
        ] + [
            {
                "text": next_step_emoji,
                "callback": self._next_step_callback,
                "args": (counter + 1,),
            }
        ]
        random.shuffle(markup)
        return utils.chunks(markup, 8)

    async def mindgamecmd(self, message: Message):
        """Open a new mindgame"""
        await self.inline.form(
            message=message,
            text=self.strings("header").format(0),
            reply_markup=self.generate_markup(0),
            disable_security=True,
        )

    async def _next_step_callback(self, call: InlineCall, counter: int):
        if call.from_user.id != self._tg_id and call.from_user.id in self._ratelimit:
            await call.answer("You've spent your chance...")
            return

        await call.edit(
            self.strings("header").format(counter),
            self.generate_markup(counter),
        )

        await call.answer("Correct!")

        self._ratelimit = []

    async def _incorrect(self, call: InlineCall):
        if call.from_user.id != self._tg_id:
            if call.from_user.id in self._ratelimit:
                await call.answer("You've spent your chance...")
                return

            self._ratelimit += [call.from_user.id]

        await call.answer("NO!")
