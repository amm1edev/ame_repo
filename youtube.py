# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: youtube
# Description: Download YouTube video
# Author: hikariatama
# Commands:
# .yt
# ---------------------------------------------------------------------------------


#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_min 1.2.10

# meta pic: https://img.icons8.com/plasticine/400/000000/youtube-play--v2.png
# meta banner: https://mods.hikariatama.ru/badges/youtube.jpg
# meta developer: @hikarimods
# scope: hikka_only
# scope: ffmpeg
# requires: pytube python-ffmpeg

import os
import subprocess

from pytube import YouTube
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class YouTubeMod(loader.Module):
    """Download YouTube video"""

    strings = {
        "name": "YouTube",
        "args": "🎞 <b>You need to specify link</b>",
        "downloading": "🎞 <b>Downloading...</b>",
        "not_found": "🎞 <b>Video not found...</b>",
    }

    strings_ru = {
        "args": "🎞 <b>Укажи ссылку на видео</b>",
        "downloading": "🎞 <b>Скачиваю...</b>",
        "not_found": "🎞 <b>Видео не найден...</b>",
        "_cmd_doc_yt": "[mp3] <ссылка> - Скачать видео YouTube",
        "_cls_doc": "Скачать YouTube видео",
    }

    @loader.unrestricted
    async def ytcmd(self, message: Message):
        """[mp3] <link> - Download video from youtube"""
        args = utils.get_args_raw(message)
        message = await utils.answer(message, self.strings("downloading"))

        ext = False
        if len(args.split()) > 1:
            ext, args = args.split(maxsplit=1)

        if not args:
            return await utils.answer(message, self.strings("args"))

        def dlyt(videourl, path):
            yt = YouTube(videourl)
            yt = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            return yt.download(path)

        def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
            filename, ext = os.path.splitext(video_file)
            out = f"{filename}.{output_ext}"
            subprocess.call(
                ["ffmpeg", "-y", "-i", video_file, out],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
            )
            os.remove(video_file)
            return out

        path = "/tmp"
        try:
            path = await utils.run_sync(dlyt, args, path)
        except Exception:
            await utils.answer(message, self.strings("not_found"))
            return

        if ext == "mp3":
            path = convert_video_to_audio_ffmpeg(path)

        await self._client.send_file(message.peer_id, path)
        os.remove(path)

        if message.out:
            await message.delete()
