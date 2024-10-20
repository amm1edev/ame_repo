# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: yoopay
# Author: hikariatama
# Commands:
# .yoopay
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.dan.tatar/yoopay_icon.png
# meta banner: https://mods.hikariatama.ru/badges/yoopay.jpg
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

from telethon.tl.types import Message
from yoomoney import Quickpay

from .. import loader, utils


@loader.tds
class YooMoneyMod(loader.Module):
    """Send Yoomoney pay link"""

    strings = {
        "name": "Yoomoney",
        "payme": '<b>💳 {}\n<a href="{}">Pay {} RUB 💳</a></b>',
        "args": "<b>🚫 Incorrect args</b>",
        "no_account": "<b>🚫 You need to configure module</b>",
    }

    strings_ru = {
        "payme": '<b>💳 {}\n<a href="{}">Оплатить {} RUB 💳</a></b>',
        "hikka.modules.yoopay.args": "<b>🚫 Неверные аргументы</b>",
        "hikka.modules.yoopay.no_account": "<b>🚫 Необходима конфигурация модуля</b>",
        "hikka.modules.yoopay._cmd_doc_yoopay": (
            "<сумма> <заголовок> ; <комментарий> - Отправить ссылку на оплату\n"
            "Пример: .yoopay 100 На кофе ; Бро, купи мне кофейку, вот ссылка"
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "account",
                doc=lambda: "Yoomoney wallet ID",
                validator=loader.validators.Integer(),
            ),
        )

    @loader.unrestricted
    async def yoopaycmd(self, message: Message):
        """<sum> <title> ; <comment> - Send payment link
        E.g: .yoopay 100 For coffee ; Bro, buy me a coffe, here is the link"""
        if not self.config["account"]:
            await utils.answer(message, self.strings("no_account"))
            return

        args = utils.get_args_raw(message)
        try:
            amount, titlecomm = args.split(maxsplit=1)
            amount = int(amount)
            title, comment = titlecomm.split(";", 1)
            if amount < 2:
                await utils.answer(message, self.strings("args"))
                return
        except Exception:
            await utils.answer(message, self.strings("args"))
            return

        quickpay = Quickpay(
            receiver=self.config["account"],
            quickpay_form="shop",
            targets=title.strip(),
            paymentType="SB",
            sum=amount,
            label="Money transfer to an individual",
        )

        await utils.answer(
            message,
            self.strings("payme").format(
                utils.escape_html(comment.strip()),
                quickpay.redirected_url,
                amount,
            ),
        )
