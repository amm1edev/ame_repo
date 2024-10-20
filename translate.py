# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU GPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: translate
# Description: Translator
# Author: HitaloSama
# Commands:
# .translate
# ---------------------------------------------------------------------------------


#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging

from Yandex import Translate

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class TranslateMod(loader.Module):
    """Translator"""

    strings = {
        "name": "Translator",
        "translated": (
            "<b>From: </b><code>{from_lang}</code>"
            "\n<b>To: </b><code>{to_lang}</code>\n\n{output}"
        ),
        "invalid_text": "Invalid text to translate",
        "doc_default_lang": "Language to translate to by default",
        "doc_api_key": "API key from https://translate.yandex.com/developers/keys",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "DEFAULT_LANG",
            "en",
            lambda m: self.strings("doc_default_lang", m),
            "API_KEY",
            "",
            lambda m: self.strings("doc_api_key", m),
        )

    def config_complete(self):
        self.tr = Translate(self.config["API_KEY"])

    @loader.unrestricted
    @loader.ratelimit
    async def translatecmd(self, message):
        """.translate [from_lang->][->to_lang] <text>"""
        args = utils.get_args(message)

        if len(args) == 0 or "->" not in args[0]:
            text = " ".join(args)
            args = ["", self.config["DEFAULT_LANG"]]
        else:
            text = " ".join(args[1:])
            args = args[0].split("->")

        if len(text) == 0 and message.is_reply:
            text = (await message.get_reply_message()).message
        if len(text) == 0:
            await utils.answer(message, self.strings("invalid_text", message))
            return
        if args[0] == "":
            args[0] = self.tr.detect(text)
        if len(args) == 3:
            del args[1]
        if len(args) == 1:
            logging.error(
                "python split() error, if there is -> in the text, it must split!"
            )
            raise RuntimeError()
        if args[1] == "":
            args[1] = self.config["DEFAULT_LANG"]
        args[0] = args[0].lower()
        logger.debug(args)
        translated = self.tr.translate(text, args[1], args[0])
        ret = self.strings("translated", message).format(
            from_lang=utils.escape_html(args[0]),
            to_lang=utils.escape_html(args[1]),
            output=utils.escape_html(translated),
        )
        await utils.answer(message, ret)
