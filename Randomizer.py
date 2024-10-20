# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Randomizer
# Author: D4n13l3k00
# Commands:
# .rndint | .rndelm | .rnduser
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


import random
import re

from .. import loader, utils  # type: ignore


@loader.tds
class RandomizerMod(loader.Module):
    strings = {"name": "Рандомайзер"}
    prefix = "<b>[Рандомайзер]</b>\n"

    @loader.owner
    async def rndintcmd(self, m):
        ".rndint <int> <int> - рандомное число из заданногоо диапозона"
        args = utils.get_args_raw(m)
        check = re.compile(r"^(\d+)\s+(\d+)$")
        if check.match(args):
            fr, to = check.match(args).groups()
            if int(fr) < int(to):
                rndint = random.randint(int(fr), int(to))
                await m.edit(
                    self.prefix
                    + "<b>Режим:</b> Рандомное число из диапозона\n<b>Диапозон:</b>"
                    f" <code>{fr}-{to}</code>\n<b>Выпало число:</b>"
                    f" <code>{rndint}</code>"
                )
            else:
                await m.edit(f"{self.prefix}Вася, укажи диапозон чисел!")
        else:
            await m.edit(f"{self.prefix}Вася, укажи диапозон чисел!")

    @loader.owner
    async def rndelmcmd(self, m):
        ".rndelm <элементы через запятую> - рандомный элемент из списка"
        args = utils.get_args_raw(m)
        if not args:
            await m.edit(f"{self.prefix}Вася, напиши список элементов через запятую!")
            return
        lst = [i.strip() for i in args.split(",") if i]
        await m.edit(
            self.prefix
            + "<b>Режим:</b> Рандомный элемент из списка\n<b>Список:</b>"
            f" <code>{', '.join(lst)}</code>\n<b>Выпало:</b>"
            f" <code>{random.choice(lst)}</code>"
        )

    @loader.owner
    async def rndusercmd(self, m):
        ".rnduser - выбор рандомного юзера из чата"
        if not m.chat:
            await m.edit(f"{self.prefix}<b>Это не чат</b>")
            return
        users = await m.client.get_participants(m.chat)
        user = random.choice(users)
        await m.edit(
            self.prefix
            + "<b>Режим:</b> Рандомный юзер из чата\n<b>Юзер:</b> <a"
            f' href="tg://user?id={user.id}">{user.first_name}</a> |'
            f" <code>{user.id}</code>"
        )
