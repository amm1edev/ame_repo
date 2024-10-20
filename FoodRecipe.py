# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: FoodRecipe
# Author: dorotorothequickend
# Commands:
# .foodrecipe
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
# 		      Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/DorotoroFoodRecipe.png
# meta developer: @DorotoroMods

from telethon.tl.types import Message

from .. import loader, utils
from ..utils import answer


@loader.tds
class FoodRecipe(loader.Module):
    """Ищет рецепт блюда по его названию."""

    strings = {"name": "FoodRecipe"}

    @loader.command()  # используем декоратор команды
    async def foodrecipecmd(self, message: Message):
        "<название блюда> - найти рецепт блюда."
        args = utils.get_args_raw(message)
        msg = await answer(message, "Пожалуйста подождите. Рецепт в поиске...!")
        if not args:
            await answer(
                message,
                (
                    "Поедим пустоту вместе! Введи ингридиенты или название блюда,"
                    " пожалуйста."
                ),
            )
        async with self._client.conversation("@cookinghelpbot") as conv:
            msgg = await conv.send_message(args)
            r = await conv.get_response()

            if r.message == "Рецепт не загрузился, либо его нет":
                await answer(msg, "🔧 Рецепт не найден.")
                return
            elif r.message == "Одного из ингридиента нету":
                await answer(msg, "🔧 Один из ингредиентов отсутствует. ")
                return
            else:
                await r.click(data="cook")
                k = await conv.get_response()
            await msgg.delete()
            await r.delete()
            await k.delete()
        ingridienti = r.text[15:]
        retept = k.text
        text = f"<b>Рецепт найден!\n\n{ingridienti}\n\nРецепт:\n{retept}</b>"
        await answer(msg, text)
