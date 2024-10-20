# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: AnimeVoices
# Author: SkillsAngels
# Commands:
# .smexk    | .smexy  | .znay         | .madara  | .sharingan
# .imsasuke | .pain   | .ras          | .tensei  | .dazai    
# .gay      | .bankai | .sate         | .yoaimo  | .valhalla 
# .itachi   | .ghoul  | .best         | .requiem | .king     
# .equality | .forest | .bankaiichigo
# ---------------------------------------------------------------------------------

#        ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▀
#        █▀█ █░▀░█ █▄█ █▀▄ ██▄
#
#                 © Copyright 2022
#
#          https://t.me/the_farkhodov
# _           _            _ _
# | |         | |          (_) |
# | |     _ | |_ _  _ _| |
# | |    / _ \| / _ \/ | | |/ /
# | |_| (_) | || (_) \ \ |   <
# \_/\_/ \\_/|_/_|_|\_\
#
#              © Copyright 2022
#
#         developed by @lotosiiik, @byateblan
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# scope: hikka_only
# scope: hikka_min 1.3.3
# meta developer: @amoremods @hikkaftgmods
# meta banner: https://ibb.co/3NjJHvv
# meta pic: https://ibb.co/zX25RNd

from .. import loader


@loader.tds
class AnimeVoicesMod(loader.Module):
    """🎤 Popular Anime Voices"""

    strings = {"name": "AnimeVoices"}

    async def smexkcmd(self, message):
        """Смех Канеки"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/27",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def smexycmd(self, message):
        """Смех Ягами"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/28",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def znaycmd(self, message):
        """Знай свое место ничтожество"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/29",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def madaracmd(self, message):
        """Учиха Мадара"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/30",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def sharingancmd(self, message):
        """Итачи Шаринган"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/30",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def imsasukecmd(self, message):
        """Учиха Саске"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/32",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def paincmd(self, message):
        """Познайте боль"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/6",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def rascmd(self, message):
        """Расширение территории"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/8",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def tenseicmd(self, message):
        """Shinra tensei"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/9",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def dazaicmd(self, message):
        """Дазаи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/10",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def gaycmd(self, message):
        """I'm gay"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bankaicmd(self, message):
        """Bankai"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def satecmd(self, message):
        """Sate sate sate"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/13",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def yoaimocmd(self, message):
        """Yoaimo"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/14",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def madaracmd(self, message):
        """Он один из основателей конохи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/15",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def valhallacmd(self, message):
        """У нас будет крутейшая байкерская банда в Канто."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/16",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def itachicmd(self, message):
        """В возрасте 7 лет он уже мыслил как Хокаге."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/17",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ghoulcmd(self, message):
        """Я...Гуль."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/18",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bestcmd(self, message):
        """В общем раз уж я сдесь стану лучшим.(Повар боец Сомо)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/19",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def requiemcmd(self, message):
        """Это реквием."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/20",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def kingcmd(self, message):
        """Король вернулся."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/21",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def equalitycmd(self, message):
        """цитата Аянокоджи про равенство."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/22",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def forestcmd(self, message):
        """Нельзя понять всю красоту леса оценивая лишь одно дерево."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/23",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bankaiichigocmd(self, message):
        """Банкай Ичиго."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/AniVoicec/24",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
