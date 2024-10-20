# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: addlinktosymbols
# Author: sqlmerr
# Commands:
# .addlinktosymbols
# ---------------------------------------------------------------------------------

"""
░██████╗░██████╗░██╗░░░░░███╗░░░███╗███████╗██████╗░██████╗░
██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔════╝██╔══██╗██╔══██╗
╚█████╗░██║██╗██║██║░░░░░██╔████╔██║█████╗░░██████╔╝██████╔╝
░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗
██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║
╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
"""
# meta developer: @sqlmerr_m
# meta banner: https://github.com/sqlmerr/hikka_mods/blob/main/assets/sqlmerrmodules_example.png?raw=true

import asyncio

from telethon import events, functions, types
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class AddLinkToSymbols(loader.Module):
    """Add link to symbols in text | Добавить ссылку на определённые символы в тексте"""

    strings = {
        "name": "AddLinkToSymbols",
        "noargs": (
            "<emoji document_id=5240241223632954241>🚫</emoji> <b>You didn't enter any"
            " arguments</b>"
        ),
        "IndexError": (
            "<emoji document_id=5431571841892228467>😟</emoji> <b>You have entered too"
            " few arguments</b>"
        ),
        "wait": (
            "<emoji document_id=5411225014148014586>🔴</emoji> <b>Please wait a"
            " second...</b>"
        ),
        "none": "<emoji document_id=5210952531676504517>❌</emoji> <b>ERROR</b>",
    }

    strings_ru = {
        "noargs": (
            "<emoji document_id=5240241223632954241>🚫</emoji> <b>Вы не ввели"
            " аргументы</b>"
        ),
        "IndexError": (
            "<emoji document_id=5431571841892228467>😟</emoji> <b>Вы ввели слишком мало"
            " аргументов</b>"
        ),
        "wait": (
            "<emoji document_id=5411225014148014586>🔴</emoji> <b>Подождите"
            " немного...</b>"
        ),
        "none": "<emoji document_id=5210952531676504517>❌</emoji> <b>ОШИБКА</b>",
    }

    @loader.command(
        ru_doc=(
            "[символы] [ссылка] [текст или реплай] Добавить ссылку на"
            " символы\n\nПример: .addlinktosymbols ап.ев https://example.com привет."
            " Еееее хай\nСимволы пишите без пробелов. "
        )
    )
    async def addlinktosymbols(self, m: Message):
        """
        [symbols] [link] [text or reply] Add link to symbols

        Example: .addlinktosymbols ah.e https://example.com hi hello. YOOOOOOO
        Write characters without spaces.
        """

        args = utils.get_args_raw(m).split()
        if not args:
            return await utils.answer(m, self.strings("noargs"))
        reply = await m.get_reply_message()

        try:
            symbols = args[0]
            link = args[1]
            text = args[2:]
            if reply is not None:
                text = reply.raw_text
        except IndexError:
            return await utils.answer(m, self.strings("IndexError"))
        await utils.answer(m, self.strings("wait"))
        txt = ""
        for t in text:
            if reply:
                txt += t
            else:
                txt += t + " "

        real_txt = ""
        for _ in range(len(txt)):
            if txt[_] in symbols:
                symbol = txt[_]
                real_txt += f'<a href="{link}">{symbol}</a>'
            else:
                real_txt += txt[_]
        if real_txt is None:
            return await utils.answer(m, self.strings("none"))
        await utils.answer(m, real_txt)
