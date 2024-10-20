# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-SA 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: osu
# Author: MoriSummerz
# Commands:
# .osume | .osutop | .osuprofile
# ---------------------------------------------------------------------------------

__version__ = (1, 3, 0)

"""
    █▀▄▀█ █▀█ █▀█ █ █▀ █ █ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
    █ ▀ █ █▄█ █▀▄ █ ▄█ █▄█ █ ▀ █ █ ▀ █ ██▄ █▀▄
    Copyright 2022 t.me/morisummermods
    Licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
# requires: requests emoji-country-flag
# meta developer: @morisummermods
# meta banner: https://i.imgur.com/fPWWFrL.jpg
# meta pic: https://i.imgur.com/fcHCrS2.png


import datetime
import json
import logging

import flag
import requests
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class OsuMod(loader.Module):
    """ "I'm an osu!bot that can do some things written by @morisummerzxc"""

    strings = {
        "name": "Osu",
        "you_are": (
            "<emoji document_id=5398001711786762757>✅</emoji> <b>You are"
            " </b><code>{}</code><b> now</b>"
        ),
    }

    strings_ru = {
        "you_are": (
            "<emoji document_id=5398001711786762757>✅</emoji> <b>Теперь ты"
            " </b><code>{}</code><b></b>"
        ),
    }

    async def client_ready(self, client, db) -> None:
        self.url = "https://osu.ppy.sh/users/"
        self.nickname = self.db.get(self.strings["name"], "nickname", "")

        if hasattr(self, "hikka"):
            return
        self.db = db
        self.client = client
        try:
            channel = await self.client.get_entity("t.me/morisummermods")
            await client(JoinChannelRequest(channel))
        except Exception:
            logger.error("Can't join morisummermods")
        try:
            post = (await client.get_messages("@morisummermods", ids=[11]))[0]
            await post.react("❤️")
        except Exception:
            logger.error("Can't react to t.me/morisummermods")

    @loader.unrestricted
    async def osumecmd(self, message: Message) -> None:
        """Remember user's nickname for commands"""
        nickname = utils.get_args_raw(message)
        self.db.set(self.strings["name"], "nickname", nickname)
        self.nickname = nickname
        await utils.answer(
            message,
            self.strings("you_are").format(utils.escape_html(self.nickname)),
        )

    @loader.unrestricted
    async def osutopcmd(self, message: Message) -> None:
        """Get user's 5 best plays"""
        nickname = self.nickname
        url = self.url
        args = utils.get_args_raw(message)
        if not nickname and not args:
            await utils.answer(
                message,
                (
                    "Remember your nickname with .osume <your nickname> or use .osutop"
                    " <nickname>"
                ),
            )
            return
        if args:
            nickname = args
        req = requests.get(f"https://osu.ppy.sh/users/{nickname}").text
        s = req.find('data-initial-data="') + 19
        JSON = req[s : req.find('"', s + 1)].replace("&quot;", '"')
        info = json.loads(JSON)
        topScores = info["extras"]["scoresBest"]
        rank = info["user"]["statistics"]["global_rank"]
        out = (
            "5 best scores for: "
            + '<a href="'
            + url
            + nickname
            + '">'
            + nickname
            + "</a> #"
            + str(rank)
            + "\n\n<b>"
        )
        for top in topScores[:5]:
            # todo: beatmap with link
            out += (
                '<a href="'
                + top["beatmap"]["url"]
                + '">'
                + top["beatmapset"]["title"]
                + "</b> by <b>"
                + top["beatmapset"]["artist_unicode"]
                + "["
                + top["beatmap"]["version"].replace("&#039;", "'")
                + "]</a>\n"
            )
            if top["rank"] == "X":
                grade = "SS+"
            elif top["rank"][-1] == "H":
                grade = top["rank"][:-1] + "+"
            else:
                grade = top["rank"]
            out += f"{grade} " + str(round(float(top["accuracy"]) * 100, 2)) + "% "
            for mod in top["mods"]:
                out += f"{mod} "
            out += str(top["beatmap"]["difficulty_rating"]) + "★"
            if top["perfect"]:
                out += "FC"
            out += "\n" + str(top["pp"]) + "pp\n</b>"
            out += (
                datetime.strptime(
                    top["created_at"], "%Y-%m-%dT%H:%M:%S+00:00"
                ).strftime("%d.%m.%Y %H:%M:%S")
                + "\n\n"
            )
        await utils.answer(message, out)
        return

    @loader.unrestricted
    async def osuprofilecmd(self, message: Message) -> None:
        """Get user's profile"""
        nickname = self.nickname
        url = self.url
        args = utils.get_args_raw(message)
        if not nickname and not args:
            await utils.answer(
                message,
                (
                    "Remember your nickname with .osume <your nickname> or use .osutop"
                    " <nickname>"
                ),
            )
            return
        if args:
            nickname = args
        await message.delete()
        req = requests.get(f"https://osu.ppy.sh/users/{nickname}").text
        s = req.find('data-initial-data="') + 19
        JSON = req[s : req.find('"', s + 1)].replace("&quot;", '"')
        info = json.loads(JSON)
        profile = info["user"]
        photo = profile["avatar_url"]
        out = (
            '<a href="'
            + url
            + profile["username"]
            + '">'
            + flag.flag(profile["country_code"])
            + profile["username"]
            + " profile</a>:\n\n"
        )
        out += (
            "<b>PP: "
            + str(profile["statistics"]["pp"])
            + "| #"
            + str(profile["statistics"]["global_rank"])
            + "(#"
            + str(profile["statistics"]["country_rank"])
            + ")</b>"
            + "\n\n"
        )
        top = info["extras"]["scoresBest"][0]
        topScore = (
            '<a href="'
            + top["beatmap"]["url"]
            + '">'
            + top["beatmapset"]["title"]
            + "</b> by <b>"
            + top["beatmapset"]["artist_unicode"]
            + "["
            + top["beatmap"]["version"].replace("&#039;", "'")
            + "]</a>\n"
        )
        if top["rank"] == "X":
            grade = "SS+"
        elif top["rank"][-1] == "H":
            grade = top["rank"][:-1] + "+"
        else:
            grade = top["rank"]
        topScore += f"{grade} " + str(round(float(top["accuracy"]) * 100, 2)) + "% "
        for mod in top["mods"]:
            topScore += f"{mod} "
        topScore += str(top["beatmap"]["difficulty_rating"]) + "★"
        if top["perfect"]:
            topScore += "FC"
        topScore += "\n" + str(top["pp"]) + "pp\n</b>"
        topScore += (
            "{"
            + str(top["statistics"]["count_300"])
            + "/"
            + str(top["statistics"]["count_100"])
            + "/"
            + str(top["statistics"]["count_50"])
            + "/"
            + str(top["statistics"]["count_miss"])
            + "}\n"
        )
        topScore += (
            datetime.strptime(top["created_at"], "%Y-%m-%dT%H:%M:%S+00:00").strftime(
                "%d.%m.%Y %H:%M:%S"
            )
            + "\n"
        )
        out += "Highest pp play:\n" + topScore + "\n"
        out += (
            "Play count: "
            + str(profile["statistics"]["play_count"])
            + "\nPlay time: "
            + str(round(profile["statistics"]["play_time"] / 3600, 2))
            + "h\nAccuracy: "
            + str(round(profile["statistics"]["hit_accuracy"], 2))
            + "%\nLVL: "
            + str(profile["statistics"]["level"]["current"])
            + "\n\nJoined "
            + str(
                datetime.strptime(
                    profile["join_date"], "%Y-%m-%dT%H:%M:%S+00:00"
                ).strftime("%d.%m.%Y")
            )
        )
        await self.client.send_file(message.peer_id, photo, caption=out)
