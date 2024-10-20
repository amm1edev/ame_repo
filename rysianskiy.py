# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: rysianskiy
# Description: Perevodit rysskiy na rysianskiy yazyk
# Author: KeyZenD
# Commands:
# .rysianskiy
# ---------------------------------------------------------------------------------


import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class RysianskiyMod(loader.Module):
    """Perevodit rysskiy na rysianskiy yazyk"""

    strings = {
        "name": "Rysianskiy yazyk",
        "nety_teksta": "<b>Nety teksta dlya izmeneniya!</b>",
    }

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def rysianskiycmd(self, soobshenie):
        """.rysianskiy <tekst ili replay na tekst>"""

        otvet = await soobshenie.get_reply_message()
        vvod = utils.get_args_raw(soobshenie)
        if not vvod:
            if not otvet or not otvet.text:
                await utils.answer(soobshenie, self.strings("nety_teksta", soobshenie))
                return
            else:
                tekst = otvet.raw_text
        else:
            tekst = vvod
        vyvod = ""
        for simvol in tekst:
            if simvol.lower() in bykvy:
                bykva = bykvy[simvol.lower()]
                if simvol.isupper():
                    bykva = bykva.upper()
            else:
                bykva = simvol
            vyvod += bykva
        await utils.answer(soobshenie, vyvod)


bykvy = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "j",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "y",
    "ф": "f",
    "х": "h",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "sh'",
    "ъ": '"',
    "ы": "y",
    "ь": "'",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}
