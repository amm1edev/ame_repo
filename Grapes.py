# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Grapes
# Author: GD-alt
# Commands:
# .pic | .dpic
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
# meta developer: @mm_mods, original by Fl1yd
# meta pic: https://img.icons8.com/emoji/344/grapes-emoji.png

from random import choice
from time import sleep

from telethon import types
from telethon.tl.types import Message

from .. import loader, utils


class GrapesMod(loader.Module):
    """Searching for random pic for your query. Original version/idea: Fl1yd."""

    strings = {
        "name": "Grapes",
        "lade": "🔎 <b>Searching…</b>",
        "p-auf": "👾 <b>O0pS, pr0b1em…</b>",
        "n-gef": "<b>Ha, stop, not found… :(</b>",
        "gef": "<b>Looks like something is found!..</b>",
        "q": "Query:",
        "args?": "📝 <b>Where is arguments, sir?</b>",
    }

    strings_ru = {
        "name": "Grapes",
        "lade": "🔎 <b>Ищу…</b>",
        "p-auf": "👾 <b>0й, пр06лемkа…</b>",
        "n-gef": "<b>А, нет, не нашлось… :(</b>",
        "gef": "<b>Кажется, нашлось!..</b>",
        "q": "Запрос:",
        "args?": "📝 <b>И где аргументы, сударь?</b>",
    }

    async def piccmd(self, message: Message):
        """Searching for pics in Yandex."""
        try:
            args = utils.get_args_raw(message)
            if not args:
                await utils.answer(message, self.strings("args?"))
                return
            await utils.answer(message, self.strings("lade"))
            reslt = await message.client.inline_query("pic", args)
            await utils.answer(
                message, f'{self.strings("gef")}\n{self.strings("q")} {args}'
            )
            sleep(1.5)
            await message.delete()
            await reslt[reslt.index(choice(reslt))].click(utils.get_chat_id(m))
        except:
            await message.respond(self.strings("n-gef"))
            return

    async def dpiccmd(self, message: Message):
        """Searching for pics in DuckDuckGo."""
        try:
            args = utils.get_args_raw(message)
            if not args:
                await utils.answer(message, self.strings("args?"))
                return
            await utils.answer(message, self.strings("lade"))
            reslt = await message.client.inline_query("duckpicsbot", args)
            await utils.answer(
                message, f'{self.strings("gef")}\n{self.strings("q")} {args}'
            )
            sleep(1.5)
            await message.delete()
            await reslt[reslt.index(choice(reslt))].click(utils.get_chat_id(m))
        except:
            await message.respond(self.strings("n-gef"))
            return
