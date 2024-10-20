# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: GameInfo
# Author: N3rcy
# Commands:
# .gameinfo
# ---------------------------------------------------------------------------------

#    ╔╗╔┌─┐┬─┐┌─┐┬ ┬
#    ║║║├┤ ├┬┘│  └┬┘
#    ╝╚╝└─┘┴└─└─┘ ┴

# Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# https://creativecommons.org/licenses/by-nc-nd/4.0/
# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

# meta developer: @nercymods
# scope: hikka_min 1.6.2

import requests
from hikkatl.tl.types import Message

from .. import loader, utils


@loader.tds
class GameInfo(loader.Module):
    """Module for fetching game information from RAWG"""

    strings = {
        "name": "GameInfo",
        "game_not_found": "<b>❌ Game not found</b>",
        "fetching": "<b>🌐 Fetching game information...</b>",
        "no_api": (
            "<b>❌ Please insert your api key in config</b> (<code>.cfg GameInfo</code>)"
        ),
        "error_fetching": "<b>❌ Error fetching game information</b>",
        "game": "<b><emoji document_id=5467583879948803288>🎮</emoji>Name: </b>%s",
        "release": (
            "<b><emoji document_id=5431897022456145283>📆</emoji>Data released: </b>%s"
        ),
        "rawg_rating": (
            "<b><emoji document_id=5435957248314579621>⭐️</emoji>Rating: </b>%s"
        ),
        "platforms": (
            "<b><emoji document_id=5386764531152198851>🏴‍☠️</emoji>Platforms: </b>%s"
        ),
        "genres": "<b><emoji document_id=5188705588925702510>🎶</emoji>Genres: </b>%s",
        "screenshots": (
            "<b><emoji document_id=5818849313555483639>📸</emoji>Screenshots: </b>%s"
        ),
    }

    strings_ru = {
        "game_not_found": "<b>❌ Игра не найдена</b>",
        "fetching": "<b>🌐 Получение информации об игре...</b>",
        "no_api": (
            "<b>❌ Пожалуйста укажите api-ключ в конфиге (<code>.cfg GameInfo</code>)"
        ),
        "error_fetching": "<b>❌ Ошибка при получении информации об игре</b>",
        "game": "<b><emoji document_id=5467583879948803288>🎮</emoji>Название: </b>%s",
        "release": (
            "<b><emoji document_id=5431897022456145283>📆</emoji>Дата релиза: </b>%s"
        ),
        "rawg_rating": (
            "<b><emoji document_id=5435957248314579621>⭐️</emoji>Рейтинг: </b>%s"
        ),
        "platforms": (
            "<b><emoji document_id=5386764531152198851>🏴‍☠️</emoji>Платформы: </b>%s"
        ),
        "genres": "<b><emoji document_id=5188705588925702510>🎶</emoji>Жанры: </b>%s",
        "screenshots": (
            "<b><emoji document_id=5818849313555483639>📸</emoji>Скриншоты: </b>%s"
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key",
                None,
                lambda: (
                    "Your API token from https://rawg.io/apidocs (If you are from"
                    " Russia use VPN)"
                ),
                validator=loader.validators.Hidden(),
            )
        )

    @loader.command(ru_doc="Получить информацию об игре <название игры>")
    async def gameinfo(self, message: Message):
        """Fetch game information from RAWG"""
        if self.config["api_key"] == None:
            await utils.answer(message, self.strings("no_api"))
            return
        if not (game_name := utils.get_args_raw(message)):
            await utils.answer(message, self.strings("game_not_found"))
            return
        await utils.answer(message, self.strings("fetching"))

        try:
            url = f"https://api.rawg.io/api/games?key={self.config['api_key']}&search={game_name}"
            response = await utils.run_sync(requests.get, url)

            if response.status_code == 404:
                await utils.answer(message, self.strings("game_not_found"))
                return
            response.raise_for_status()

            data = response.json()["results"][0]

            game_name = data.get("name", "N/A")
            released_date = data.get("released", "N/A")
            rating = data.get("rating", "N/A")

            platforms_str = (
                ", ".join(
                    platform["platform"]["name"]
                    for platform in data.get("platforms", [])
                )
                or "N/A"
            )

            genres_str = (
                ", ".join(genre["name"] for genre in data.get("genres", [])) or "N/A"
            )

            response = await utils.run_sync(
                requests.get,
                f"https://api.rawg.io/api/games/{data['id']}/screenshots?key={self.config['api_key']}",
            )
            screenshots = []

            if response.status_code == 200:
                screenshots_data = response.json()["results"][:3]
                for screenshot in screenshots_data:
                    screenshots.append(screenshot["image"])
            screenshots_str = ", ".join(screenshots) if screenshots else "N/A"

            game_info_message = (
                self.strings("game") % game_name
                + "\n"
                + self.strings("release") % released_date
                + "\n"
                + self.strings("rawg_rating") % rating
                + "\n"
                + self.strings("platforms") % platforms_str
                + "\n"
                + self.strings("genres") % genres_str
                + "\n"
                + self.strings("screenshots") % screenshots_str
            )
            await utils.answer(message, game_info_message)
        except Exception:
            await utils.answer(message, self.strings("error_fetching"))
