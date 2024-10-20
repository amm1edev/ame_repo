# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: kickall-addusers
# Description: No description
# Author: SekaiYoneya
# Commands:
# .addusers | .kickall
# ---------------------------------------------------------------------------------


# @Sekai_Yoneya

import asyncio

from telethon import errors, events, functions

from .. import loader, utils


class addmembersMod(loader.Module):
    strings = {"name": "kickall & addusers"}

    async def adduserscmd(self, event):
        """Добавляет людей с чата в чат."""
        if len(event.text.split()) == 2:
            idschannelgroup = event.text.split(" ", maxsplit=1)[1]
            user = [
                i async for i in event.client.iter_participants(event.to_id.channel_id)
            ]
            await event.edit(
                f"<b>{len(user)} пользователей будет приглашено из чата"
                f" {event.to_id.channel_id} в чат/канал {idschannelgroup}</b>"
            )
            for u in user:
                try:
                    try:
                        if u.bot == False:
                            await event.client(
                                functions.channels.InviteToChannelRequest(
                                    idschannelgroup, [u.id]
                                )
                            )
                            await asyncio.sleep(1)
                        else:
                            pass
                    except:
                        pass
                except errors.FloodWaitError as e:
                    print("Flood for", e.seconds)
        else:
            await event.edit(f"<b>Куда приглашать будем?</b>")

    async def kickallcmd(self, event):
        """Удаляет всех пользователей из чата."""
        user = [i async for i in event.client.iter_participants(event.to_id.channel_id)]
        await event.edit(
            f"<b>{len(user)} пользователей будет кикнуто из чата"
            f" {event.to_id.channel_id}</b>"
        )
        for u in user:
            try:
                try:
                    if u.is_self != True:
                        await event.client.kick_participant(event.chat_id, u.id)
                        await asyncio.sleep(1)
                    else:
                        pass
                except:
                    pass
            except errors.FloodWaitError as e:
                print("Flood for", e.seconds)
