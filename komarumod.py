# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: komarumod
# Author: Den4ikSuperOstryyPer4ik
# Commands:
# .komaru
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 2)
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
# meta banner: https://0x0.st/Hs4u.png
# meta developer: @AstroModules

from random import choice

from telethon.tl.types import (
    InputMessagesFilterGif,
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    Message,
)

from .. import loader, utils


class KomaruMod(loader.Module):
    """Random picture/video/gif from the @komarueveryday"""

    strings = {
        "name": "Komaru",
        "choosing": "<emoji document_id=5328311576736833844>🔴</emoji> Choosing {}...",
        "gif": "gif",
        "video": "video",
        "photo": "photo",
    }

    strings_ru = {
        "choosing": "<emoji document_id=5328311576736833844>🔴</emoji> Подбираем {}...",
        "gif": "ваш гиф",
        "video": "ваше видео",
        "photo": "вашу картинку(пикчу)",
    }

    SEARCH_TYPES = {
        InputMessagesFilterGif: "gif",
        InputMessagesFilterPhotos: "photo",
        InputMessagesFilterVideo: "video",
    }

    @loader.command(ru_doc="- подобрать рандом картинку(пикчу)/видео/гиф")
    async def komaru(self, message: Message):
        """- choose a random picture/gif/video"""
        search_type = choice(
            [
                InputMessagesFilterGif,
                InputMessagesFilterPhotos,
                InputMessagesFilterVideo,
            ]
        )
        search_type_str = self.strings(self.SEARCH_TYPES[search_type])

        msg = await utils.answer(
            message, self.strings("choosing").format(search_type_str)
        )

        chosed_msg = choice(
            [
                message_in_channel
                async for message_in_channel in self.client.iter_messages(
                    "komarueveryday", limit=200, filter=search_type
                )
            ]
        )

        reply = await message.get_reply_message()
        if reply:
            reply = reply.id
        else:
            reply = None

        return await utils.answer_file(
            msg,
            chosed_msg,
            chosed_msg.text or "<b>Подобрал " + search_type_str + ".</b>",
            reply_to=reply,
        )
