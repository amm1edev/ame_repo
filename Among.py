# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Among
# Author: DarkModules
# Commands:
# Failed to parse
# ---------------------------------------------------------------------------------

#
# █▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
# █▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://te.legra.ph/file/17f9f1dcfeca1242bb353.jpg
# meta banner: https://te.legra.ph/file/17f9f1dcfeca1242bb353.jpg
# scope: hikka_min 1.5.0
# scope: hikka_only
# version: 1.0

from io import BytesIO
from random import randint
from secrets import choice
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont
from requests import get

from .. import loader, utils


class AmongMod(loader.Module):
    """Create AmongUs stickers"""

    strings = {
        "name": "Among",
    }

    async def amongcmd(self, message):
        """Type message or reply"""
        clrs = {
            "red": 1,
            "lime": 2,
            "green": 3,
            "blue": 4,
            "cyan": 5,
            "brown": 6,
            "purple": 7,
            "pink": 8,
            "orange": 9,
            "yellow": 10,
            "white": 11,
            "black": 12,
        }
        clr = randint(1, 12)
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text in clrs:
            clr = clrs[text]
            text = None
        if not text:
            if not reply:
                await utils.answer(message, message.sender)
                return
            if not reply.text:
                await utils.answer(message, reply.sender)
                return
            text = utils.get_args_raw(message)
        if text.split(" ")[0] in clrs:
            clr = clrs[text.split(" ")[0]]
            text = " ".join(text.split(" ")[1:])
        if text == "colors":
            await message.edit(
                (
                    "Cores disponíveis:\n"
                    + "\n".join(f"• `{i}`" for i in list(clrs.keys()))
                )
            )
            return
        url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
        font = ImageFont.truetype(BytesIO(get(url + "bold.ttf").content), 60)
        imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
        text_ = "\n".join("\n".join(wrap(part, 30)) for part in text.split("\n"))
        w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
            text_, font, stroke_width=2
        )
        text = Image.new("RGBA", (w + 30, h + 30))
        ImageDraw.Draw(text).multiline_text(
            (15, 15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000"
        )
        w = imposter.width + text.width + 10
        h = max(imposter.height, text.height)
        image = Image.new("RGBA", (w, h))
        image.paste(imposter, (0, h - imposter.height), imposter)
        image.paste(text, (w - text.width, 0), text)
        image.thumbnail((512, 512))
        output = BytesIO()
        output.name = "dziru.webp"
        image.save(output)
        output.seek(0)
        await message.delete()
        await message.client.send_file(message.to_id, output, reply_to=reply)
