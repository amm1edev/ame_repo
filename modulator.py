# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: modulator
# Description: Modulate pitch of voice
# Author: KeyZenD
# Commands:
# Failed to parse
# ---------------------------------------------------------------------------------


R = int
Q = float
E = len
import io
import os

import numpy as G
from pydub import AudioSegment as M

# requires: pydub numpy
from .. import loader as A
from .. import utils


class BMod(A.Module):
    "Modulate pitch of voice"
    strings = {"name": "Modulator"}

    async def modulatecmd(W, message):
        A = message
        B = await A.get_reply_message()
        if not B or not B.file and "audio" in B.file.mime_type:
            return await A.edit("<b>Reply to audio!</b>")
        N = io.BytesIO(await B.download_media(bytes))
        N.seek(0)
        X = []
        H = M.empty()
        I = M.from_file(N)
        I = [A for A in I]
        C = utils.get_args(A)
        J = 0.9, 1.1, 0.01
        O = 3
        if E(C) == 3:
            try:
                J = (Q(A) for A in C)
            except:
                pass
        if E(C) == 4:
            try:
                J = (Q(A) for A in C[0:3])
                O = R(C[3])
            except:
                pass
        P = G.repeat(G.arange(*J), O)
        S = G.sin(P)
        D = list(map(lambda x: x[0] * x[-1], zip(P, S)))
        K = 1
        await A.edit("<b>Modulating...</b>")
        for T, L in enumerate(I):
            U = D[T % E(D)]
            K += 1
            if K > E(D):
                K = 0
                D = D[::-1]
            V = R(L.frame_rate * U)
            H += L._spawn(L.raw_data, overrides={"frame_rate": V})
        F = io.BytesIO()
        F.name = "modulator_by_keyzend.ogg"
        H.export(F, format="ogg", bitrate="64k", codec="libopus")
        F.seek(0)
        await A.client.send_file(
            A.to_id, F, reply_to=B.id, voice_note=True, duration=E(H) / 1000
        )
        await A.delete()
