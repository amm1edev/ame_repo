# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MeowCrypto
# Description: Awesome cryptocurrency viewer by @smeowcodes
# Author: skillzmeow
# Commands:
# .defvalue | .crypto
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 4)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes

import random as r

import requests
from telethon.tl.types import Message

from .. import loader, utils


class MeowCryptoManagerMod(loader.Module):
    """Awesome cryptocurrency viewer by @smeowcodes"""

    strings = {
        "name": "MeowCrypto",
        "inc_args": "<b>🐳 Incorrect args</b>",
        "keyerror": (
            "🗿 <b>Maybe the coin is not in the site database or you typed the wrong"
            " name.</b>"
        ),
        "okey": "<b>👯 Successfully. Current default valute: {}</b>",
    }
    strings_ru = {
        "inc_args": "<b>🐳 Неккоректные аргументы</b>",
        "keyerror": (
            "🗿 <b>Возможно монеты нету в базе данных сайта, или вы ввели неккоректное"
            " название.</b>"
        ),
        "okey": "<b>👯 Успешно. Текущая стандартная валюта: {}</b>",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        post = await client.get_messages("smeowcodes", ids=831)
        await post.react("❤️")

    async def defvaluecmd(self, message: Message):
        """set a default valute"""

        args = utils.get_args_raw(message)
        self.db.set("defaultvalute", "val", args)
        await utils.answer(message, self.strings("okey").format(args))

    async def cryptocmd(self, message: Message):
        "use .crypto <count (float or int)> <coin name>."
        args = utils.get_args_raw(message)
        tray = self.db.get("defaultvalute", "val", args)
        if tray == "":
            tray = "btc"
        if not args:
            args = "1" + " " + str(tray)
        args_list = args.split(" ")
        try:
            if len(args_list) == 1 and isinstance(float(args_list[0]), float) == True:
                args_list.append(str(tray))
        except Exception:
            args_list = ["1", args_list[0]]
        coin = args_list[1].upper()
        api = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD,RUB,UAH,PLN,KZT,BTC,ETH,TONCOIN"
        ).json()
        smiles = r.choice(
            [
                "<emoji document_id=5316957963833844741>🎉</emoji>",
                "<emoji document_id=5318887237373406513>🎉</emoji>",
                "<emoji document_id=5319279393657331316>🎉</emoji>",
                "<emoji document_id=5316773207225671537>🎉</emoji>",
                "<emoji document_id=5319032480282451646>🎉</emoji>",
            ]
        )

        try:
            try:
                count = float(args_list[0])
                form = (
                    "{} <b>{} {} is:</b>\n\n<emoji"
                    " document_id=6323374027985389586>🇺🇸</emoji>"
                    " <code>{}$</code>\n<emoji"
                    " document_id=6323289850921354919>🇺🇦</emoji>"
                    " <code>{}₴</code>\n<emoji"
                    " document_id=6323602387101550101>🇵🇱</emoji>"
                    " <code>{}zł.</code>\n<emoji"
                    " document_id=6323139226418284334>🇷🇺</emoji>"
                    " <code>{}₽</code>\n<emoji"
                    " document_id=6323135275048371614>🇰🇿</emoji>"
                    " <code>{}₸</code>\n<emoji"
                    " document_id=5465465383035083768>💰</emoji> <code>{}"
                    " BTC</code>\n<emoji document_id=5465198785825087352>💰</emoji>"
                    " <code>{} ETH</code>\n<emoji"
                    " document_id=5197515039296200279>💰</emoji> <code>{} TONCOIN</code>"
                ).format(
                    smiles,
                    count,
                    coin,
                    round(api["USD"] * count, 2),
                    round(api["UAH"] * count, 2),
                    round(api["PLN"] * count, 2),
                    round(api["RUB"] * count, 2),
                    round(api["KZT"] * count, 2),
                    round(api["BTC"] * count, 4),
                    round(api["ETH"] * count, 4),
                    round(api["TONCOIN"] * count, 4),
                )

                a = r.randint(0, 5)
                if a == 3:
                    mark = [
                        [{"text": "💞 MeowCrypto", "url": "https://t.me/smeowcodes/831"}]
                    ]
                else:
                    mark = []
                # await self.inline.form(
                #    message=message,
                #    text=form,
                #    reply_markup=mark,
                # )
                await utils.answer(message, form)
            except KeyError:
                await utils.answer(message, self.strings("keyerror"))
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))
