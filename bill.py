# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: bill
# Author: Ijidishurka
# Commands:
# .billy
# ---------------------------------------------------------------------------------

# канал @modwini
from .. import loader


@loader.tds
class billy(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "Billy"}

    async def billycmd(self, message):
        """Отправляет видео сообщение"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://telesco.pe/kruglishik/31",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
