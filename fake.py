# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: fake
# Description: Показывает фейковые действия.
# Author: Fl1yd
# Commands:
# .fake
# ---------------------------------------------------------------------------------


from asyncio import sleep
from random import choice, randint

from .. import loader, utils


def register(cb):
    cb(FakeActionsMod())


class FakeActionsMod(loader.Module):
    """Показывает фейковые действия."""

    strings = {"name": "Fake Actions"}

    async def fakecmd(self, event):
        """Использование: .fake <действие>.\nСписок действий: typing, contact, game, location, record-audio, record-round, record-video, voice, round, video, photo, document.\nОтмена: .fake cancel"""
        options = [
            "typing",
            "contact",
            "game",
            "location",
            "record-audio",
            "record-round",
            "record-video",
            "voice",
            "round",
            "video",
            "photo",
            "document",
            "cancel",
        ]
        args = utils.get_args_raw(event).split()
        if len(args) == 0:
            fake_action = choice(options)
            fake_time = randint(30, 60)
        elif len(args) == 1:
            try:
                fake_action = str(args[0]).lower()
                fake_time = randint(30, 60)
            except ValueError:
                fake_action = choice(options)
                fake_time = int(args[0])
        elif len(args) == 2:
            fake_action = str(args[0]).lower()
            fake_time = int(args[1])
        else:
            return await event.edit("Неправильный ввод.")
        try:
            await event.delete()
            async with event.client.action(event.chat_id, fake_action):
                await sleep(fake_time)
        except BaseException:
            return
