# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: hearts
# Description: No description
# Author: KeyZenD
# Commands:
# .hearts
# ---------------------------------------------------------------------------------


from asyncio import sleep

from .. import loader


@loader.tds
class HeartsMod(loader.Module):
    strings = {"name": "Heart's"}

    @loader.owner
    async def heartscmd(self, message):
        for _ in range(10):
            for heart in ["❤", "️🧡", "💛", "💚", "💙", "💜"]:
                await message.edit(heart)
                await sleep(0.3)
