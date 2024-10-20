# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: cheval
# Description: Выполняет команду в канале
# Author: KeyZenD
# Commands:
# .cheval
# ---------------------------------------------------------------------------------


from .. import loader, utils


class channelEvalMod(loader.Module):
    """Выполняет команду в канале"""

    strings = {"name": "ChannelEval"}

    async def chevalcmd(self, message):
        """.channel <канал> <id сообщения реплая, или же выполнение команды из комментариев> <комманда в том виде, в котором бы ты отправил её в чат>"""
        args = utils.get_args(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit("<b>Укажи канал.</b>")
        if len(args) < 1:
            return await message.edit("<b>Укажи команду для выполнения.</b>")
        channel = args[0]
        args = args[1:]
        if not args[0].isdigit() and reply:
            rmsg = (
                reply.fwd_from.saved_from_msg_id if (reply and reply.fwd_from) else None
            )
            fullcmd = " ".join(args)
        elif args[0].isdigit():
            rmsg = int(args[0])
            fullcmd = " ".join(args[1:])
        else:
            rmsg = None
            fullcmd = " ".join(args)

        cmd = fullcmd.split(" ")[0]
        if cmd.startswith("."):
            cmd = cmd[1:]
        if channel.isdigit():
            channel = int(channel)
        if not cmd in self.allmodules.commands.keys():
            return await message.edit(
                "<b>Кажется у тебя нет в списке команды </b><code>."
                + cmd
                + "\n</code><b>Кстати сокращения команд я не понимяу)\n<code>"
                + message.raw_text
                + "</code>"
            )

        try:
            m = await message.client.send_message(channel, fullcmd, reply_to=rmsg)
        except Exception as e:
            return await message.edit("<b>Возникла ошибка:</b>\n" + repr(e))
        await self.allmodules.commands[cmd](m)
        try:
            url = f"https://t.me/c/{m.to_id.channel_id}/{m.id}"
        except:
            url = ""
        await message.edit(f'<a href="{url}">Команда отправлена!</a>')
