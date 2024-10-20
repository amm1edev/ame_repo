# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: voiceGirlsV4
# Author: Ijidishurka
# Commands:
# .пр      | .кд  | .прив  | .норм | .нуи
# .хорошо  | .аня | .мне19 | .хз   | .непон
# .го      | .да  | .нуда  | .что  | .куда
# .спок    | .кн  | .добр  | .пока | .прощай
# .сладких | .лан | .пж    | .дядя | .хм
# ---------------------------------------------------------------------------------

# meta developer: @modwini
from telethon.tl.functions.channels import JoinChannelRequest

from .. import loader


@loader.tds
class voiceGirls3(loader.Module):
    """Голосовые сообщения девушек"""

    strings = {"name": "voiceGirls3"}

    async def прcmd(self, message):
        """| Привет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/335",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кдcmd(self, message):
        """| Как дела?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/336",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def привcmd(self, message):
        """| Приветик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/337",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нормcmd(self, message):
        """| Все нормально"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/338",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нуиcmd(self, message):
        """| Ну и что"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/339",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хорошоcmd(self, message):
        """| Хорошо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/340",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def аняcmd(self, message):
        """| Я Аня"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/341",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def мне19cmd(self, message):
        """| Мне 19 лет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/342",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хзcmd(self, message):
        """| не знаю"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/343",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def непонcmd(self, message):
        """| Не поняла"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/344",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def гоcmd(self, message):
        """| Ну давай"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/345",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def даcmd(self, message):
        """| Да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/346",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нудаcmd(self, message):
        """| Ну да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/347",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def чтоcmd(self, message):
        """| Что?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/348",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кудаcmd(self, message):
        """| Куда?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/349",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def спокcmd(self, message):
        """| Спокойной ночи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/350",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кнcmd(self, message):
        """| Как настроение?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/351",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def добрcmd(self, message):
        """| Доброе утро"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/352",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def покаcmd(self, message):
        """| Пока"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/353",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def прощайcmd(self, message):
        """| Прощай"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/354",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сладкихcmd(self, message):
        """| Сладких снов"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/355",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ланcmd(self, message):
        """| Ну ладно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/356",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пжcmd(self, message):
        """| Ну пожалуйста"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/357",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def дядяcmd(self, message):
        """| Дядя не надо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/358",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def хмcmd(self, message):
        """| хмммм"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/359",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
