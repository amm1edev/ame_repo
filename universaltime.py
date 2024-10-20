# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: universaltime
# Author: AmoreForever
# Commands:
# .atime | .atimei
# ---------------------------------------------------------------------------------

# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠛⠛
# ⣶⣦⣤⣤⣤⣤⣤⣤⣬⣭⣭⣍⣉⡙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣋⣩⣭⣥⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶
# ⣆⠀⠀⠀⢡⠁⠀⡀⠀⢸⠟⠻⣯⠙⠛⠷⣶⣬⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣥⣶⡟⠻⣙⡉⠀⢰⡆⠀⠀⣡⠀⣧⠀⠀⠀⢨
# ⠻⣦⠀⠀⠈⣇⣀⣧⣴⣿⣶⣶⣿⣷⠀⢀⡇⠉⠻⢶⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣡⡶⠟⠉⠀⢣⠀⣿⠷⠀⠀⠀⠀⣿⡷⢀⠇⠀⠀⢠⣿
# ⣦⡈⢧⡀⠀⠘⢮⡙⠛⠉⠀⠄⠙⢿⣀⠞⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠈⠳⣄⠉⠓⠒⠚⠋⢀⡠⠋⠀⢀⣴⣏⣿
# ⣿⣿⣿⣛⣦⣀⠀⠙⠓⠦⠤⣤⠔⠛⠁⠀⠀⠀⠀⠀⢀⣀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣀⣀⣀⣀⢙⢓⣒⡒⠚⠋⢠⣤⢶⣟⣽⣿⣿
# ⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⣴⣿⣷⣶⣶⣶⣾⡖⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣿⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣷⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

#                           🔒 Licensed under the GNU GPLv3
#                    🌐 https://www.gnu.org/licenses/agpl-3.0.html
#                            https://t.me/amorescam

# meta developer: @amoremods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Universaltime.jpg
# @Den4ikSuperOstryyPer4ik: I Love AmoreMods :)


import datetime
import logging

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


def check_time():
    offsets = [3, 5, 4, 2, 1, -7, 6, 9, 5.30, 9, 8, -8, -4]
    hrs = []
    for x in offsets:
        offset = datetime.timedelta(hours=x)
        not_tz = datetime.timezone(offset)
        time = datetime.datetime.now(not_tz)
        format_ = time.strftime("%d.%m.%y | %H:%M")
        hrs.append(format_)
    return (
        "<emoji document_id=4920662486778119009>🌐</emoji> <b>Universal"
        " time</b>\n\n<emoji document_id=6323139226418284334>🇷🇺</emoji> Russia ➪"
        f" {hrs[0]}\n<emoji document_id=6323430017179059570>🇺🇿</emoji> Uzbekistan ➪"
        f" {hrs[1]}\n<emoji document_id=6323289850921354919>🇺🇦</emoji> Ukraine ➪"
        f" {hrs[3]}\n<emoji document_id=6323575251498174463>🇦🇿</emoji> Azerbaijan ➪"
        f" {hrs[2]}\n<emoji document_id=6320817337033295141>🇩🇪</emoji> German ➪"
        f" {hrs[3]}\n<emoji document_id=6323589145717376403>🇬🇧</emoji> UK ➪"
        f" {hrs[4]}\n<emoji document_id=6323602387101550101>🇵🇱</emoji> Poland ➪"
        f" {hrs[3]}\n<emoji document_id=6323374027985389586>🇺🇸</emoji> USA ➪"
        f" {hrs[5]}\n<emoji document_id=6323615997852910673>🇰🇬</emoji> Kyrgyzstan ➪"
        f" {hrs[6]}\n<emoji document_id=6323135275048371614>🇰🇿</emoji> Kazakhstan ➪"
        f" {hrs[6]}\n<emoji document_id=6323555846835930376>🇮🇶</emoji> Iraq ➪"
        f" {hrs[0]}\n<emoji document_id=6323356796576597627>🇯🇵</emoji> Japan ➪"
        f" {hrs[7]}\n<emoji document_id=6323152716910561397>🇰🇷</emoji> South KR ➪"
        f" {hrs[7]}\n<emoji document_id=6323181871148566277>🇮🇳</emoji> India ➪"
        f" {hrs[8]}\n<emoji document_id=6323570711717742330>🇫🇷</emoji> France ➪"
        f" {hrs[3]}\n<emoji document_id=6323453751168337485>🇨🇳</emoji> China ➪"
        f" {hrs[9]}\n<emoji document_id=6321003171678259486>🇹🇷</emoji> Turkey ➪"
        f" {hrs[0]}\n<emoji document_id=6323602322677040561>🇨🇱</emoji> Mongolia ➪"
        f" {hrs[10]}\n<emoji document_id=6323325327351219831>🇨🇦</emoji> Canada ➪"
        f" {hrs[11]}\n<emoji document_id=6323471399188957082>🇮🇹</emoji> Italia ➪"
        f" {hrs[2]}\n<emoji document_id=6323516260122363644>🇪🇬</emoji> Egypt ➪"
        f" {hrs[3]}\n<emoji document_id=6323236391463421376>🇦🇲</emoji> Armenia ➪"
        f" {hrs[12]}\n\n<emoji document_id=5188216117272780281>🍙</emoji> #whyamore"
    )


@loader.tds
class UniversalTimeMod(loader.Module):
    """See the time of other countries"""

    strings = {"name": "UnivTime"}

    @loader.command(ru_docs="Смотреть мировое время")
    async def atimecmd(self, message):
        """See time"""
        kk = check_time()
        await utils.answer(message, kk)

    @loader.command(ru_docs="Смотреть мировое время в инлайн режиме")
    async def atimeicmd(self, message):
        """See time on inline mode"""
        kk = check_time()
        await self.inline.form(
            text=kk,
            message=message,
            gif="https://te.legra.ph/file/2ab9b131ceceb9b020583.mp4",
            reply_markup=[
                [
                    {
                        "text": "🍃 Refresh",
                        "callback": self.refresh,
                    }
                ],
                [
                    {
                        "text": "🔻 Close",
                        "action": "close",
                    }
                ],
            ],
        )

    async def refresh(self, call: InlineCall):  # thanks @Den4ikSuperOstryyPer4ik
        kk = check_time()
        await call.edit(
            text=kk,
            reply_markup=[
                [
                    {
                        "text": "🍃 Refresh",
                        "callback": self.refresh,
                    }
                ],
                [
                    {
                        "text": "🔻 Close",
                        "action": "close",
                    }
                ],
            ],
        )
        await call.answer("Refreshed ✨")
