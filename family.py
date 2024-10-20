# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: family
# Author: KeyZenD
# Commands:
# .family
# ---------------------------------------------------------------------------------

# requires: pillow, pymorphy2
import io
import logging
import random
from io import BytesIO

import pymorphy2
import requests
import telethon
from PIL import Image, ImageDraw, ImageFont

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(FamilyMod())


@loader.tds
class FamilyMod(loader.Module):
    """Quote a message"""

    strings = {"name": "Family"}

    async def client_ready(self, client, db):
        self.client = message.client

    @loader.unrestricted
    @loader.ratelimit
    async def familycmd(self, message):
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, "<b>Нет Реплая.</b>")
            return
        if not args:
            await utils.answer(message, "<b>Нет Текста.</b>")
            return
        pic = await check_media(message, reply)
        if not pic:
            await utils.answer(message, "<b>Нет Изображения.</b>")
            return
        await message.edit("Семья")
        font = requests.get(
            "https://github.com/KeyZenD/l/blob/master/bold.ttf?raw=true"
        ).content
        family = makeFamily(pic, args, font)
        await message.client.send_file(message.to_id, family, reply_to=reply)
        await message.delete()


def place(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize(
        (random.randint(size, size * 2), random.randint(size, size * 2))
    )
    background.paste(overlay, cords)


def placeText(background, cords, size, text, font):
    text_cords = (
        cords[0] + random.randint(0, size // 2),
        cords[1] + random.randint(0, size // 2),
    )
    draw = ImageDraw.Draw(background)
    draw.text(
        text_cords,
        text,
        (0, 0, 0),
        font=ImageFont.truetype(io.BytesIO(font), random.randint(size // 8, size // 4)),
    )


def makeFamily(image, caption, font):
    morph = pymorphy2.MorphAnalyzer()
    infl = morph.parse(caption)[0].inflect({"plur", "gent"})
    if not infl:
        caption_mlt = caption
    else:
        caption_mlt = infl.word
    canvas = Image.new("RGBA", (600, 600), "white")

    draw = ImageDraw.Draw(canvas)

    draw.text(
        (120, 5),
        "ахах семья " + caption_mlt,
        (0, 0, 0),
        font=ImageFont.truetype(io.BytesIO(font), 32),
    )

    family = [
        {"name": "мама", "cords": (60, 100), "size": 160},
        {"name": "папа", "cords": (260, 80), "size": 180},
        {"name": "сын", "cords": (60, 380), "size": 125},
        {"name": "дочь", "cords": (230, 320), "size": 125},
        {"name": "дочь", "cords": (225, 380), "size": 125},
        {"name": "сын", "cords": (340, 390), "size": 125},
    ]

    for member in family:
        place(canvas, image, member["cords"], member["size"])
    for member in family:
        placeText(
            canvas,
            member["cords"],
            member["size"],
            member["name"] + " " + caption,
            font,
        )
    temp = BytesIO()
    canvas.save(temp, format="png")
    return temp.getvalue()


async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None
