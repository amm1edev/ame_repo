# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: GitUploader
# Description: Загружает файлы на репозиторий GitHub
# Author: Yahikoro
# Commands:
# .gitadd
# ---------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

import base64
import json
import logging
import os

import requests
from requests.exceptions import ChunkedEncodingError, MissingSchema

from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(GitaddMod())


@loader.tds
class GitaddMod(loader.Module):
    """Загружает файлы на репозиторий GitHub"""

    strings = {
        "name": "GitUploader",
        "reply_to_file": "<b>Ответьте на файл</b>",
        "error_file": "Формат не поддерживается",
        "connection_error": "<i>Ошибка соединения</i>",
        "repo_error": "<i>Ошибка репозитория</i>",
        "token_error": "<i>Ошибка токена</i>",
        "exist_422": (
            "<b>Не удалось загрузить файл. Возможная причина: файл с таким названием"
            " уже существует в репозитории.</b>"
        ),
        "cfg_token": "Токен GitHub",
        "token_not_found": "Токен не найден",
        "username_not_found": "Имя пользователя GitHub не указано",
        "repo_not_found": "Репозиторий не указан",
        "cfg_gh_user": "Имя пользователя на GitHub",
        "cfg_gh_repo": "Репозиторий, куда нужно загружать модули",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "GH_TOKEN",
            "TOKEN",
            lambda m: self.strings("cfg_token", m),
            "GH_USERNAME",
            "USERNAME",
            lambda m: self.strings("cfg_gh_user", m),
            "GH_REPO",
            "REPOSITORY",
            lambda m: self.strings("cfg_gh_repo", m),
        )

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def gitaddcmd(self, message):
        if self.config["GH_TOKEN"] == "TOKEN":
            await utils.answer(message, self.strings("token_not_found", message))
            return
        if self.config["GH_USERNAME"] == "USERNAME":
            await utils.answer(message, self.strings("username_not_found", message))
            return
        if self.config["GH_REPO"] == "REPOSITORY":
            await utils.answer(message, self.strings("repo_not_found", message))
            return
        reply = await message.get_reply_message()
        if not reply:
            await utils.answer(message, self.strings("reply_to_file", message))
            return
        media = reply.media
        if not media:
            await utils.answer(message, self.strings("reply_to_file", message))
            return
        try:
            fname = (reply.media.document.attributes[0]).file_name
        except AttributeError:
            await utils.answer(message, self.strings("error_file", message))
            return
        try:
            file = await message.client.download_file(media)
            encoded_string = base64.b64encode(file)
            stout = encoded_string.decode("utf-8")
            TOKEN = self.config["GH_TOKEN"]
            USERNAME = self.config["GH_USERNAME"]
            REPO = self.config["GH_REPO"]
            # url = f'{self.config["GH_REPO"]}{fname}'
            url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{fname}"
            head = {
                "Authorization": f"token {TOKEN}",
                "Accept": "application/vnd.github.v3+json",
            }
            git_data = '{"message": "Upload file", "content":' + '"' + stout + '"' + "}"
            r = requests.put(url, headers=head, data=git_data)
            if int(r.status_code) == 201:
                uploaded_to = f"https://github.com/{USERNAME}/{REPO}"
                uploaded_to_raw = "/".join(
                    r.json()["content"].get("download_url").split("/")[:-1]
                    + [fname.replace(" ", "%20")]
                )
                await utils.answer(
                    message,
                    (
                        f"Файл <code>{fname}</code> успешно загружен на <a"
                        f" href=\f'{uploaded_to}'>репозиторий!</a>\n\nПрямая ссылка:"
                        f" <code>{uploaded_to_raw}</code>"
                    ),
                )
                return
            elif int(r.status_code) == 422:
                await utils.answer(message, self.strings("exist_422", message))
                return
            else:
                json_resp = json.loads(r.text)
                git_resp = json_resp["message"]
                await utils.answer(
                    message,
                    (
                        "Произошла неизвестная ошибка! Ответ сервера:\n"
                        f" <code>{git_resp}</code>"
                    ),
                )
                return
        except ConnectionError:
            await utils.answer(message, self.strings("connection_error", message))
            return
        except MissingSchema:
            await utils.answer(message, self.strings("repo_error", message))
            return
        except ChunkedEncodingError:
            await utils.answer(message, self.strings("token_error", message))
            return
