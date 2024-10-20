# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: random_tools
# Description: Random tools
# Author: CakesTwix
# Commands:
# .mac2vendor | .onept | .np
# ---------------------------------------------------------------------------------


"""

    █▀▀ ▄▀█ █▄▀ █▀▀ █▀ ▀█▀ █░█░█ █ ▀▄▀
    █▄▄ █▀█ █░█ ██▄ ▄█ ░█░ ▀▄▀▄▀ █ █░█

    Copyleft 2022 t.me/CakesTwix                                                            
    This program is free software; you can redistribute it and/or modify 

"""

__version__ = (1, 1, 0)

# meta pic: https://i0.wp.com/alliancestake.org/wp-content/uploads/2017/09/icon-circle-tools-blue-1.png?fit=300%2C300&ssl=1
# meta developer: @cakestwix_mods

import asyncio
import logging

import aiohttp

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.unrestricted
@loader.ratelimit
@loader.tds
class RToolsMod(loader.Module):
    """Random tools"""

    strings = {
        "name": "Tools",
        "no_found": "No found",
        "no_args": "Not found args, pls check help",
        "general_error": "Oh no, cringe, error",
    }

    strings_ru = {
        "no_found": "Не найдено",
        "no_args": "Аргументы не найдены, пожалуйста, проверьте справку",
        "general_error": "❗️Ашибка❗️ ",
    }

    @loader.unrestricted
    @loader.ratelimit
    async def mac2vendorcmd(self, message):
        """Get vendor name by mac"""
        if args := utils.get_args(message):
            mac = args[0].lower()
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://api.macvendors.com/{mac}") as get:
                    if get.ok:
                        await utils.answer(message, await get.text())
                    else:
                        await utils.answer(message, self.strings["no_found"])
                        await asyncio.sleep(5)
                        await message.delete()
        else:
            await utils.answer(message, self.strings["no_args"])
            await asyncio.sleep(5)
            await message.delete()

    @loader.unrestricted
    @loader.ratelimit
    async def oneptcmd(self, message):
        """A simple URL shortener (1pt.co)"""
        if args := utils.get_args(message):
            mac = args[0].lower()
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.1pt.co/addURL?long={mac}") as get:
                    if get.ok:
                        answer_json = await get.json()
                        await utils.answer(message, "1pt.co/" + answer_json["short"])
                    else:
                        await utils.answer(message, self.strings["general_error"])
                        await asyncio.sleep(5)
                        await message.delete()
        else:
            await utils.answer(message, self.strings["no_args"])
            await asyncio.sleep(5)
            await message.delete()

    @loader.unrestricted
    @loader.ratelimit
    async def npcmd(self, message):
        """Нова Пошта"""
        if args := utils.get_args(message):
            document_number = args[0].lower()

            data = {
                "apiKey": "abe3a74549c55e4b703ed042c5169406",
                "modelName": "TrackingDocument",
                "calledMethod": "getStatusDocuments",
                "methodProperties": {
                    "Documents": [{"DocumentNumber": document_number, "Phone": ""}]
                },
            }

            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://api.novaposhta.ua/v2.0/json/", json=data
                ) as get:
                    answer = await get.json()
                    await session.close()
            item = answer["data"][0]

            caption = f"Экспресс-накладная: {item['Number']}"
            caption += f"\nСтатус: {item['Status']}"
            if "DateCreated" in item:
                caption += f"\nБыло создано: {item['DateCreated']}"
                caption += f"\nОжид. дата доставки: {item['ScheduledDeliveryDate']}"
                caption += f"\n{item['CitySender']} -> {item['CityRecipient']}"

            if item.get("DocumentCost") is not None:
                caption += f"\nЦена доставки: {item['DocumentCost']} грн."

            await utils.answer(message, caption)
