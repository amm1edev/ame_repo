# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: NewsLetter
# Author: shadowhikka
# Commands:
# .sendnews
# ---------------------------------------------------------------------------------

# █▀ █░█ ▄▀█ █▀▄ █▀█ █░█░█
# ▄█ █▀█ █▀█ █▄▀ █▄█ ▀▄▀▄▀

# Copyright 2023 t.me/shadow_modules
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from telethon.tl.types import Message  # type: ignore

from .. import loader, utils
from ..inline.types import InlineCall  # type: ignore

# meta developer: @shadow_modules, @hikarimods
# scope: hikka_only
# scope: hikka_min 1.3.0
# meta banner: https://i.imgur.com/Hy9ABNY.jpeg


@loader.tds
class NewsLetterMod(loader.Module):
    strings = {
        "name": "NewsLetter",
        "succnews": (
            "<b>✅ Newsletter successfully sent</b>\n<b>👁‍🗨 Chats that were"
            " sent:</b>\n{}"
        ),
        "nochat": "<b>No chat to send</b>",
        "warnform": (
            "<b>⚠️ Attention!</b>\n<b>😰 When sending a newsletter to a lot of chats,"
            " there may be a flood</b>\n<b>✅ If you agree that you can get a flood,"
            " click on the button below</b>"
        ),
        "noargs": "<b>😥 There are no messages to send</b>",
        "yes": "✅ Yes",
        "no": "❌ No",
    }
    strings_ru = {
        "succnews": (
            "<b>✅ Рассылка успешно отправлена</b>\n<b>👁‍🗨 Чаты в которые была"
            " отправлена рассылка:</b>\n{}"
        ),
        "nochat": "<b>Нет чата для рассылки</b>",
        "warnform": (
            "<b>⚠️ Внимание!</b>\n<b>😰 При отправке рассылки во многое количество чатов"
            " может быть флудвейт</b>\n<b>✅ Если вы согласны с тем что можете получить"
            " флудвейт - нажмите на кнопку ниже</b>"
        ),
        "noargs": "<b>😥 Нет сообщения что-бы рассылать</b>",
        "yes": "✅ Да",
        "no": "❌ Нет",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chats",
                [],
                lambda: "Chat for newsletter",
                validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("^@[a-zA-Z0-9_]{1,32}$"),
                    ),
                ),
            ),
        )

    async def sendnewscmd(self, message: Message):
        if self.get("warn") == "no":
            await self.inline.form(
                message=message,
                text=self.strings("warnform"),
                reply_markup=[
                    [
                        {
                            "text": self.strings("yes"),
                            "callback": self.inline__callAnswer,
                            "args": ("yes",),
                        },
                    ],
                    [
                        {
                            "text": self.strings("no"),
                            "callback": self.inline__callAnswer,
                            "args": ("no",),
                        },
                    ],
                ],
            )
            return
        args = utils.get_args_raw(message)
        chats = self.config["chats"]
        try:
            for chat in chats:
                await self.client.send_message(chat, args)
            await utils.answer(
                message,
                self.strings("succnews").format("\n".join(map(str, chats))),
            )
        except ValueError:
            await utils.answer(message, self.strings("noargs"))

    async def inline__callAnswer(self, call: InlineCall, value: str):
        self.set("warn", value)
        await call.delete()
