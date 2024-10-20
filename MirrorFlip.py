# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MirrorFlip
# Description: No description
# Author: KeyZenD
# Commands:
# Failed to parse
# ---------------------------------------------------------------------------------


_C = "png"
_B = "name"
_A = "image"
_R = "отражает"
_P = "часть."
import asyncio
import logging
from io import BytesIO as ist

from PIL import Image
from PIL import ImageOps as IO
from telethon.tl.types import DocumentAttributeFilename as DAF

from .. import loader as _L
from .. import utils as U

logger = logging.getLogger(__name__)


@_L.tds
class MFMod(_L.Module):
    f"{_R} фоточки"
    strings = {_B: "MirrorFlip"}

    def __init__(A):
        A.name = A.strings[_B]

    async def llcmd(A, message):
        await KZD(message, 1)

    async def rrcmd(A, message):
        await KZD(message, 2)

    async def uucmd(A, message):
        await KZD(message, 3)

    async def ddcmd(A, message):
        await KZD(message, 4)


async def KZD(message, type):
    S = "sticker"
    A = message
    N = await A.get_reply_message()
    Q, J = await CM(N)
    if not Q or not N:
        await A.edit("<b>Реплай на стикер или фото!</b>")
        return
    O = "KZD." + J
    P = U.get_args_raw(A)
    if P:
        if P in [_A[:A] for A in range(1, len(_A) + 1)]:
            O = "KZD.png"
            J = _C
        if P in [S[:A] for A in range(1, len(S) + 1)]:
            O = "KZD.webp"
            J = "webp"
    R = ist()
    await A.edit("<b>Извиняюсь...</b>")
    await A.client.download_media(Q, R)
    E = Image.open(R)
    B, C = E.size
    if B % 2 != 0 and type in [1, 2] or C % 2 != 0 and type in [3, 4]:
        E = E.resize((B + 1, C + 1))
        C, B = E.size
    if type == 1:
        D = 0
        F = 0
        G = B // 2
        H = C
        K = G
        L = D
    if type == 2:
        D = B // 2
        F = 0
        G = B
        H = C
        K = F
        L = F
    if type == 3:
        D = 0
        F = 0
        G = B
        H = C // 2
        K = D
        L = H
    if type == 4:
        D = 0
        F = C // 2
        G = B
        H = C
        K = D
        L = D
    I = E.crop((D, F, G, H))
    if type in [1, 2]:
        I = IO.mirror(I)
    else:
        I = IO.flip(I)
    E.paste(I, (K, L))
    M = ist()
    M.name = O
    E.save(M, J)
    M.seek(0)
    await A.client.send_file(A.to_id, M, reply_to=N)
    await A.delete()


async def CM(R):
    D = False
    C = None
    A = R
    if A and A.media:
        if A.photo:
            B = A.photo
            E = _C
        elif A.document:
            if DAF(file_name="AnimatedSticker.tgs") in A.media.document.attributes:
                return D, C
            if A.gif or A.video or A.audio or A.voice:
                return D, C
            B = A.media.document
            if _A not in B.mime_type:
                return D, C
            E = B.mime_type.split("/")[1]
        else:
            return D, C
    else:
        return D, C
    if not B or B is C:
        return D, C
    else:
        return B, E
