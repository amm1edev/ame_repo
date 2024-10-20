# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: trigger
# Author: AmoreForever
# Commands:
# .trig
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

__version__ = (1, 2, 0)

# meta developer: @amoremods
# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Trigger.jpg

import requests
from telethon.tl.types import DocumentAttributeFilename

from .. import loader


@loader.tds
class TriggerMod(loader.Module):
    """Make trigger"""

    strings = {
        "name": "Trigger",
        "not_reply": "⚠️ Reply to only photo",
    }

    @loader.command(ru_doc="<ответ на картинку>")
    async def trigcmd(self, message):
        """<reply to photo>"""
        if message.is_reply:
            reply_message = await message.get_reply_message()
            data = await check_media(reply_message)
            if isinstance(data, bool):
                await message.edit(self.strings("not_reply"))
                return
        else:
            await message.edit(self.strings("not_reply"))
            return

        file = await message.client.download_media(data, bytes)
        path = requests.post(
            "https://te.legra.ph/upload", files={"file": ("file", file, None)}
        ).json()
        try:
            amore = (
                "https://some-random-api.ml/canvas/triggered?avatar=https://te.legra.ph"
                + path[0]["src"]
            )
        except KeyError:
            amore = path["error"]
        m = await self.inline.form(
            text="🎨 ­Wait...­",
            message=message,
            gif=f"{amore}",
            reply_markup={},
            ttl=3600,
        )


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
            if (
                DocumentAttributeFilename(file_name="st.tgs")
                in reply_message.media.document.attributes
            ):
                return False
            if reply_message.video or reply_message.gif:
                return False
            if reply_message.file or reply_message.audio:
                return False
            data = reply_message.media.document
        else:
            return False
    else:
        return False
    if not data or data is None:
        return False
    else:
        return data
