# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MeowMail
# Description: Big updated news sender. idea by @shadow_modules
# Author: skillzmeow
# Commands:
# .news | .settext
# ---------------------------------------------------------------------------------


__version__ = (0, 0, 1)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

from asyncio import sleep

from telethon.tl.types import Message

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes
# meta pic: https://siasky.net/XACW0K6mdI6W6tUiG4lEhxfy49KpLHAN-tRPmCsWcAOCnw
# meta banner: https://siasky.net/fAMEML097T4v2x8Zh27F2vzFI2SXs7ezO48tQxoTfodxfA
from .. import loader, utils


class MeowMailMod(loader.Module):
    """big updated news sender. idea by @shadow_modules"""

    strings = {
        "name": "MeowMail",
        "sep": (
            "2 comma-separated arguments. the first is the delay between messages in"
            " seconds, the second is the number of repetitions."
        ),
        "args_inc": "<b>🚨 Arguments are incorrect.</b>",
        "not_set": "<b>❗️ Text not set! Use .settext</b>",
        "activated": (
            "<b>⚡️ The text is set. Use the .news command to start the newsletter."
            " Don't forget to use the config!\n✏️ Text:</b> <code>{}</code>"
        ),
        "news": (
            "<b>😉 The mailing has started. You can find the defined chats in the"
            " config.</b>"
        ),
    }

    strings_ru = {
        "sep": (
            "2 аргумента через запятую. первым идет задержка между сообщениями в"
            " секундах, вторым кол-во повторов"
        ),
        "args_inc": "<b>🚨 Аргументы некорректны.",
        "not_set": "<b>❗️ Текст не установлен! Используйте .settext</b>",
        "activated": (
            "<b>⚡️ Текст задан. Используйте команду .news что бы начать рассылку. Не"
            " забывайте про конфиг!\n✏️ Текст:</b> <code>{}</code>"
        ),
        "news": "<b>😉 Рассылка началась. Заданные чаты можно узнать в конфиге.</b>",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Chats",
                [],
                lambda: "Chat for newsletter",
                validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("^@[a-zA-Z0-9_]{1,32}$"),
                    ),
                ),
            ),
            loader.ConfigValue(
                "NewsSettings",
                "600, 5",
                lambda: self.strings("sep"),
            ),
        )

    async def newscmd(self, message: Message):
        "start a newsletter"
        status = self.db.get("meowmail", "status", "")
        settings = self.config["NewsSettings"]
        text = self.db.get("meowmail", "text", "")
        if text:
            await utils.answer(message, self.strings("news"))
            for x in range(int(settings[1])):
                for chat in self.config["Chats"]:
                    await self.client.send_message(chat, text)
                await sleep(int(settings[0]))
        else:
            await utils.answer(message, self.strings("not_set"))

    async def settextcmd(self, message: Message):
        "<text>, .config meowmail -> NewsSettings"
        args = utils.get_args_raw(message)
        if args:
            self.db.set("meowmail", "text", args)
            await utils.answer(message, self.strings("activated").format(args))
        else:
            await utils.answer(message, self.strings("args_inc"))
