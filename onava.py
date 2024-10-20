# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: onava
# Description: Гифку/видео/стикер на аву.
# Author: Fl1yd
# Commands:
# .onava | .togif
# ---------------------------------------------------------------------------------


import os

from telethon import functions

from .. import loader, utils


def register(cb):
    cb(OnAvaMod())


class OnAvaMod(loader.Module):
    """Гифку/видео/стикер на аву."""

    strings = {"name": "OnAva"}

    async def onavacmd(self, message):
        """Установить на аву гифку/видео/стикер.\nИспользование: .onava <реплай>."""
        try:
            reply = await message.get_reply_message()
            if reply:
                await message.edit("Скачиваем...")
                if reply.video:
                    await message.client.download_media(reply.media, "ava.mp4")
                    await message.edit("Конвертируем...")
                    os.system("ffmpeg -i ava.mp4 -c copy -an gifavaa.mp4 -y")
                    os.system("ffmpeg -i gifavaa.mp4 -vf scale=360:360 gifava.mp4 -y")
                else:
                    await message.client.download_media(reply.media, "tgs.tgs")
                    await message.edit("Конвертируем...")
                    os.system(
                        "lottie_convert.py tgs.tgs tgs.gif; mv tgs.gif gifava.mp4"
                    )
            else:
                return await message.edit(
                    "Нет реплая на гиф/анимированный стикер/видеосообщение."
                )
            await message.edit("Устанавливаем аву...")
            await message.client(
                functions.photos.UploadProfilePhotoRequest(
                    video=await message.client.upload_file("gifava.mp4"),
                    video_start_ts=0.0,
                )
            )
            await message.edit("Ава установлена.")
            os.system("rm -rf ava.mp4 gifava.mp4 gifavaa.mp4 tgs.tgs tgs.gif")
        except:
            await message.edit("Произошла непредвиденная ошибка.")
            os.system("rm -rf ava.mp4 gifava.mp4 gifavaa.mp4 tgs.tgs tgs.gif")
            return

    async def togifcmd(self, message):
        """Сделать из медиа гифку.\nИспользование: .togif <реплай>."""
        try:
            await message.edit("Скачиваем...")
            reply = await message.get_reply_message()
            if reply:
                if reply.video:
                    await message.client.download_media(reply.media, "inputfile.mp4")
                    await message.edit("Конвертируем...")
                    os.system("ffmpeg -i inputfile.mp4 -vcodec copy -an outputfile.mp4")
                    await message.edit("Отправляем...")
                    await message.client.send_file(message.to_id, "outputfile.mp4")
                elif reply.file.ext == ".tgs":
                    await message.client.download_media(reply.media, f"tgs.tgs")
                    await message.edit("Конвертируем...")
                    os.system("lottie_convert.py tgs.tgs tgs.gif")
                    await message.edit("Отправляем...")
                    await message.client.send_file(
                        message.to_id, "tgs.gif", reply_to=reply.id
                    )
                else:
                    return await message.edit("Этот файл не поддерживается.")
                await message.delete()
                os.system("rm -rf inputfile.mp4 outputfile.mp4 tgs.tgs tgs.gif")
            else:
                return await message.edit("Нет реплая на видео/гиф/стикр.")
        except:
            await message.edit("Произошла непредвиденная ошибка.")
            os.system("rm -rf inputfile.mp4 outputfile.mp4 tgs.tgs tgs.gif")
            return
