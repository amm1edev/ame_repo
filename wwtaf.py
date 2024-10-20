# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: wwtaf
# Description: Модуль для работы с текстом или файлами.
# Author: Fl1yd
# Commands:
# .file   | .tabfix    | .text2txt | .text2py | .bold
# .italic | .underline | .mono     | .cross   | .enter
# ---------------------------------------------------------------------------------


import io

from requests import get
from telethon import types

from .. import loader, utils


def register(cb):
    cb(WWTaFMod())


class WWTaFMod(loader.Module):
    """Модуль для работы с текстом или файлами."""

    strings = {"name": "WWTaF"}

    async def filecmd(self, event):
        """Получить файл по ссылке.\nИспользование: .file <ссылка или реплай на ссылку>."""
        try:
            text = utils.get_args_raw(event)
            reply = await event.get_reply_message()

            if text:
                urll = text.split()
                for url in urll:
                    if "://" in url:
                        break
                text = get(url).text
                file = io.BytesIO(bytes(text, "utf-8"))
                file.name = url.split("/")[-1]
                file.seek(0)
                await event.client.send_file(event.to_id, file)
                await event.delete()

            if reply:
                urll = reply.raw_text.split()
                for url in urll:
                    if "://" in url:
                        break
                text = get(url).text
                file = io.BytesIO(bytes(text, "utf-8"))
                file.name = url.split("/")[-1]
                file.seek(0)
                await event.client.send_file(event.to_id, file, reply_to=reply)
                await event.delete()

            if not text and not reply:
                await event.edit("<b>Нет текста или реплая.</b>")
        except:
            await event.edit(
                '<b>Возможно вы забыли добавить "http://" перед ссылкой.</b>'
            )
            return

    async def tabfixcmd(self, event):
        """Используй .tabfix <реплай или файл с текстом .tabfix>."""
        await event.delete()
        try:
            reply = await event.get_reply_message()
            text = await event.client.download_file(reply, bytes)
            text = str(text, "utf-8")
            tabs = text.count("\t")
            text = text.replace("\t", " " * 4)
            file = io.BytesIO(bytes(text, "utf-8"))
            filename = reply.media.document.attributes[-1].file_name
            file.name = "TabsFixed_" + filename
            file.seek(0)
            await event.client.send_file(
                event.to_id, file, caption=f"<b>Заменено: {tabs} табов.</b>"
            )
        except:
            await event.edit("<b>Нет реплая на файл.</b>")

    async def text2txtcmd(self, event):
        """Переносит текст в файл .txt.\nИспользуй: .text2txt <текст или реплай>."""
        await event.delete()
        text = utils.get_args_raw(event)
        reply = await event.get_reply_message()
        if text:
            await event.client.send_file(
                event.to_id,
                text.encode(),
                attributes=[types.DocumentAttributeFilename(file_name="text2txt.txt")],
            )
        if reply:
            await event.client.send_file(
                event.to_id,
                reply.raw_text.encode(),
                attributes=[types.DocumentAttributeFilename(file_name="text2txt.txt")],
            )
        if not text and not reply:
            await event.edit("<b>Нет текста или реплая.</b>")

    async def text2pycmd(self, event):
        """Переносит текст в файл .py.\nИспользуй: .text2py <текст или реплай>."""
        await event.delete()
        text = utils.get_args_raw(event)
        reply = await event.get_reply_message()
        if text:
            await event.client.send_file(
                event.to_id,
                text.encode(),
                attributes=[types.DocumentAttributeFilename(file_name="text2py.py")],
            )
        if reply:
            await event.client.send_file(
                event.to_id,
                reply.raw_text.encode(),
                attributes=[types.DocumentAttributeFilename(file_name="text2py.py")],
            )
        if not text and not reply:
            await event.edit("<b>Нет текста или реплая.</b>")

    async def boldcmd(self, message):
        """Сделать текст жирным.\nИспользуй: .bold <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<b>{text}</b>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<b>{reply.raw_text}</b>")
            else:
                await message.delete()
                await reply.edit(f"<b>{reply.raw_text}</b>")

    async def italiccmd(self, message):
        """Сделать текст курсивным.\nИспользуй: .italic <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<i>{text}</i>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<i>{reply.raw_text}</i>")
            else:
                await message.delete()
                await reply.edit(f"<i>{reply.raw_text}</i>")

    async def underlinecmd(self, message):
        """Сделать текст подчеркнутым.\nИспользуй: .underline <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<u>{text}</u>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<u>{reply.raw_text}</u>")
            else:
                await message.delete()
                await reply.edit(f"<u>{reply.raw_text}</u>")

    async def monocmd(self, message):
        """Сделать текст моноширинным.\nИспользуй: .mono <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<code>{text}</code>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<code>{reply.raw_text}</code>")
            else:
                await message.delete()
                await reply.edit(f"<code>{reply.raw_text}</code>")

    async def crosscmd(self, message):
        """Сделать текст зачеркнутым.\nИспользуй: .cross <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<s>{text}</s>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<s>{reply.raw_text}</s>")
            else:
                await message.delete()
                await reply.edit(f"<s>{reply.raw_text}</s>")

    async def entercmd(self, message):
        """Перенос строки после каждого слова.\nИспользуй: .enter <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.respond("\n".join(text.split(" ")))
        if reply:
            await message.edit("\n".join(reply.text.split(" ")))
        await message.delete()
