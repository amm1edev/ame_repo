# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the Copyleft license.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Silero
# Description: Silero Models: pre-trained speech-to-text, text-to-speech and text-enhancement models made embarrassingly simple
# Author: CakesTwix
# Commands:
# .sxenia | .saidar | .sbaya | .skseniya | .srandom
# ---------------------------------------------------------------------------------


"""

    █▀▀ ▄▀█ █▄▀ █▀▀ █▀ ▀█▀ █░█░█ █ ▀▄▀
    █▄▄ █▀█ █░█ ██▄ ▄█ ░█░ ▀▄▀▄▀ █ █░█

    Copyleft 2022 t.me/CakesTwix
    This program is free software; you can redistribute it and/or modify

"""

__version__ = (1, 1, 1)

# requires: torch
# meta pic: https://cdn.pixabay.com/photo/2017/07/09/20/48/speaker-2488096_1280.png
# meta developer: @cakestwix_mods
# scope: hikka_only

import logging
import os
import re

import aiohttp
import torch

from .. import loader, utils

logger = logging.getLogger(__name__)

device = torch.device("cpu")
torch.set_num_threads(4)


@loader.tds
class SileroMod(loader.Module):
    """Silero Models: pre-trained speech-to-text, text-to-speech and text-enhancement models made embarrassingly simple"""

    strings = {
        "name": "Silero",
        "cfg_as_audio_note": "Send audio as a voice message",
        "cfg_rate": "Sound frequency",
        "no_avx2": "Your server does not support AVX2 instructions.",
    }

    strings_ru = {
        "name": "Silero",
        "cfg_as_audio_note": "Отправлять аудио как голосовые сообщения",
        "cfg_rate": "Частота звука",
        "no_avx2": "Твой сервер не поддерживает AVX2 инструкции",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "CONFIG_AS_AUDIO_NOTE",
            True,
            lambda: self.strings("cfg_as_audio_note"),
            "CONFIG_RATE",
            48000,
            lambda: self.strings("cfg_rate"),
        )

    async def client_ready(self, client, db) -> None:
        with open("/proc/cpuinfo") as f:
            if "avx2" not in f.read():
                raise loader.LoadError(self.strings["no_avx2"])

        if not os.path.isfile(os.path.abspath(os.getcwd()) + "/assets/model.pt"):
            torch.hub.download_url_to_file(
                "https://models.silero.ai/models/tts/ru/ru_v3.pt", "assets/model.pt"
            )

        self.model = torch.package.PackageImporter("assets/model.pt").load_pickle(
            "tts_models", "model"
        )
        self.model.to(device)

    async def send_audio(self, text: str, speaker: str, message):
        audio_paths = self.model.save_wav(
            text=text, speaker=speaker, sample_rate=self.config["CONFIG_RATE"]
        )

        with open(audio_paths, "rb") as audio_file:
            content = audio_file.read()
            audio_file.seek(0)

            await self._client.send_file(
                message.chat.id,
                audio_file,
                voice_note=self.config["CONFIG_AS_AUDIO_NOTE"],
                reply_to=await message.get_reply_message(),
            )

    async def sxeniacmd(self, message):
        """From text to sound (xenia)"""
        if args := utils.get_args_raw(message):
            await message.delete()
            await self.send_audio(args, "xenia", message)

    async def saidarcmd(self, message):
        """From text to sound (aidar)"""
        if args := utils.get_args_raw(message):
            await message.delete()
            await self.send_audio(args, "aidar", message)

    async def sbayacmd(self, message):
        """From text to sound (baya)"""
        if args := utils.get_args_raw(message):
            await message.delete()
            await self.send_audio(args, "baya", message)

    async def skseniyacmd(self, message):
        """From text to sound (kseniya)"""
        if args := utils.get_args_raw(message):
            await message.delete()
            await self.send_audio(args, "kseniya", message)

    async def srandomcmd(self, message):
        """From text to sound (random)"""
        if args := utils.get_args_raw(message):
            await message.delete()
            await self.send_audio(args, "random", message)
