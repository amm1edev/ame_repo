# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: DoYouKnowAlphabet
# Author: dorotorothequickend
# Commands:
# .alphabetru | .consonantorvowel | .letterinfo | .alphabeteng
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroDoYouKnowAlphabet.png
# meta developer: @DorotoroMods

import re

from .. import loader, utils

vowel = ["a", "а", "е", "e", "ë", "и", "u", "o", "о", "i", "я", "у", "y", "э", "ы", "ю"]
bublik = ["ь", "ъ"]
myagkie = ["й", "ч", "щ"]
alwaystverdie = ["ш", "ж", "ц"]
nevsegdatverd = [
    "б",
    "в",
    "г",
    "д",
    "з",
    "к",
    "л",
    "м",
    "н",
    "х",
    "п",
    "р",
    "с",
    "т",
    "ф",
]
zvonk = ["б", "в", "г", "д", "ж", "з", "й", "л", "м", "н", "р"]
neslishu = ["к", "п", "ш", "щ", "с", "т", "ф", "х", "ц", "ч"]
parnie = ["б", "п", "в", "г", "к", "д", "т", "ж", "ш", "з", "с", "ф", "щ"]
neparn = ["х", "ц", "ч", "р", "н", "м", " й", "л"]
sonor = ["л", "р", "н", "й", "м"]
consonant = [
    "б",
    "в",
    "г",
    "д",
    "ж",
    "з",
    "й",
    "к",
    "л",
    "м",
    "н",
    "ш ",
    "щ",
    "х",
    "п",
    "р",
    "с",
    "т",
    "ф",
    "ц",
    "ч",
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    " k",
    "j",
    "l",
    "m",
    " n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]
prefix = "<b>///Информация о Букве </b>\n"


@loader.tds
class Alphabet(loader.Module):
    """Special for Kids."""

    strings = {"name": "DoYouKnowAlphabet?"}

    @loader.command()
    async def alphabetru(self, m):
        "- узнать русский алфавит."
        await utils.answer(
            m,
            (
                "<code> а, б, в, г, д, е, ë, ж, з, и, й, к, л, м, н, о, п, р, с, т, у,"
                " ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я </code>"
            ),
        )

    @loader.command()
    async def consonantorvowel(self, m):
        "<буква> - узнать, гласная или согласная буква."
        args = utils.get_args_raw(m)
        for letter in vowel:
            if args == letter:
                await utils.answer(m, f"{prefix}Буква <b>{args}</b> - гласная.")
                return
        for letter in consonant:
            if args == letter:
                await utils.answer(m, f"{prefix}Буква <b>{args}</b> - согласная.")

    @loader.command()
    async def letterinfo(self, m):
        "<буква> - показывает информацию о букве."
        args = utils.get_args_raw(m)
        letter = args
        text = f"{prefix}Буква <b>{args}</b>:\n"
        if args in consonant:
            text = f"{prefix}Буква <b>{args}</b>:\n Согласная\n"
        elif letter in myagkie:
            text = f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда мягкая\n"

        if letter in alwaystverdie:
            text = f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твёрдая\n"
        if letter in nevsegdatverd:
            text = f"{prefix}Буква <b>{args}</b>:\n Согласная\n Твёрдая\n"
        if letter in neslishu and letter in myagkie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда мягкая\n Глухая\n"
            )
        if letter in nevsegdatverd:
            text = f"{prefix}Буква <b>{args}</b>:\n Согласная\n Твёрдая\n"
        if letter in zvonk and letter in nevsegdatverd:
            text = f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Звонкая\n"
        if letter in neslishu and letter in nevsegdatverd:
            text = f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Глухая\n"
        if letter in neslishu and letter in alwaystverdie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Глухая\n"
            )
        if letter in zvonk and letter in alwaystverdie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Звонкая\n"
            )
        if letter in neslishu and letter in alwaystverdie and letter in parnie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Глухая\n"
                " Парная\n"
            )
        if letter in neslishu and letter in nevsegdatverd and letter in parnie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Глухая\n Парная\n"
            )
        if letter in neslishu and letter in alwaystverdie and letter in neparn:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Глухая\n"
                " Непарная\n"
            )
        if letter in neslishu and letter in nevsegdatverd and letter in neparn:
            text = (
                f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Глухая\n"
                " Непарная\n"
            )
        if letter in zvonk and letter in nevsegdatverd and letter in parnie:
            text = f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Парная\n"
        if letter in zvonk and letter in nevsegdatverd and letter in neparn:
            text = (
                f"{prefix}Буква <b>{args}</b>:\nСогласная\n Твердая\n Звонкая\n"
                " Непарная"
            )
        if letter in zvonk and letter in alwaystverdie and letter in neparn:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Звонкая\n"
                " Непарная\n"
            )
        if letter in zvonk and letter in alwaystverdie and letter in parnie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Звонкая\n"
                " Парная\n"
            )
        if letter in zvonk and letter in myagkie and letter in neparn:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда мягкая\n Звонкая\n"
                " Непарная\n\n <b>Всегда мягкие буквы: 'й', 'ч', 'щ'. Буква Й немного"
                " баганная, а в других может не быть пункта ПАРНЫЙ/НЕПАРНЫЙ</b>"
            )
        if letter in zvonk and letter in alwaystverdie and letter in parnie:
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Всегда твëрдая\n Звонкая\n"
                " Парная\n"
            )
        await utils.answer(m, text)

        if letter in vowel:
            text = f"{prefix}Буква <b>{args}</b>:\n Гласная\n"
            await utils.answer(m, text)
        if letter in bublik:
            text = f"{prefix}Буква <b>{args}</b>:\n Звука не обозначает "
            await utils.answer(m, text)
        if letter not in args:
            await utils.answer("<b>Введи букву, чорт.</b>")
        if letter == "р":
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Сонорная\n Непарная\n"
                " Звонкая\n Твёрдая"
            )
            await utils.answer(m, text)
        if letter == "л":
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Сонорная\n Непарная\n"
                " Звонкая\n Твёрдая"
            )
            await utils.answer(m, text)
        if letter == "н":
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Сонорная\n Непарная\n"
                " Звонкая\n Твёрдая"
            )
            await utils.answer(m, text)
        if letter == "й":
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Сонорная\n Непарная\n"
                " Звонкая\n Всегда мягкая"
            )
            await utils.answer(m, text)
        if letter == "м":
            text = (
                f"{prefix}Буква <b>{args}</b>:\n Согласная\n Сонорная\n Непарная\n"
                " Звонкая\n Твёрдая"
            )
            await utils.answer(m, text)

    @loader.command()
    async def alphabeteng(self, m):
        "- узнать английский алфавит."
        await utils.answer(
            m,
            (
                "<code> a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u,"
                " v, w, x, y, z </code>"
            ),
        )
