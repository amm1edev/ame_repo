# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: oksimiron
# Author: Ijidishurka
# Commands:
# .rap
# ---------------------------------------------------------------------------------

# meta developer: @modwini
from asyncio import sleep

from .. import loader


@loader.tds
class rap(loader.Module):
    strings = {"name": "Реп оксимирона"}

    @loader.owner
    async def rapcmd(self, message):
        for _ in range(1):
            for rap in [
                "Говно",
                "залупа",
                "пенис",
                "хер",
                "давалка",
                "хуй",
                "блядина",
                "Головка",
                "шлюха",
                "жопа",
                "член",
                "еблан",
                "петух…",
                "Мудила",
                "Рукоблуд",
                "ссанина",
                "очко",
                "блядун",
                "вагина",
                "Сука",
                "ебланище",
                "влагалище",
                "пердун",
                "дрочила",
                "Пидор",
                "пизда",
                "туз",
                "малафья",
                "Гомик",
                "мудила",
                "пилотка",
                "мандаАнус",
                "вагина",
                "путана",
                "педрила",
                "Шалава",
                "хуило",
                "мошонка",
                "елда…",
                "Раунд!",
            ]:
                await message.edit(rap)
                await sleep(0.3)
