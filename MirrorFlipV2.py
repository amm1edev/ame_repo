# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MirrorFlipV2
# Description: No description
# Author: KeyZenD
# Commands:
# .ll | .rr | .uu | .dd
# ---------------------------------------------------------------------------------


from asyncio import sleep
from io import BytesIO

from PIL import Image, ImageOps

from .. import loader, utils


class MirrorFlipMod(loader.Module):
    strings = {"name": "MirrorFlip", 0: "<b>Reply to image.</b>"}

    async def llcmd(self, m):
        return await make(m, 1)

    async def rrcmd(self, m):
        return await make(m, 2)

    async def uucmd(self, m):
        return await make(m, 3)

    async def ddcmd(self, m):
        return await make(m, 4)


async def make(m, o):
    r = await m.get_reply_message()
    s = None
    try:
        s = await r.download_media(bytes, thumb=-1 if not r.sticker else None)
        img = Image.open(BytesIO(s))
    except:
        pass
    if not s:
        return await utils.answer(m, MirrorFlipMod.strings[0])
    await m.delete()
    w, h = img.size
    if o in [1, 2]:
        if o == 2:
            img = ImageOps.mirror(img)
        part = img.crop([0, 0, w // 2, h])
        img = ImageOps.mirror(img)
    else:
        if o == 4:
            img = ImageOps.flip(img)
        part = img.crop([0, 0, w, h // 2])
        img = ImageOps.flip(img)
    img.paste(part, (0, 0))
    out = BytesIO()
    out.name = "x.webp" if r.sticker else "x.png"
    img.save(out)
    out.seek(0)
    return await r.reply(file=out)
