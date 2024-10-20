# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: warn
# Description: Система предупреждений.
# Author: GeekTG
# Commands:
# .warn | .warnslimit | .warns | .swarn | .clearwarns
# ---------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

# Module author: @ftgmodulesbyfl1yd

from telethon.errors import UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from .. import loader, utils


@loader.tds
class WarnsMod(loader.Module):
    """Система предупреждений."""

    strings = {"name": "Warns"}

    async def client_ready(self, client, db):
        self.db = db

    async def warncmd(self, message):
        """Выдать варн. Используй: .warn <@ или реплай>."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        chat = await message.get_chat()
        if not chat.admin_rights and not chat.creator:
            return await message.edit("<b>Я не админ здесь.</b>")
        else:
            if not chat.admin_rights.ban_users:
                return await message.edit("<b>У меня нет нужных прав.</b>")

        warns = self.db.get("Warns", "warns", {})
        args = utils.get_args(message)
        reply = await message.get_reply_message()
        chatid = str(message.chat_id)
        reason = "Необоснованно"

        if not args and not reply:
            return await message.edit("<b>Нет аргументов или реплая.</b>")

        if reply:
            user = await message.client.get_entity(reply.sender_id)
            args = utils.get_args_raw(message)
            if args:
                reason = args
        else:
            user = await message.client.get_entity(
                args[0] if not args[0].isnumeric() else int(args[0])
            )
            if args:
                if len(args) == 1:
                    args = utils.get_args_raw(message)
                    user = await message.client.get_entity(
                        args if not args.isnumeric() else int(args)
                    )
                elif len(args) >= 2:
                    reason = utils.get_args_raw(message).split(" ", 1)[1]
        userid = str(user.id)
        me = await message.client.get_me()
        if me.id == user.id:
            return await message.edit("<b>Ты не можешь себе давать предупреждение!</b>")

        if chatid not in warns:
            warns.update({chatid: {"limit": 3, "action": "ban"}})
        if userid not in warns[chatid]:
            warns[chatid].update({userid: []})

        if not args and not reply:
            return await message.edit("<b>Нет аргументов или реплая.</b>")

        warns[chatid][userid].append(reason)
        count = len(warns[chatid][userid])

        if count == warns[chatid]["limit"]:
            warns[chatid].pop(userid)
            self.db.set("Warns", "warns", warns)
            try:
                if warns[chatid]["action"] == "kick":
                    await message.client.kick_participant(int(chatid), user.id)
                elif warns[chatid]["action"] == "ban":
                    await message.client(
                        EditBannedRequest(
                            int(chatid),
                            user.id,
                            ChatBannedRights(until_date=None, view_messages=True),
                        )
                    )
                elif warns[chatid]["action"] == "mute":
                    await message.client(
                        EditBannedRequest(
                            int(chatid),
                            user.id,
                            ChatBannedRights(until_date=True, send_messages=True),
                        )
                    )
            except UserAdminInvalidError:
                return await message.edit("<b>У меня нет достаточных прав.</b>")
            else:
                return await message.edit(
                    f"<b>{user.first_name} получил"
                    f" {count}/{warns[chatid]['limit']} предупреждения, и был ограничен"
                    " в чате.</b>"
                )
        self.db.set("Warns", "warns", warns)
        await message.edit(
            f'<b><a href="tg://user?id={user.id}">{user.first_name}</a> получил'
            f' {count}/{warns[chatid]["limit"]} предупреждений.</b>'
            + (f"\nПричина: {reason}.</b>" if reason != "Необоснованно" else "")
        )

    async def warnslimitcmd(self, message):  # sourcery skip: last-if-guard
        """Установить лимит предупреждений. Используй: .warnslimit <кол-во:int>."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")

        warns = self.db.get("Warns", "warns", {})
        args = utils.get_args_raw(message)
        chatid = str(message.chat_id)

        if chatid not in warns:
            warns.update({chatid: {"limit": 3}})
        if not args:
            return await message.edit(
                f"<b>Лимит предупреждений в этом чате: {warns[chatid]['limit']}</b>"
            )

        try:
            warns[chatid].update({"limit": int(args)})
            self.db.set("Warns", "warns", warns)
            return await message.edit(
                "<b>Лимит предупреждений в этом чате был установлен на:"
                f" {warns[chatid]['limit']}</b>"
            )
        except ValueError:
            return await message.edit("Значение должно быть числом.")

    async def warnscmd(self, message):
        """Посмотреть кол-во варнов. Используй: .warns <@ или реплай> или <list>."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        chatid = str(message.chat_id)
        warns = self.db.get("Warns", "warns", {})

        if not args and not reply:
            return await message.edit("<b>Нет аргументов или реплая.</b>")

        if args == "list":
            users = ""
            try:
                for _ in warns[chatid]:
                    if _ not in ["limit", "action"]:
                        user = await message.client.get_entity(int(_))
                        users += (
                            f"• <a href='tg://user?id={int(_)}'>{user.first_name}</a>"
                            f" <b>| [</b><code>{_}</code><b>]</b>\n"
                        )
                return await message.edit(
                    f"<b>Список тех, кто получил предупреждения:\n\n{users}"
                )
            except KeyError:
                return await message.edit(
                    "<b>В этом чате никто не получал предупреждения.</b>"
                )

        try:
            if args:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            else:
                user = await message.client.get_entity(reply.sender_id)
            userid = str(user.id)
        except ValueError:
            return await message.edit("<b>Не удалось найти этого пользователя.</b>")

        try:
            if userid not in warns[chatid]:
                return await message.edit(
                    "<b>Этот пользователь не получал предупреждения.</b>"
                )

            msg = "".join(
                f"<b>{count})</b> {_}\n"
                for count, _ in enumerate(warns[chatid][userid], start=1)
            )
            return await message.edit(
                "<b>Предупреждения <a"
                f' href="tg://user?id={user.id}">{user.first_name}</a>:\n\n{msg}</b>'
            )
        except KeyError:
            return await message.edit(
                f'<b>У <a href="tg://user?id={user.id}">{user.first_name}</a> нет'
                " предупреждений.</b>"
            )

    async def swarncmd(self, message):
        """Изменить режим ограничения. Используй: .swarn <kick/ban/mute/none>."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        args = utils.get_args_raw(message)
        chatid = str(message.chat_id)
        warns = self.db.get("Warns", "warns", {})

        if chatid not in warns:
            warns.update({chatid: {"action": "ban"}})

        if args:
            if args == "kick":
                warns[chatid].update({"action": "kick"})
            elif args == "ban":
                warns[chatid].update({"action": "ban"})
            elif args == "mute":
                warns[chatid].update({"action": "mute"})
            elif args == "none":
                warns[chatid].update({"action": "none"})
            else:
                return await message.edit(
                    "<b>Такого режима нет в списке.\nДоступные режимы:"
                    " kick/ban/mute/none.</b>"
                )
            self.db.set("AntiMention", "action", warns)
            return await message.edit(
                "<b>Теперь при достижения лимита предупреждений будет выполняться"
                f" действие: {warns[chatid]['action']}.</b>"
            )
        else:
            return await message.edit(
                "<b>При достижения лимита предупреждений будет выполняться действие:"
                f" {warns[chatid]['action']}.</b>"
            )

    async def clearwarnscmd(self, message):
        """Очистить все варны. Используй: .clearwarns <@ или реплай>."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        chatid = str(message.chat_id)
        warns = self.db.get("Warns", "warns", {})
        if not args and not reply:
            return await message.edit("<b>Нет аргументов или реплая.</b>")

        try:
            if args:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            else:
                user = await message.client.get_entity(reply.sender_id)
            userid = str(user.id)
        except ValueError:
            return await message.edit("<b>Не удалось найти этого пользователя.</b>")

        try:
            warns[chatid][userid].pop()
            if len(warns[chatid][userid]) == 0:
                warns[chatid].pop(userid)
            self.db.set("Warns", "warns", warns)
            return await message.edit(
                f'<b>У <a href="tg://user?id={user.id}">{user.first_name}</a> удалено'
                " последнее предупреждение.</b>"
            )
        except KeyError:
            return await message.edit(
                f'<b>У <a href="tg://user?id={user.id}">{user.first_name}</a> нет'
                " предупреждений.</b>"
            )
