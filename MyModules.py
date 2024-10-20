# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MyModules
# Author: DarkModules
# Commands:
# .mymodules
# ---------------------------------------------------------------------------------

# The MIT License (MIT)
# Copyright (c) 2022 penggrin

# meta developer: @penggrinmods
# scope: hikka_only

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MyModulesMod(loader.Module):
    """List of all of the modules currently installed, without all of that annoying crap. In just one simple message!"""

    strings = {
        "name": "MyModules",
        "amount": "❤️ I have <b>{}</b> modules installed.",
        "modules": "❤️ Here is all of them:",
    }

    strings_ru = {
        "amount": "❤️ У меня установлено <b>{}</b> модулей.",
        "modules": "❤️ Все они здесь:",
    }

    @loader.command(ru_doc="Показать все установленные модули")
    async def mymodulescmd(self, message):
        """- List of all of the modules currently installed"""

        result = (
            f"{self.strings('amount').format(str(len(self.allmodules.modules)))}\n{self.strings('modules')} | "
        )

        for mod in self.allmodules.modules:
            try:
                name = mod.strings["name"]
            except KeyError:
                name = mod.__clas__.__name__
            result += f"<code>{name}</code> | "

        await utils.answer(message, result)
