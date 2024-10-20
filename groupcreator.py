# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: groupcreator
# Description: Создать чат или канал.
# Author: Fl1yd
# Commands:
# .create
# ---------------------------------------------------------------------------------


from telethon.errors import UserRestrictedError
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.messages import (
    CreateChatRequest,
    DeleteChatUserRequest,
    ExportChatInviteRequest,
)

from .. import loader, utils


def register(cb):
    cb(GroupCreatorMod())


class GroupCreatorMod(loader.Module):
    """Создать чат или канал."""

    strings = {"name": "GroupCreator"}

    async def createcmd(self, message):
        """Используй .create <g|s|c> <название>, чтобы создать группу, супергруппу или канал."""
        args = utils.get_args_raw(message).split(" ")
        try:
            title = utils.get_args_raw(message).split(" ", 1)[1]
            if "g" in args[0]:
                r = await message.client(
                    CreateChatRequest(users=["missrose_bot"], title=title)
                )
                created_chat = r.chats[0].id
                await message.client(
                    DeleteChatUserRequest(chat_id=created_chat, user_id="@missrose_bot")
                )
            elif "s" in args[0]:
                r = await message.client(
                    CreateChannelRequest(title=title, about="", megagroup=True)
                )
            elif "c" in args[0]:
                r = await message.client(
                    CreateChannelRequest(title=title, about="", megagroup=False)
                )
            created_chat = r.chats[0].id
            result = await message.client(ExportChatInviteRequest(peer=created_chat))
            await message.edit(
                f'<b>Группа "{title}" создана.\nЛинк: {result.link}.</b>'
            )
        except IndexError:
            return await message.edit("<b>Неверно указаны аргументы.</b>")
        except UnboundLocalError:
            return await message.edit("<b>Неверно указаны аргументы.</b>")
        except UserRestrictedError:
            return await message.edit(
                "<b>У вас спамбан, вы не можете создавать каналы или группы.</b>"
            )
