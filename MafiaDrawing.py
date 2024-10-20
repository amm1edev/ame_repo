# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MafiaDrawing
# Description: Модуль ловли подарков в True Mafia News.
# Author: Yahikoro
# Commands:
# .md
# ---------------------------------------------------------------------------------


from .. import loader, utils


class MafiaDrawingMod(loader.Module):
    """Модуль ловли подарков в True Mafia News."""

    strings = {"name": "MafiaDrawing"}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("MafiaDrawing", "status", True)

    async def mdcmd(self, message):
        """Используй: .md чтобы включить/выключить ловлю подарков."""
        status = self.db.get("MafiaDrawing", "status")
        if status is not True:
            await message.edit("<b>Ловля подарков:</b> <code>Включена</code>")
            self.db.set("MafiaDrawing", "status", True)
        else:
            await message.edit("<b>Ловля подарков:</b> <code>Отключена</code>")
            self.db.set("MafiaDrawing", "status", False)

    async def watcher(self, message):
        try:
            status = self.db.get("MafiaDrawing", "status")
            me = (await message.client.get_me()).id
            if status:
                if message.chat_id == -1001169391811:
                    click = (await message.click(0)).message
                    await message.client.send_message(
                        me, f"Словлен подарок:\n\n{click}"
                    )
        except:
            pass
