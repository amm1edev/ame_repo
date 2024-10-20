# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: RandomHuman
# Author: dorotorothequickend
# Commands:
# .generatehuman | .generatepass | .generateschl | .generatedocs | .generateauto
# .generatebank 
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# ---------------------------------------------------------------------------------
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroGenerateHuman.png
# meta developer: @DorotoroMods

from telethon.tl.types import Message

from .. import loader, utils
from ..utils import answer


@loader.tds
class RandomHuman(loader.Module):
    """Отправляет рандомное имя, фамилию, дату рождения, email, пароль и телефон."""

    strings = {"name": "GenerateHuman"}

    @loader.command()
    async def generatehumancmd(self, message: Message):
        "- сгенерировать человека."
        msg = await answer(message, "<b><i>Подбираю человека...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            popo4ka = await conv.send_message("👤 Пользователь")
            r = await conv.get_response()
            await popo4ka.delete()
            await r.delete()
        dsopthx = r.text.split("\n")
        dsopthx.remove("👤 Пользователь")
        dsopthx.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        chel = "\n".join(dsopthx)
        text = (
            "<b>Человек сгенерирован. Кое-что про"
            f" него:\n\n{chel}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)

    @loader.command()
    async def generatepasscmd(self, message: Message):
        "- сгенерировать паспорт."
        msg = await answer(message, "<b><i>Ищу паспорта...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            jdun = await conv.send_message("🛂 Паспорт")
            r = await conv.get_response()
            await jdun.delete()
            await r.delete()
        udalit = r.text.split("\n")
        udalit.remove("🛂 Паспорт")
        udalit.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        papa = "\n".join(udalit)
        text = (
            "<b>Паспорт сгенерирован. Вот что я"
            f" нарыл:\n\n{papa}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)

    @loader.command()
    async def generateschlcmd(self, message: Message):
        "- сгенерировать инф-цию об образовании."
        msg = await answer(message, "<b><i>Пробиваю документы...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            jdun = await conv.send_message("🏫 Образование")
            r = await conv.get_response()
            await jdun.delete()
            await r.delete()
        udalit = r.text.split("\n")
        udalit.remove("🏫 Образование")
        udalit.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        papa = "\n".join(udalit)
        text = (
            "<b>Образование сгенерировано. Вот что я"
            f" нарыл:\n\n{papa}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)

    @loader.command()
    async def generatedocscmd(self, message: Message):
        "- сгенерировать документы."
        msg = await answer(message, "<b><i>Пробиваю документы...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            jdun = await conv.send_message("📄 Документы")
            r = await conv.get_response()
            await jdun.delete()
            await r.delete()
        udalit = r.text.split("\n")
        udalit.remove("📄 Документы")
        udalit.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        papa = "\n".join(udalit)
        text = (
            "<b>Документы сгенерированы. Вот что я"
            f" нарыл:\n\n{papa}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)

    @loader.command()
    async def generateauto(self, message: Message):
        "- сгенерировать инф-цию об авто."
        msg = await answer(message, "<b><i>Пробиваю номера авто...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            jdun = await conv.send_message("🚙 Автомобиль")
            r = await conv.get_response()
            await jdun.delete()
            await r.delete()
        udalit = r.text.split("\n")
        udalit.remove("🚙 Автомобиль")
        udalit.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        papa = "\n".join(udalit)
        text = (
            "<b>Автомобиль сгенерирован. Вот что я"
            f" нарыл:\n\n{papa}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)

    @loader.command()
    async def generatebank(self, message: Message):
        "- сгенерировать платежную инф-цию."
        msg = await answer(message, "<b><i>Пробиваю банковские карты...</i></b>")
        async with self._client.conversation("@randomdatatools_bot") as conv:
            jdun = await conv.send_message("🏦 Банк")
            r = await conv.get_response()
            await jdun.delete()
            await r.delete()
        udalit = r.text.split("\n")
        udalit.remove("🏦 Платежная информация")
        udalit.remove("<i>(Нажмите на значение, чтобы скопировать его)</i>")
        papa = "\n".join(udalit)
        text = (
            "<b>Платежная инф-ция сгенерирована. Вот что я"
            f" нарыл:\n\n{papa}\n\n<tg-spoiler><i>RandomHuman</i></tg-spoiler></b>"
        )
        await answer(msg, text)
