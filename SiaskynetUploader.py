# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: SiaskynetUploader
# Description: Siasky.net uploader by @blazeftg
# Author: blazedzn
# Commands:
# .upload
# ---------------------------------------------------------------------------------


import os

import siaskynet as skynet

from .. import loader, utils


@loader.tds
class UploaderMod(loader.Module):
    """siasky.net uploader by @blazeftg"""

    strings = {"name": "FileUploader"}

    async def uploadcmd(self, message):
        """.upload <реплай на файл> - загружает файл на сервер
        или
        .upload <реплай на текст> - загружает текст из реплая на сервер
        """
        await message.edit(f"<b>Загружаю...</b>")
        client = skynet.SkynetClient()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("Нужен реплай")
            return
        try:
            file = await reply.download_media()
            link = client.upload_file(file)
            filtered = link.split("sia://")
            link = "https://siasky.net/" + str(filtered[1])
            await message.edit("Линк: \n" + link)
        except:
            f = open("text.txt", "w")
            f.write(reply.raw_text)
            f.close()
            link = client.upload_file("text.txt")
            filtered = link.split("sia://")
            link = "https://siasky.net/" + str(filtered[1])
            await message.edit("Линк: \n" + link)
            os.remove("text.txt")
