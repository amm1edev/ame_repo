# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: BFGMod
# Description: Send mes
# Author: trololo65
# Commands:
# .bbton | .bbtoff | .bfgon | .bfgoff
# ---------------------------------------------------------------------------------


# meta developer: @trololo_1

from asyncio import sleep

from .. import loader, utils


class BFGMod(loader.Module):
    """Send mes"""

    strigs = {"name": "BFGMod"}

    async def client_ready(self, client, db):
        self.db = db

    async def bbtoncmd(self, message):
        """ """
        await utils.answer(message, "<b>Запущено</b>")
        status = self.db.set("BFGMod", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("BFGMod", "status1"):
                    return
                await message.respond("10")
                await sleep(2)
            status = self.db.get("BFGMod", "status1")
            await message.respond("🚀Оценивать")

    async def bbtoffcmd(self, message):
        """ """
        self.db.set("BFGMod", "status1", False)
        await utils.answer(message, "<b>Остановлено</b>")

    async def bfgoncmd(self, message):
        """ """
        await utils.answer(message, "<b>Запущено</b>")
        status = self.db.set("BFGMod", "status2", True)
        while status:
            await message.respond("копать материю")
            await sleep(60 * 5)
            status = self.db.get("BFGMod", "status2")
            if not status:
                return

    async def bfgoffcmd(self, message):
        """ """
        self.db.set("BFGMod", "status2", False)
        await utils.answer(message, "<b>Остановлено</b>")
