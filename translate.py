# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: translate
# Description: 🔡 Module for text translation
# ➡️ .tr en ru | Hello World
# ➡️ .tr ru | Hello World
# ➡️ .tr ru + reply to message
# Author: CakesTwix
# Commands:
# .atr | .itr | .gtr | .ltr
# ---------------------------------------------------------------------------------


"""

    █▀▀ ▄▀█ █▄▀ █▀▀ █▀ ▀█▀ █░█░█ █ ▀▄▀
    █▄▄ █▀█ █░█ ██▄ ▄█ ░█░ ▀▄▀▄▀ █ █░█

    Copyleft 2022 t.me/CakesTwix                                                            
    This program is free software; you can redistribute it and/or modify 

"""

__version__ = (2, 0, 0)

# meta pic: https://img.icons8.com/color/512/40C057/translate-text.png
# meta developer: @cakestwix_mods
# requires: translators

import asyncio
import logging

import aiohttp
import translators as trl

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.unrestricted
@loader.ratelimit
@loader.tds
class TranslatorMod(loader.Module):
    """
    🔡 Module for text translation
    ➡️ .tr en ru | Hello World
    ➡️ .tr ru | Hello World
    ➡️ .tr ru + reply to message
    """

    strings = {
        "name": "🔡 Translator",
        "cfg_lingva_url": "Alternative front-end for Google Translate",
        "error": "Error!\n .gtr [en] ru | text or check help",
    }

    strings_ru = {
        "cfg_lingva_url": "Альтернативный интерфейс для Google Translate",
        "error": "Ошибка!\n .gtr [en] ru | текст или проверьте хелп",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "lingva_url",
            "https://lingva.ml/api/v1/{source}/{target}/{query}",
            lambda m: self.strings("cfg_lingva_url", m),
        )
        self.name = self.strings["name"]

    async def tr(self, message, translator):
        if args := utils.get_args_raw(message):
            lang_args = args.split("|")[0].split()  # Lang
            if reply := await message.get_reply_message():
                if reply.message == "":
                    return await utils.answer(message, self.strings["error"])
                if len(lang_args) == 2:
                    translated_text = translator(
                        reply.message,
                        from_language=lang_args[0],
                        to_language=lang_args[1],
                    )
                    return await utils.answer(message, translated_text)
                elif len(lang_args) == 1:
                    translated_text = translator(
                        reply.message, to_language=lang_args[0]
                    )
                    return await utils.answer(message, translated_text)
                else:
                    await utils.answer(message, self.strings["error"])
                    await asyncio.sleep(5)
                    await message.delete()
                    return

            text_args = args.split("|")[1]  # Text
            if len(lang_args) == 2 and text_args:
                translated_text = translator(
                    text_args, from_language=lang_args[0], to_language=lang_args[1]
                )
            elif len(lang_args) == 1 and text_args:
                translated_text = translator(text_args, to_language=lang_args[0])
            else:
                await utils.answer(message, self.strings["error"])
                await asyncio.sleep(5)
                await message.delete()
                return

            await utils.answer(message, translated_text)
        else:
            await utils.answer(message, self.strings["error"])
            await asyncio.sleep(5)
            await message.delete()

    async def atrcmd(self, message):
        """
        Based on Argos (LibreTranslate)
        """
        await self.tr(message, trl.argos)

    async def itrcmd(self, message):
        """
        Based on Iciba
        """
        await self.tr(message, trl.iciba)

    async def gtrcmd(self, message):
        """
        Based on Google Translate
        """
        await self.tr(message, trl.google)

    async def ltrcmd(self, message):
        """
        Based on lingva.ml (Google Translate)
        """
        if args := utils.get_args_raw(message):
            lang_args = args.split("|")[0].split()  # Lang
            text_args = args.split("|")[1]  # Text
            if len(lang_args) == 2 and text_args:
                url = self.config["lingva_url"].format(
                    source=lang_args[0], target=lang_args[1], query=text_args
                )
            elif len(lang_args) == 1 and text_args:
                url = self.config["lingva_url"].format(
                    source="auto", target=lang_args[0], query=text_args
                )
            else:
                await utils.answer(message, self.strings["error"])
                await asyncio.sleep(5)
                await message.delete()
                return

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as get:
                    translated_text = await get.json()
                    await session.close()

            await utils.answer(message, translated_text["translation"])
        else:
            await utils.answer(message, self.strings["error"])
            await asyncio.sleep(5)
            await message.delete()
