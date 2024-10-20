# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: hearts
# Description: No description
# Author: Fl1yd
# Commands:
# .lhearts | .shearts
# ---------------------------------------------------------------------------------


from asyncio import sleep

from .. import loader


@loader.tds
class HeartsMod(loader.Module):
    strings = {"name": "Heart's"}

    @loader.owner
    async def lheartscmd(self, message):
        for _ in range(10):
            for lheart in ["❤", "️🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍"]:
                await message.edit(lheart)
                await sleep(3)

    async def sheartscmd(self, message):
        for _ in range(10):
            for sheart in ["❤", "️🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍"]:
                await message.edit(sheart)
                await sleep(0.3)
