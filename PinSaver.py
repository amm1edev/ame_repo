# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: PinSaver
# Author: DziruModules
# Commands:
# .pin
# ---------------------------------------------------------------------------------

#
# █▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
# █▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://raw.githubusercontent.com/DziruModules/assets/master/DziruModules.jpg
# meta banner: https://raw.githubusercontent.com/DziruModules/assets/master/PinSaver.png
# scope: hikka_only
# version: 1.0

from .. import loader, utils


class PinSaverMod(loader.Module):
    """Pinterest saver via @TopSaverBot"""

    strings = {
        "name": "Pin saver",
        "dwait": "<emoji document_id=5334922351744132060>😉</emoji> <b>Just wait!</b>",
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>Provide the correct"
            " Pin-Link!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>Submitted"
            " successfully!</b>"
        ),
    }

    strings_ru = {
        "dwait": (
            "<emoji document_id=5334922351744132060>😉</emoji> <b>Просто подождите!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>Укажите правильную"
            " ссылку на Pin!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>Отправлено"
            " успешно!</b>"
        ),
    }

    strings_uz = {
        "dwait": (
            "<emoji document_id=5334922351744132060>😉</emoji> <b>Shunchaki kuting!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>To'g'ri Pin havola"
            " kiriting!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>Muvaffaqiyatli"
            " yuborildi!</b>"
        ),
    }

    strings_de = {
        "dwait": (
            "<emoji document_id=5334922351744132060>😉</emoji> <b>Warte einfach!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>Geben Sie den"
            " richtigen Pin-Link an!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>Erfolgreich"
            " gesendet</b></b>"
        ),
    }

    strings_jp = {
        "dwait": "<emoji document_id=5334922351744132060>😉</emoji> <b>ちょっと待って!</b>",
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>有効な PIN"
            " リンクを提供してください。!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>正常に送信されました!</b></b>"
        ),
    }

    strings_tr = {
        "dwait": (
            "<emoji document_id=5334922351744132060>😉</emoji> <b>Sadece bekle!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5335046240075784593>😠</emoji> <b>Doğru Pin-adresi"
            " gönderin!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5346032779303854340>😎</emoji> <b>Başariyla"
            " gönderildi!</b></b>"
        ),
    }

    async def pincmd(self, message):
        """LINK from Pinterest"""
        link = utils.get_args_raw(message)
        if not link:
            await utils.answer(message, self.strings("denterlink", message))
            return
        message = await utils.answer(message, self.strings("dwait"))
        async with self._client.conversation("@TopSaverBot") as bot:
            act = []
            act += [await bot.send_message(link)]
            ignore = await bot.get_response()
            work = await bot.get_response()
        await message.delete()
        await self._client.send_file(
            message.peer_id,
            work.media,
            caption=self.strings("dsaved"),
            reply_to=message.reply_to_msg_id,
        )
        await self.client.delete_dialog("@TopSaverBot")
