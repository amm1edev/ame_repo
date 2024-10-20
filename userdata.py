# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: userdata
# Description: Модуль может изменить ваши данные в Telegram
# Author: Fl1yd
# Commands:
# .name | .bio | .username
# ---------------------------------------------------------------------------------


import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest

from .. import loader, utils


def register(cb):
    cb(UserDataMod())


class UserDataMod(loader.Module):
    """Модуль может изменить ваши данные в Telegram"""

    strings = {"name": "UserData"}

    async def namecmd(self, message):
        """Команда .name изменит ваше имя."""
        args = utils.get_args_raw(message).split("/")
        if not args:
            return await message.edit("Нет аргументов.")
        if len(args) == 1:
            firstname = args[0]
            lastname = " "
        elif len(args) == 2:
            firstname = args[0]
            lastname = args[1]
        await message.client(
            UpdateProfileRequest(first_name=firstname, last_name=lastname)
        )
        await message.edit("Имя изменено успешно!")

    async def biocmd(self, message):
        """Команда .bio изменит ваше био."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit("Нет аргументов.")
        await message.client(UpdateProfileRequest(about=args))
        await message.edit("Био изменено успешно!")

    async def usernamecmd(self, message):
        """Команда .username изменит ваше био."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit("Нет аргументов.")
        try:
            await message.client(UpdateUsernameRequest(args))
            await message.edit("Юзернейм изменен успешно!")
        except UsernameOccupiedError:
            await message.edit("Такой юзернейм уже занят!")
