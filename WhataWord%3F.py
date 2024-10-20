# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: WhataWord?
# Author: dorotorothequickend
# Commands:
# .waw
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
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroWhataWord.png
# meta developer: @DorotoroMods

from .. import loader, utils


@loader.tds
class whataword(loader.Module):
    """Ищет определение слова."""

    strings = {"name": "What a Word?"}

    @loader.command()
    async def wawcmd(self, message):
        "<слово> - ищет определение вашего слова."
        args = utils.get_args_raw(message)
        ktoetochitaetlox = await utils.answer(
            message, "<b><i>Открываю свой словарик...</i></b>"
        )
        if not args:
            return
        async with self._client.conversation("@definerBot") as conv:
            perdunmsg = await conv.send_message(args)
            jdun = await conv.get_response()
            await perdunmsg.delete()
            await jdun.delete()
        text = f"<b>Я нашел кое-что в словаре:</b>\n{jdun.text}"
        await utils.answer(ktoetochitaetlox, text)
