# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Vizjener
# Description: Конвертация текста в шифр Виженеря и наоборот.
# Author: trololo65
# Commands:
# .toviz | .tounviz
# ---------------------------------------------------------------------------------


# meta developer: @trololo_1

import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class VijenerMod(loader.Module):
    """Конвертация текста в шифр Виженеря и наоборот."""

    strings = {"name": "Vizjener"}

    @loader.unrestricted
    async def tovizcmd(self, message):
        """.toviz {ключ} {текст}"""
        try:
            alphabet = [
                "",
                "а",
                "б",
                "в",
                "г",
                "д",
                "е",
                "ё",
                "ж",
                "з",
                "и",
                "й",
                "к",
                "л",
                "м",
                "н",
                "о",
                "п",
                "р",
                "с",
                "т",
                "у",
                "ф",
                "х",
                "ц",
                "ч",
                "ш",
                "щ",
                "ъ",
                "ы",
                "ь",
                "э",
                "ю",
                "я",
            ]
            text = utils.get_args_raw(message)
            key = str(text.split(" ")[0])
            shifr = str(text.split(" ", maxsplit=1)[1])
            key_list = []
            shifr_list = []
            for word in key.split():
                for letter in word.lower():
                    key_list.append(letter)
            for word in shifr.split():
                for letter in word.lower():
                    shifr_list.append(letter)
                shifr_list.append(" ")
            key_index = 0
            sms = ""
            for i in range(0, len(shifr_list)):
                if shifr_list[i].isalpha():
                    if key_index == len(key_list):
                        key_index = 0
                    a = alphabet.index(shifr_list[i])
                    b = alphabet.index(key_list[key_index])
                    result = int(a) + int(b)
                    if result >= 33:
                        result = result % 33
                    if result == 0:
                        result = 33
                    sms += alphabet[result]

                    key_index += 1
                else:
                    sms += shifr_list[i]
            await message.edit(sms)
        except:
            await message.edit(
                "<strong> ERROR. Возможно вы ввели некириллические символы, либо ввели"
                " в ключ что то кроме буквенных символов. </strong>"
            )

    @loader.unrestricted
    async def tounvizcmd(self, message):
        """.tounviz {ключ} {текст}"""
        try:
            alphabet = [
                "",
                "а",
                "б",
                "в",
                "г",
                "д",
                "е",
                "ё",
                "ж",
                "з",
                "и",
                "й",
                "к",
                "л",
                "м",
                "н",
                "о",
                "п",
                "р",
                "с",
                "т",
                "у",
                "ф",
                "х",
                "ц",
                "ч",
                "ш",
                "щ",
                "ъ",
                "ы",
                "ь",
                "э",
                "ю",
                "я",
            ]
            text = utils.get_args_raw(message)
            key = str(text.split(" ")[0])
            shifr = str(text.split(" ", maxsplit=1)[1])
            key_list = []
            shifr_list = []
            for word in key.split():
                for letter in word.lower():
                    key_list.append(letter)
            for word in shifr.split():
                for letter in word.lower():
                    shifr_list.append(letter)
                shifr_list.append(" ")
            key_index = 0
            sms = ""
            for i in range(0, len(shifr_list)):
                if shifr_list[i].isalpha():
                    if key_index == len(key_list):
                        key_index = 0
                    a = alphabet.index(shifr_list[i])
                    b = alphabet.index(key_list[key_index])
                    if int(b) == 33:
                        result = int(a) % int(b)
                    else:
                        result = int(a) - int(b)
                    if result < 0:
                        result = result - 1
                    if result == 0:
                        result = 33
                    sms += alphabet[result]
                    key_index += 1
                else:
                    sms += shifr_list[i]
            await message.edit(sms)
        except:
            await message.edit(
                "<strong> ERROR. Возможно вы ввели некириллические символы, либо ввели"
                " в ключ что то кроме буквенных символов. </strong>"
            )
