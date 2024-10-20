# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Shazam
# Author: D4n13l3k00
# Commands:
# .shazam | .shazamtext
# ---------------------------------------------------------------------------------

# .------.------.------.------.------.------.------.------.------.------.
# |D.--. |4.--. |N.--. |1.--. |3.--. |L.--. |3.--. |K.--. |0.--. |0.--. |
# | :/\: | :/\: | :(): | :/\: | :(): | :/\: | :(): | :/\: | :/\: | :/\: |
# | (__) | :\/: | ()() | (__) | ()() | (__) | ()() | :\/: | :\/: | :\/: |
# | '--'D| '--'4| '--'N| '--'1| '--'3| '--'L| '--'3| '--'K| '--'0| '--'0|
# `------`------`------`------`------`------`------`------`------`------'
#
#                     Copyright 2023 t.me/D4n13l3k00
#           Licensed under the Creative Commons CC BY-NC-ND 4.0
#
#                    Full license text can be found at:
#       https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
#
#                           Human-friendly one:
#            https://creativecommons.org/licenses/by-nc-nd/4.0

# meta developer: @D4n13l3k00


# requires: ShazamAPI

import io

from ShazamAPI import Shazam

from .. import loader, utils  # type: ignore


@loader.tds
class ShazamMod(loader.Module):
    """Shazam API"""

    strings = {"name": "Shazam API"}
    tag = "<b>[Shazam]</b> "

    @loader.owner
    async def shazamcmd(self, m):
        """.shazam <reply to audio> - распознать трек"""
        s = await get_audio_shazam(m)
        if not s:
            return
        try:
            shazam = Shazam(s.track.read())
            recog = shazam.recognizeSong()
            track = next(recog)[1]["track"]
            await m.client.send_file(
                m.to_id,
                file=track["images"]["background"],
                caption=self.tag + "Распознанный трек: " + track["share"]["subject"],
                reply_to=s.reply.id,
            )
            await m.delete()
        except:
            await m.edit(f"{self.tag}Не удалось распознать...")

    async def shazamtextcmd(self, m):
        """.shazamtext <reply to audio> - узнать текст трека"""
        s = await get_audio_shazam(m)
        if not s:
            return
        try:
            shazam = Shazam(s.track.read())
            recog = shazam.recognizeSong()
            track = next(recog)[1]["track"]
            text = track["sections"][1]["text"]
            await utils.answer(
                m,
                "\n".join(
                    self.tag + f"Текст трека {track['share']['subject']}\n\n" + text
                ),
            )
        except Exception:
            await m.edit(f"{self.tag}Не удалось распознать... | Текста нет...")


async def get_audio_shazam(m):
    class rct:
        track = io.BytesIO()
        reply = None

    reply = await m.get_reply_message()
    if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
        ae = rct()
        await utils.answer(m, "<b>[Shazam]</b> Скачиваю...")
        ae.track = io.BytesIO(await reply.download_media(bytes))
        ae.reply = reply
        await m.edit("<b>[Shazam]</b> Распознаю...")
        return ae
    else:
        await utils.answer(m, "<b>[Shazam]</b> reply to audio...")
        return None
