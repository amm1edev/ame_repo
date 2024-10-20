# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Frazes
# Description: Госу, пикапы, подкаты.
# Author: SekaiYoneya
# Commands:
# .gosu | .pikap | .podkat | .ayf
# ---------------------------------------------------------------------------------


# by @Sekai_Yoneya

import random
from asyncio import sleep

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register

from .. import loader, utils


def register(cb):
    cb(FrazesMod())


class FrazesMod(loader.Module):
    """Госу, пикапы, подкаты."""

    strings = {"name": "Фразы"}

    def init(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def gosucmd(self, event):
        """Выебать чью-то мамку"""
        chat = "@yoneyabs_bot"
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1705701465)
                )
                await event.client.send_message(chat, "/gosu")
                response = await response
            except YouBlockedUserError:
                await event.edit("<code>Разблокируй @YoneyaBS_bot</code>")
                return
            await event.edit(response.text)

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def pikapcmd(self, event):
        """Пикап"""
        chat = "@yoneyabs_bot"
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1705701465)
                )
                await event.client.send_message(chat, "/pikap")
                response = await response
            except YouBlockedUserError:
                await event.edit("<code>Разблокируй @YoneyaBS_bot</code>")
                return
            await event.edit(response.text)

    async def podkatcmd(self, event):
        """Подкат"""
        chat = "@yoneyabs_bot"
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1705701465)
                )
                await event.client.send_message(chat, "/podkat")
                response = await response
            except YouBlockedUserError:
                await event.edit("<code>Разблокируй @YoneyaBS_bot</code>")
                return
            await event.edit(response.text)

    async def ayfcmd(self, event):
        """АУФ!!!"""
        chat = "@yoneyabs_bot"
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1705701465)
                )
                await event.client.send_message(chat, "/ayf")
                response = await response
            except YouBlockedUserError:
                await event.edit("<code>Разблокируй @YoneyaBS_bot</code>")
                return
            await event.edit(response.text)
