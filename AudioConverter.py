# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AudioConverter
# Description: Конвертирование в разные форматы
# Author: SekaiYoneya
# Commands:
# .tovoice | .toformat
# ---------------------------------------------------------------------------------


# @Sekai_Yoneya

import io

from pydub import AudioSegment
from telethon import types

from .. import loader, utils


def register(cb):
    cb(AudioConverterMod())


class AudioConverterMod(loader.Module):
    """Конвертирование в разные форматы"""

    strings = {"name": "AudioConverter"}

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def tovoicecmd(self, message):
        """.tovoice <reply to audio>
        Сконвертировать аудио в войс
        """
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("А где реплай?")
            return
        else:
            try:
                if reply.media.document.attributes[0].voice == True:
                    await message.edit("Это войс, а не аудиофайл!")
                    return
            except:
                await message.edit("Это не аудиофайл!")
                return
        await message.edit("[AudioConverter] Скачиваем...")
        au = io.BytesIO()
        await message.client.download_media(reply.media.document, au)
        au.seek(0)
        await message.edit("[AudioConverter] Делаем войс...")
        audio = AudioSegment.from_file(au)
        m = io.BytesIO()
        m.name = "voice.ogg"
        audio.split_to_mono()
        await message.edit("[AudioConverter] Экспортируем...")
        dur = len(audio) / 1000
        audio.export(m, format="ogg", bitrate="64k", codec="libopus")
        await message.edit("[AudioConverter] Отправляем...")
        m.seek(0)
        await message.client.send_file(
            message.to_id, m, reply_to=reply.id, voice_note=True, duration=dur
        )
        await message.delete()

    async def toformatcmd(self, message):
        """.toformat [format] <reply to audio>
           Сконвертировать аудио/видео/войс в нужный формат
        Поддерживаются mp3, m4a, ogg, mpeg, wav, oga
        """
        frmts = ["ogg", "mpeg", "mp3", "wav", "oga", "m4a", "3gp"]
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("А где реплай?")
            return
        else:
            try:
                reply.media.document.attributes[0].duration
                if utils.get_args_raw(message):
                    if utils.get_args_raw(message) not in frmts:
                        await message.edit(
                            f"Формат {utils.get_args_raw(message)} для конвертирования"
                            " не поддерживается!"
                        )
                        return
                    formatik = utils.get_args_raw(message)
                else:
                    await message.edit("Укажите формат конвертирования")
                    return
            except:
                await message.edit("Это не аудиофайл!")
                return
        await message.edit("[Audio Converter] Скачиваем...")
        au = io.BytesIO()
        await message.client.download_media(reply.media.document, au)
        au.seek(0)
        await message.edit(f"[AudioConverter] Конвертируем в {formatik}...")
        audio = AudioSegment.from_file(au)
        m = io.BytesIO()
        m.name = "Converted_to." + formatik
        audio.split_to_mono()
        await message.edit("[AudioConverter] Экспортируем...")
        audio.export(m, format=formatik)
        await message.edit("[Audio Converter] Отправляем...")
        m.seek(0)
        await message.client.send_file(
            message.to_id,
            m,
            reply_to=reply.id,
            attributes=[
                types.DocumentAttributeAudio(
                    duration=reply.document.attributes[0].duration,
                    title=f"Converted to " + formatik,
                    performer="@Sekai_Yoneya",
                )
            ],
        )
        await message.delete()
