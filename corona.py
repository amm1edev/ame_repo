# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU GPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: corona
# Description: Gets the latest COVID-19 data found in JHU database for a country
# Author: HitaloSama
# Commands:
# .corona
# ---------------------------------------------------------------------------------


#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2020 The Authors

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

import json
import logging
from datetime import datetime

import dateutil.parser
import requests

from .. import loader, utils

logger = logging.getLogger(__name__)


class CoronaReportsMod(loader.Module):
    """Gets the latest COVID-19 data found in JHU database for a country"""

    strings = {"name": "Corona"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "DEFAULT_COUNTRY", "spain", "Enter your default country here"
        )

    async def coronacmd(self, message):
        """.corona <country (Optional)>"""
        args = utils.get_args_raw(message)
        if not args:
            country = self.config["DEFAULT_COUNTRY"]
        else:
            country = args

        message = await utils.answer(message, "<code>Visiting  Wuhan...</code>")

        url = "https://covid19.mathdro.id/api/countries/" + country
        tries = 0
        response = requests.get(url)

        while response.status_code == 400 and tries < 10:
            response = requests.get(url)
            tries += 1
            await utils.answer(message, "<code>Try #" + str(tries) + "...</code>")

        jsonDumps = json.dumps(response.json(), sort_keys=True)
        jsonResponse = json.loads(jsonDumps)

        if response.status_code == 200:
            confirmed = jsonResponse["confirmed"]["value"]
            recovered = jsonResponse["recovered"]["value"]
            deaths = jsonResponse["deaths"]["value"]
            active = confirmed - recovered - deaths

            try:
                lastUpdate = dateutil.parser.parse(jsonResponse["lastUpdate"]).strftime(
                    "%d/%m/%Y - %X"
                )
            except (ValueError, TypeError) as e:
                logger.error(e)
                lastUpdate = jsonResponse["lastUpdate"]

            msg = "<s>-------------------------------------</s>\n"
            msg += "👑🦠 in " + country.capitalize() + "<i> " + lastUpdate + "</i>\n"
            msg += "<s>-------------------------------------</s>\n"
            msg += "<b>😷 Confirmed:</b> " + str(confirmed)
            msg += (
                "\n<b>🤧 Active:</b> "
                + str(active)
                + " ("
                + str(round(active / confirmed * 100, 2))
                + "%)"
            )
            msg += (
                "\n<b>🏥 Recovered:</b> "
                + str(recovered)
                + " ("
                + str(round(recovered / confirmed * 100, 2))
                + "%)"
            )
            msg += (
                "\n<b>💀 Deaths:</b> "
                + str(deaths)
                + " ("
                + str(round(deaths / confirmed * 100, 2))
                + "%)"
            )

        elif response.status_code == 404:
            msg = "<code>" + jsonResponse["error"]["message"] + "</code>"
        elif response.status_code == 400:
            msg = "<code>Bad request</code>"
        else:
            msg = "<code>Unknown error</code>"
        await utils.answer(message, msg)
