# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: leave
# Description: No description
# Author: KeyZenD
# Commands:
# .leave
# ---------------------------------------------------------------------------------


from asyncio import sleep

from telethon.tl.functions.channels import LeaveChannelRequest

from .. import loader, utils


@loader.tds
class LeaveMod(loader.Module):
    strings = {"name": "Just leave"}

    @loader.sudo
    async def leavecmd(self, message):
        """.leave"""
        if not message.chat:
            await message.edit("<b>Дурка блять</b>")
            return
        text = utils.get_args_raw(message)
        if not text:
            text = "До связи."
        if text.lower() == "del":
            await message.delete()
        else:
            await message.edit(f"<b>{text}</b>")
        await sleep(1)
        await message.client(LeaveChannelRequest(message.chat_id))
