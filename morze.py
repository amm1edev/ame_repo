# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: morze
# Description: Конвертация текста в шифр Морзе и наоборот.
#
# Символы использовать не советую, могут возникать ошибки!!
# Author: GeekTG
# Commands:
# .tomrz | .toabc
# ---------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

# Module author: @trololo_1

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MorzeMod(loader.Module):
    """Конвертация текста в шифр Морзе и наоборот.

    Символы использовать не советую, могут возникать ошибки!!"""

    strings = {"name": "Morze"}

    @loader.unrestricted
    async def tomrzcmd(self, message):
        """.tomrz [реплай или текст]"""
        de = {
            "А": "•- ",
            "Б": "-••• ",
            "В": "•-- ",
            "Г": "--• ",
            "Д": "-•• ",
            "Е": "• ",
            "Ё": "• ",
            "Ж": "•••- ",
            "З": "--•• ",
            "И": "•• ",
            "Й": "•--- ",
            "К": "-•- ",
            "Л": "•-•• ",
            "М": "-- ",
            "Н": "-• ",
            "О": "--- ",
            "П": "•--• ",
            "Р": "•-• ",
            "С": "••• ",
            "Т": "- ",
            "У": "••- ",
            "Ф": "••-• ",
            "Х": "•••• ",
            "Ц": "-•-• ",
            "Ч": "---• ",
            "Ш": "---- ",
            "Щ": "--•- ",
            "Ъ": "--•-- ",
            "Ы": "-•-- ",
            "Ь": "-••- ",
            "Э": "••-•• ",
            "Ю": "••-- ",
            "Я": "•-•- ",
            "1": "•---- ",
            "2": "••--- ",
            "3": "•••-- ",
            "4": "••••- ",
            "5": "••••• ",
            "6": "-•••• ",
            "7": "--••• ",
            "8": "---•• ",
            "9": "----• ",
            "0": "----- ",
            ".": "•••••• ",
            ",": "•-•-•- ",
            ";": "-•-•-• ",
            ":": "---••• ",
            "?": "••--•• ",
            "!": "--••-- ",
            "-": "-••••- ",
            "(": "-•--• ",
            ")": "-•--•- ",
            "/": "-••-• ",
            '"': "•-••-• ",
            "+": "•-•-• ",
            "_": "••--•- ",
            "$": "•••-••- ",
            "@": "•--•-• ",
            "=": "-•••- ",
            "&": "•-••• ",
        }

        reply = await message.get_reply_message()
        text = utils.get_args_raw(message)

        if reply and not text:
            text = reply.raw_text
        if not text:
            return await utils.answer(
                message, "<code>Вы не ввели текст или не сделали реплай.</code>"
            )
        x = ""
        for word in text.split():
            for letter in word.upper():
                x += de[letter]
            x += " "
        await message.edit(x)

    @loader.unrestricted
    async def toabccmd(self, message):
        """.toabc [реплай или текст]"""

        en = {
            "•-": "А",
            "-•••": "Б",
            "•--": "В",
            "--•": "Г",
            "-••": "Д",
            "•": "Е",
            "•••-": "Ж",
            "--••": "З",
            "••": "И",
            "•---": "Й",
            "-•-": "К",
            "•-••": "Л",
            "--": "М",
            "-•": "Н",
            "---": "О",
            "•--•": "П",
            "•-•": "Р",
            "•••": "С",
            "-": "Т",
            "••-": "У",
            "••-•": "Ф",
            "••••": "Х",
            "-•-•": "Ц",
            "---•": "Ч",
            "----": "Ш",
            "--•-": "Щ",
            "--•--": "Ъ",
            "-•--": "Ы",
            "-••-": "Ь",
            "••-••": "Э",
            "••--": "Ю",
            "•-•-": "Я",
            "•----": "1",
            "••---": "2",
            "•••--": "3",
            "••••-": "4",
            "•••••": "5",
            "-••••": "6",
            "--•••": "7",
            "---••": "8",
            "----•": "9",
            "-----": "0",
            "••••••": ".",
            "•-•-•-": ",",
            "-•-•-•": ";",
            "---•••": ":",
            "••--••": "?",
            "--••--": "!",
            "-••••-": "-",
            "-•--•-": ")",
            "-•--•": "(",
            "-••-•": "/",
            "•-••-•": '"',
            "•-•-•": "+",
            "••--•-": "_",
            "•••-••-": "$",
            "•--•-•": "@",
            "-•••-": "=",
            "•-•••": "&",
        }

        reply = await message.get_reply_message()
        text = utils.get_args_raw(message)

        if reply and not text:
            text = reply.raw_text
        if not text:
            return await utils.answer(
                message, "<code>Вы не ввели текст или не сделали реплай.</code>"
            )
        x = ""
        for word in text.split("  "):
            for letter in word.split():
                x += en[letter].lower()
            x += " "
        await message.edit(x)
