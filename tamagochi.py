# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: tamagochi
# Author: vsecoder
# Commands:
# .starttam | .infotam
# ---------------------------------------------------------------------------------

"""
                                _             
  __   _____  ___  ___ ___   __| | ___ _ __   
  \ \ / / __|/ _ \/ __/ _ \ / _` |/ _ \ '__|  
   \ V /\__ \  __/ (_| (_) | (_| |  __/ |     
    \_/ |___/\___|\___\___/ \__,_|\___|_|     

    Copyleft 2022 t.me/vsecoder                                                            
    This program is free software; you can redistribute it and/or modify 

"""
# meta developer: @vsecoder_m
# meta pic: https://img.icons8.com/external-flat-andi-nur-abdillah/344/external-Tamagochi-retro-gadget-(flat)-flat-andi-nur-abdillah.png

__version__ = (0, 0, 1)

import asyncio
import logging

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)

tamogochi_ = {
    "name": "",
    "health": 100,
    "hunger": 100,
    "clean": 100,
    "mood": 100,
    "sleepiness": 100,
    "age": 0,
}

stats = ["hunger", "clean", "mood", "sleepiness"]

ascii_cats = [
    """
      \    /\\
       )  ( ')
      (  /  )
 hi    \(__)|
""",
    """
  ^~^  ,
 ('Y') )
 /   \/ 
(\|||/)
""",
    """
 /\_/\\
( o o )
==_Y_==
  `-'
""",
    """
 |\__/,|   (`\\
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
""",
    """
  /\_/\\
 ( ^.^ )
   \\"/
 ( | | )
(__d b__)
""",
    """
   |\__/,|   (`\\
   |o o  |__ _)
 _.( T   )  `  /
((_ `^--' /_<  \\
`` `-'(((/  (((/
""",
    """
 ,_     _
 |\\\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \\
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
""",
    """
  ,-.       _,---._ __  / \\
 /  )    .-'       `./ /   \\
(  (   ,'            `/    /|
 \  `-"             \\'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \  `.___________|/
  `--'   `--'

""",
    """
                        _
                       | \\
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/
""",
    """
       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
[bug] .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'

""",
    """
           ___
          (___)
   ____
 _\___ \  |\_/|
\     \ \/ , , \ ___
 \__   \ \ ="= //|||\\
  |===  \/____)_)||||
  \______|    | |||||
      _/_|  | | =====
     (_/  \_)_) sad
  _________________
 (                _)
  (__   '          )
    (___    _____)
        '--'
""",
]


