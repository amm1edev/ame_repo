# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: YandexMusic
# Author: Den4ikSuperOstryyPer4ik
# Commands:
# .ym
# ---------------------------------------------------------------------------------

__version__ = (1, 1, 1)
#
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
#
#                                             © Copyright 2023
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules

from .. import loader, utils


class YaMusicMod(loader.Module):
    """Поиск музыки через музыкального бота от Яндекса"""

    strings = {
        "name": "YandexMusic",
        "na": "😅 <b>А что искать то?</b>",
        "searching": "<b>Поиск...</b>",
    }

    async def ymcmd(self, message):
        """- найти трек по названию"""
        args = utils.get_args_raw(message)
        bot = "@music_yandex_bot"
        if not args:
            await utils.answer(message, self.strings("na"))
        try:
            await utils.answer(message, self.strings("searching"))
            music = await message.client.inline_query(bot, args)
            await message.delete()
            try:
                await utils.answer_file(
                    message,
                    music[1].result.document,
                    caption="<b>🎧 Возможно, это тот трек, который вы искали</b>",
                )
            except:
                await utils.answer_file(
                    message,
                    music[3].result.document,
                    caption="<b>🎧 Возможно, это тот трек, который вы искали</b>",
                )
        except:
            await utils.answer(
                message,
                f"<b>😔 Нам не удалось найти трек с названием <code>{args}</code><b>",
            )
