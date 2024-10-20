# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: craiyon
# Author: hikariatama
# Commands:
# .craiyon
# ---------------------------------------------------------------------------------

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#
#          https://t.me/hikariatama
#
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://static.dan.tatar/craiyon_icon.png
# meta banner: https://mods.hikariatama.ru/badges/craiyon.jpg
# meta developer: @hikarimods
# scope: hikka_only
# scope: hikka_min 1.2.10

import base64

import requests
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class CrAIyonMod(loader.Module):
    """Generates images by description using Craiyon AI (DALL-E)"""

    strings = {
        "name": "CrAIyon",
        "args": "🚫 <b>No photo description specified</b>",
        "generating": (
            "🖌 <b>Drawing request </b><code>{}</code><b> using craiyon. Be patient,"
            " this takes some time</b>"
        ),
        "error": "🚫 <b>I can't draw </b><code>{}</code>",
        "drawing": "🖌 <b>This is delicious </b><code>{}</code>",
    }

    strings_ru = {
        "args": "🚫 <b>Не указано описание фотографии</b>",
        "generating": (
            "🖌 <b>Рисую запрос </b><code>{}</code><b> через craiyon. Будьте терпеливы,"
            " это занимает некоторое время</b>"
        ),
        "error": "🚫 <b>Я не могу нарисовать </b><code>{}</code>",
        "drawing": "🖌 <b>Восхитительный </b><code>{}</code>",
        "_cmd_doc_craiyon": (
            "<описание> - Сгенерировать изображение по описанию с помощью Craiyon AI"
            " (DALL-E)"
        ),
        "_cls_doc": "Генерирует изображения по описанию с помощью Craiyon AI (DALL-E)",
    }

    strings_de = {
        "args": "🚫 <b>Keine Bildbeschreibung angegeben</b>",
        "generating": (
            "🖌 <b>Zeichne Anfrage </b><code>{}</code><b> mit craiyon. Sei geduldig,"
            " das dauert ein wenig</b>"
        ),
        "error": "🚫 <b>Kann nicht zeichnen </b><code>{}</code>",
        "drawing": "🖌 <b>Das ist lecker </b><code>{}</code>",
        "_cmd_doc_craiyon": (
            "<Beschreibung> - Generiert ein Bild nach Beschreibung mit Craiyon AI"
            " (DALL-E)"
        ),
        "_cls_doc": "Generiert Bilder nach Beschreibung mit Craiyon AI (DALL-E)",
    }

    strings_hi = {
        "args": "🚫 <b>कोई फोटो विवरण निर्दिष्ट नहीं किया गया</b>",
        "generating": (
            "🖌 <b>craiyon के साथ अनुरोध रचना </b><code>{}</code><b>। धैर्य रखें,"
            " यह कुछ समय लेता है</b>"
        ),
        "error": "🚫 <b>मैं नहीं चित्र बना सकता </b><code>{}</code>",
        "drawing": "🖌 <b>यह अद्भुत है </b><code>{}</code>",
        "_cmd_doc_craiyon": (
            "<विवरण> - Craiyon AI (DALL-E) का उपयोग करके विवरण के अनुसार एक छवि उत्पन्न"
            " करता है"
        ),
        "_cls_doc": (
            "Craiyon AI (DALL-E) का उपयोग करके विवरण के अनुसार छवियां उत्पन्न करता है"
        ),
    }

    strings_uz = {
        "args": "🚫 <b>Rasm tavsifi ko'rsatilmadi</b>",
        "generating": (
            "🖌 <b>craiyon orqali so'rovni chizish </b><code>{}</code><b>."
            " Sabr qiling, bu bir necha vaqt oladi</b>"
        ),
        "error": "🚫 <b>Rasmni chizib bo'lmadi </b><code>{}</code>",
        "drawing": "🖌 <b>Bu juda yaxshi </b><code>{}</code>",
        "_cmd_doc_craiyon": (
            "<tavsif> - Craiyon AI (DALL-E) orqali tavsifga mos rasm yaratadi"
        ),
        "_cls_doc": "Craiyon AI (DALL-E) orqali tavsifga mos rasmlar yaratadi",
    }

    strings_tr = {
        "args": "🚫 <b>Fotoğraf açıklaması belirtilmedi</b>",
        "generating": (
            "🖌 <b>craiyon ile istek çizimi </b><code>{}</code><b>."
            " Sabırlı olun, bu biraz zaman alır</b>"
        ),
        "error": "🚫 <b>Çizemiyorum </b><code>{}</code>",
        "drawing": "🖌 <b>Bu lezzetli </b><code>{}</code>",
        "_cmd_doc_craiyon": (
            "<açıklama> - Craiyon AI (DALL-E) kullanarak açıklamaya göre bir resim"
            " oluşturun"
        ),
        "_cls_doc": "Craiyon AI (DALL-E) kullanarak açıklamaya göre resimler oluşturur",
    }

    async def craiyoncmd(self, message: Message):
        """<description> - Generate an image by description using Craiyon AI (DALL-E)"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args"))
            return

        form = await self.inline.form(
            self.strings("generating").format(utils.escape_html(args)),
            message=message,
            gif="https://pa1.narvii.com/6074/b2f0163e5dd1ff7ee6582e1e032eb906b25228ac_hq.gif",
            silent=True,
            reply_markup={"text": "🧑‍🎨 Drawing...", "data": "empty"},
            ttl=24 * 60 * 60,
        )

        result = (
            await utils.run_sync(
                requests.post,
                "https://backend.craiyon.com/generate",
                json={"prompt": args},
                headers={
                    "accept": "application/json",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
                    "content-type": "application/json",
                    "origin": "https://www.craiyon.com",
                    "referer": "https://www.craiyon.com/",
                    "user-agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                        " (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
                    ),
                },
            )
        ).json()

        if not result.get("images"):
            await form.edit(
                self.strings("error").format(args),
                reply_markup=None,
                gif="https://data.whicdn.com/images/61134119/original.gif",
            )
            return

        images = [base64.b64decode(i.encode()) for i in result["images"]]
        await message.respond(self.strings("drawing").format(args), file=images)
        await form.delete()
