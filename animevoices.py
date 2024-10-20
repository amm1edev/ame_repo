# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: animevoices
# Author: AmoreForever
# Commands:
# .smexk    | .smexy      | .znay       | .madara   | .sharingan
# .itachi   | .imsasuke   | .pain       | .ras      | .tensei   
# .dazai    | .gay        | .bankai     | .sate     | .yoaimo   
# .ghoul    | .welaw      | .dattebayo  | .hardlife | .hanma    
# .surprise | .equal      | .beautytree | .bankaii  | .yamete   
# .mafia    | .sharingann | .smexe      | .naruto   | .smexr    
# .ohayo    | .iamhungry  | .amaterasu  | .owo      | .ghoulru  
# ---------------------------------------------------------------------------------

# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru

# meta developer: @hikamorumods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/AnimeVoices.jpg

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
            "https://t.me/animevoicesbyamore/9",
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
            "https://t.me/animevoicesbyamore/7",
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
            "https://t.me/animevoicesbyamore/35",
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
            "https://t.me/animevoicesbyamore/24",
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
            "https://t.me/VoiceAmore/29",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def itachicmd(self, message):
        """Учиха Итачи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/26",
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
            "https://t.me/VoiceAmore/30",
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
            "https://t.me/animevoicesbyamore/15",
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
            "https://t.me/animevoicesbyamore/17",
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
            "https://t.me/animevoicesbyamore/18",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def dazaicmd(self, message):
        """Dazai"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/3",
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
            "https://t.me/animevoicesbyamore/20",
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
            "https://t.me/animevoicesbyamore/21",
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
            "https://t.me/animevoicesbyamore/5",
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
            "https://t.me/animevoicesbyamore/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ghoulcmd(self, message):
        """Я гуль"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def welawcmd(self, message):
        """Мы закон"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/13",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def dattebayocmd(self, message):
        """Даттебайо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/14",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def hardlifecmd(self, message):
        """Жизнь такова"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/16",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def hanmacmd(self, message):
        """Я Ханма Шужи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/25",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def surprisecmd(self, message):
        """Surprise MxtherFxcker"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/30",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def equalcmd(self, message):
        """Мы созданы равными"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/31",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def beautytreecmd(self, message):
        """Красота леса"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/32",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def bankaiicmd(self, message):
        """Bankai remix"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/33",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def yametecmd(self, message):
        """Фулл ямете кудасай"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/47",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def mafiacmd(self, message):
        """Просыпается мафия"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/48",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def sharinganncmd(self, message):
        """Sharingan remix"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/49",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def smexecmd(self, message):
        """Смех Эрен"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/50",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def narutocmd(self, message):
        """Naruto heroes"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/51",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def smexrcmd(self, message):
        """Смех рюк"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/52",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ohayocmd(self, message):
        """Охаё"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/53",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def iamhungrycmd(self, message):
        """Есть хочу"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/54",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def amaterasucmd(self, message):
        """Аматерасу remix"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/55",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def owocmd(self, message):
        """Full OwO"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/56",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ghoulrucmd(self, message):
        """Русский Tokyo Ghoul"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/animevoicesbyamore/57",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    # voices by @dziru
