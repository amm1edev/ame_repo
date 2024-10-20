# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: BusinessCard
# Description: Show your vizit card
# Author: skillzmeow
# Commands:
# .vizit
# ---------------------------------------------------------------------------------


__version__ = (2, 0, 2)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
# scope: inline
# scope: hikka_only
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀

# meta developer: @skillzmeow, @anon97945

# you can edit this module
# 2022
import logging

from telethon.tl.types import Message

from .. import loader
from ..inline.types import InlineQuery

logger = logging.getLogger(__name__)


@loader.tds
class MyVizitkaMod(loader.Module):
    """Show your vizit card"""

    strings = {"name": "BussinesCard"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "message",
                "<b>I don't know where me.</b>",
                lambda: "Your custom message to business card",
            ),
            loader.ConfigValue(
                "button1",
                "😎 skillз modules, https://t.me/smeowcodes",
                lambda: "Your_text, https://link.com",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button2",
                "🥳 developer, https://t.me/smeowcodes",
                lambda: "Your_text, https://link.com",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button3",
                "🕌 my house, https://t.me/hikka_offtop",
                lambda: "Your_text, https://link.com",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "button4",
                "🫖 teapots, https://t.me/teapots1",
                lambda: "Your_text, https://link.com",
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "image_url",
                "https://i.imgur.com/RSq64Xu.jpeg",
                lambda: "Your file url",
            ),
            loader.ConfigValue(
                "custom_format",
                "photo",
                lambda: self.strings("_cfg_cst_frmt"),
                validator=loader.validators.Choice(["photo", "video", "audio", "gif"]),
            ),
        )

    def _get_mark(self, btn_count):
        btn_count = str(btn_count)
        return (
            {
                "text": self.config[f"button{btn_count}"][0],
                "url": self.config[f"button{btn_count}"][1],
            }
            if self.config[f"button{btn_count}"]
            else None
        )

    @loader.unrestricted
    async def vizitcmd(self, message: Message):
        """big thanks to @apodiktum_modules"""
        m = {x: self._get_mark(x) for x in range(5)}
        await self.inline.form(
            message=message,
            text=self.config["message"],
            reply_markup=[
                [
                    *([m[1]] if m[1] else []),
                    *([m[2]] if m[2] else []),
                ],
                [
                    *([m[3]] if m[3] else []),
                    *([m[4]] if m[4] else []),
                ],
            ],
            **(
                {}
                if self.config["disable_banner"]
                else {self.config["custom_format"]: self.config["image_url"]}
            ),
        )

    @loader.inline_everyone
    async def vizit_inline_handler(self, query: InlineQuery) -> dict:
        """Send userbot info"""
        m = {x: self._get_mark(x) for x in range(5)}
        return {
            "title": "SmartVizitka",
            "description": "пантуйся своей пиздатой визиткой",
            "message": self.config["message"],
            "thumb": "https://0x0.st/oBQx.jpg",
            "reply_markup": [
                [
                    *([m[1]] if m[1] else []),
                    *([m[2]] if m[2] else []),
                ],
                [
                    *([m[3]] if m[3] else []),
                    *([m[4]] if m[4] else []),
                ],
            ],
        }
