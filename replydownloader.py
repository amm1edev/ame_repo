# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: replydownloader
# Description: Скачать файлом реплай.
# Author: Fl1yd
# Commands:
# .dlr | .ulf
# ---------------------------------------------------------------------------------


import os
from asyncio import sleep

from .. import loader, utils


def register(cb):
    cb(ReplyDownloaderMod())


class ReplyDownloaderMod(loader.Module):
    """Скачать файлом реплай."""

    strings = {"name": "Reply Downloader"}

    async def dlrcmd(self, message):
        """Команда .dlr <реплай на файл> <название (по желанию)> скачивает файл, либо сохраняет текст в файл на который был сделан реплай."""
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if reply:
            await message.edit("Скачиваем...")
            if reply.text:
                text = reply.text
                fname = f"{name or message.id+reply.id}.txt"
                file = open(fname, "w")
                file.write(text)
                file.close()
                await message.edit(
                    f"Файл сохранён как: <code>{fname}</code>.\n\nВы можете отправить"
                    f" его в этот чат с помощью команды <code>.ulf {fname}</code>."
                )
            else:
                ext = reply.file.ext
                fname = f"{name or message.id+reply.id}{ext}"
                await message.client.download_media(reply, fname)
                await message.edit(
                    f"Этот файл сохранён как: <code>{fname}</code>.\n\nВы можете"
                    " отправить его в этот чат с помощью команды <code>.ulf"
                    f" {fname}</code>."
                )
        else:
            return await message.edit("Нет реплая.")

    async def ulfcmd(self, message):
        """Команда .ulf <d>* <название файла> отправляет файл в чат.\n* - удалить файл после отправки."""
        name = utils.get_args_raw(message)
        d = False
        if "d " in name:
            d = True
        if name:
            try:
                name = name.replace("d ", "")
                await message.edit(f"Отправляем <code>{name}</code>...")
                if d == True:
                    await message.client.send_file(message.to_id, f"{name}")
                    await message.edit(
                        f"Отправляем <code>{name}</code>... Успешно!\nУдаляем"
                        f" <code>{name}</code>..."
                    )
                    os.remove(name)
                    await message.edit(
                        f"Отправляем <code>{name}</code>... Успешно!\nУдаляем"
                        f" <code>{name}</code>... Успешно!"
                    )
                    await sleep(0.5)
                else:
                    await message.client.send_file(message.to_id, name)
            except:
                return await message.edit("Такой файл не существует.")
            await message.delete()
        else:
            return await message.edit("Нет аргументов.")
