# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Reposaver
# Author: DarkModules
# Commands:
# .repo
# ---------------------------------------------------------------------------------

#
# █▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
# █▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# scope: hikka_only
# version: 1.0

from .. import loader, utils


class RepoSaverMod(loader.Module):
    """GitHub Repository saver via @githubrepo_download_bot"""

    strings = {
        "name": "Reposaver",
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Just wait!</b>",
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Provide the correct"
            " Repository link!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>Submitted"
            " successfully!</b>"
        ),
    }

    strings_ru = {
        "dwait": (
            "<emoji document_id=5283042475408106112>🙏</emoji> <b>Просто подождите!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Укажите правильную"
            " ссылку на Repository!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>Отправлено"
            " успешно!</b>"
        ),
    }

    strings_uz = {
        "dwait": (
            "<emoji document_id=5283042475408106112>🙏</emoji> <b>Shunchaki kuting!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>To'g'ri Repository"
            " havola kiriting!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>Muvaffaqiyatli"
            " yuborildi!</b>"
        ),
    }

    strings_de = {
        "dwait": (
            "<emoji document_id=5283042475408106112>🙏</emoji> <b>Warte einfach!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Geben Sie den"
            " richtigen Repository link an!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>Erfolgreich"
            " gesendet</b></b>"
        ),
    }

    strings_jp = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>ちょっと待って!</b>",
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>有効な Repository"
            " リンクを提供してください。!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>正常に送信されました!</b></b>"
        ),
    }

    strings_tr = {
        "dwait": (
            "<emoji document_id=5283042475408106112>🙏</emoji> <b>Sadece bekle!</b>"
        ),
        "denterlink": (
            "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Doğru Repository"
            " adresi gönderin!</b>"
        ),
        "dsaved": (
            "<emoji document_id=5240446815127477236>😎</emoji> <b>Başariyla"
            " gönderildi!</b></b>"
        ),
    }

    async def repocmd(self, message):
        """enter Repository link from GitHub"""
        link = utils.get_args_raw(message)
        if not link:
            await utils.answer(message, self.strings("denterlink", message))
            return

        message = await utils.answer(message, self.strings("dwait"))
        async with self._client.conversation("@githubrepo_download_bot") as bot:
            act = []
            act += [await bot.send_message(link)]
            ignore = await bot.get_response()
            secignore = await bot.get_response()
            work = await bot.get_response()

        await message.delete()
        await self._client.send_file(
            message.peer_id,
            work.media,
            caption=self.strings("dsaved"),
            reply_to=message.reply_to_msg_id,
        )
        await self.client.delete_dialog("@githubrepo_download_bot")