@loader.tds
class TamagochiMod(loader.Module):
    """
    🤳 Module for add Tamogochi to your Telegram[BETA]

    This is beta version, please, report bugs and send ideas to t.me/vsecoder

    📝 Commands:
    """

    strings = {
        "name": "Tamogochi",
        "error": "Error! Look in the .logs for more information.",
        "eat": ".\n<code>{}</code>\n<b>🍔 You fed your {}!</b>",
        "drink": ".\n<code>{}</code>\n<b>🍺 You gave your {} a drink!</b>",
        "play": ".\n<code>{}</code>\n<b>🎮 You played with your {}!</b>",
        "sleep": ".\n<code>{}</code>\n<b>💤 You put your {} to sleep!</b>",
        "clean": ".\n<code>{}</code>\n<b>🧼 You cleaned your {}!</b>",
        "dead": ".\n<code>{}</code>\n<b>💀 Your {} died...",
        "create": (
            ".\n<code>{}</code>\n<b>🐣 You created a Tamagochi as name {}!\nType command"
            " .infotam!</b>"
        ),
        "not_create": ".\n<code>{}</code>\n<b>🐣 You now have a Tamagochi!</b>",
        "info": (
            ".\n<code>{}</code>\n<b>🐣 Your Tamagochi {} is {} years old, {}"
            " lives.</b>\n - Hunger: {}/100\n - Clean: {}/100\n - Mood: {}/100\n -"
            " Sleepiness: {}/100"
        ),
    }

    strings_ru = {
        "error": "Ошибка! Посмотрите в .logs для получения дополнительной информации.",
        "eat": ".\n<code>{}</code>\n<b>🍔 Вы покормили {}!</b>",
        "drink": ".\n<code>{}</code>\n<b>🍺 Вы напоили {}!</b>",
        "play": ".\n<code>{}</code>\n<b>🎮 Вы поиграли с {}!</b>",
        "sleep": ".\n<code>{}</code>\n<b>💤 Вы отправили {} спать!</b>",
        "clean": ".\n<code>{}</code>\n<b>🧼 Вы помыли {}!</b>",
        "dead": ".\n<code>{}</code>\n<b>💀 Ваш {} умер...</b>",
        "create": (
            ".\n<code>{}</code>\n<b>🐣 Вы создали тамогочи с именем {}!\nВведите команду"
            " .infotam!</b>"
        ),
        "not_create": ".\n<code>{}</code>\n<b>🐣 У вас уже есть тамогочи!</b>",
        "info": (
            ".\n<code>{}</code>\n<b>🐣 Вашему тамогочи {} уже {} год(-а), {}"
            " жизней.</b>\n - Голод: {}/100\n - Чистота: {}/100\n - Настроение:"
            " {}/100\n - Сонливость: {}/100"
        ),
    }

    async def client_ready(self, client, db):
        self._client = client
        self.db = db

        self.keyboard = [
            [
                {"text": "🥕", "callback": self.render, "args": ["eat"]},
                {"text": "🍼", "callback": self.render, "args": ["drink"]},
                {"text": "🎮", "callback": self.render, "args": ["play"]},
                {"text": "🛌", "callback": self.render, "args": ["sleep"]},
                {"text": "🚿", "callback": self.render, "args": ["clean"]},
            ],
            [
                {"text": "🔄", "callback": self.render, "args": ["reload"]},
            ],
        ]

        if self.db.get("Tamagochi", "pet") == {}:
            # ticks
            while True:
                await asyncio.sleep(3600)
                pet = self.db.get("Tamagochi", "pet")
                pet["age"] += 1
                pet["hunger"] -= 1
                pet["clean"] -= 1
                pet["mood"] -= 1
                pet["sleepiness"] -= 1
                for stat in stats:
                    if pet[stat] <= 0:
                        pet["health"] -= 1
                        pet[stat] = 0
                if pet["health"] <= 0:
                    self.db.set("Tamagochi", "pet", None)
                    break
                self.db.set("Tamagochi", "pet", pet)

    async def render(self, message: InlineCall, press):
        pet = self.db.get("Tamagochi", "pet")

        if press == "eat":
            await self.feedtam(message)
        elif press == "drink":
            await self.drinktam(message)
        elif press == "play":
            await self.playtam(message)
        elif press == "sleep":
            await self.sleeptam(message)
        elif press == "clean":
            await self.cleantam(message)

        n = pet["age"]
        suffix = (
            "год"
            if 11 <= n <= 19 or n % 10 == 1
            else "года" if 2 <= n % 10 <= 4 else "лет"
        )

        await message.edit(
            text=self.strings["info"]
            .format(
                ascii_cats[8],
                pet["name"],
                pet["age"],
                pet["health"],
                pet["hunger"],
                pet["clean"],
                pet["mood"],
                pet["sleepiness"],
            )
            .replace("год(-а)", suffix),
            reply_markup=self.keyboard,
        )

    async def starttamcmd(self, message):
        """
        {name} - начать игру
        """
        args = utils.get_args_raw(message)
        pet = tamogochi_
        pet["name"] = args
        if not self.db.get("Tamagochi", "pet"):
            self.db.set("Tamagochi", "pet", pet)
            await message.edit(
                self.strings["create"].format(
                    ascii_cats[0], self.db.get("Tamagochi", "pet")["name"]
                )
            )

            # ticks
            while True:
                await asyncio.sleep(360)
                pet = self.db.get("Tamagochi", "pet")
                pet["age"] += 1
                pet["hunger"] -= 1
                pet["clean"] -= 1
                pet["mood"] -= 1
                pet["sleepiness"] -= 1
                for stat in stats:
                    if pet[stat] <= 0:
                        pet["health"] -= 1
                        pet[stat] = 0
                if pet["health"] <= 0:
                    await message.edit(
                        self.strings["dead"].format(
                            ascii_cats[10], self.db.get("Tamagochi", "pet")["name"]
                        )
                    )
                    self.db.set("Tamagochi", "pet", None)
                    break
                self.db.set("Tamagochi", "pet", pet)

        else:
            await message.edit(self.strings["not_create"].format(ascii_cats[9]))

    async def feedtam(self, message):
        """
        покормить
        """
        pet = self.db.get("Tamagochi", "pet")
        if pet:
            if pet["hunger"] >= 90:
                return
            pet["hunger"] += 10
            pet["clean"] -= 1
            pet["mood"] += 1
            pet["sleepiness"] -= 2
            self.db.set("Tamagochi", "pet", pet)

    async def drinktam(self, message):
        """
        напоить
        """
        pet = self.db.get("Tamagochi", "pet")
        if pet:
            if pet["hunger"] >= 95:
                return
            pet["hunger"] += 5
            pet["clean"] -= 1
            pet["mood"] += 1
            pet["sleepiness"] -= 2
            self.db.set("Tamagochi", "pet", pet)

    async def playtam(self, message):
        """
        поиграть
        """
        pet = self.db.get("Tamagochi", "pet")
        if pet:
            if pet["mood"] >= 90:
                return
            pet["hunger"] -= 1
            pet["clean"] -= 1
            pet["mood"] += 10
            pet["sleepiness"] -= 2
            self.db.set("Tamagochi", "pet", pet)

    async def sleeptam(self, message):
        """
        отправить спать
        """
        pet = self.db.get("Tamagochi", "pet")
        if pet:
            if pet["sleepiness"] >= 90:
                return
            pet["hunger"] -= 1
            pet["clean"] -= 1
            pet["mood"] += 1
            pet["sleepiness"] += 10
            self.db.set("Tamagochi", "pet", pet)

    async def cleantam(self, message):
        """
        помыть
        """
        pet = self.db.get("Tamagochi", "pet")
        if pet:
            if pet["clean"] >= 90:
                return
            pet["hunger"] -= 1
            pet["clean"] += 10
            pet["mood"] += 1
            pet["sleepiness"] -= 2
            self.db.set("Tamagochi", "pet", pet)

    async def infotamcmd(self, message):
        """
        инфо
        """

        pet = self.db.get("Tamagochi", "pet")
        n = pet["age"]
        suffix = (
            "год"
            if 11 <= n <= 19 or n % 10 == 1
            else "года" if 2 <= n % 10 <= 4 else "лет"
        )
        if pet:
            await self.inline.form(
                text=self.strings["info"]
                .format(
                    ascii_cats[8],
                    pet["name"],
                    pet["age"],
                    pet["health"],
                    pet["hunger"],
                    pet["clean"],
                    pet["mood"],
                    pet["sleepiness"],
                )
                .replace("год(-а)", suffix),
                message=message,
                always_allow=[message.from_id],
                reply_markup=self.keyboard,
            )
