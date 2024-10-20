# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: 01code
# Author: dorotorothequickend
# Commands:
# .codeit | .decode
# ---------------------------------------------------------------------------------

#                █████████████████████████████████████████
#                █────██────█────█────█───█────█────█────█
#                █─██──█─██─█─██─█─██─██─██─██─█─██─█─██─█
#                █─██──█─██─█────█─██─██─██─██─█────█─██─█
#                █─██──█─██─█─█─██─██─██─██─██─█─█─██─██─█
#                █────██────█─█─██────██─██────█─█─██────█
#                █████████████████████████████████████████
#
#
#                     Copyright 2022 t.me/Dorotoro
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://raw.githubusercontent.com/dorotorothequickend/DorotoroModules/main/banners/Dorotoro01code.png
# meta developer: @DorotoroMods

from .. import loader, utils

# https://clck.ru/32dhcu (StackOverflow)


@loader.tds
class tocodedecodemod(loader.Module):
    """Ваш персональный шифратор в двоичный код."""

    strings = {"name": "01code"}

    @loader.command()
    async def codeit(self, message):
        "<текст, который необходимо зашифровать> - шифрует ваш текст в двоичный код."
        args = utils.get_args_raw(message)

        def to_bits(args, encoding="utf-8", errors="surrogatepass"):
            bits = bin(int.from_bytes(args.encode(encoding, errors), "big"))[2:]
            return bits.zfill(8 * ((len(bits) + 7) // 8))

        result = to_bits(args)
        await utils.answer(
            message,
            (
                "<emoji document_id=4985930888572306287>🖥</emoji> <b>Текст"
                f" зашифрован:</b>\n<code>{result}</code>"
            ),
        )

    @loader.command()
    async def decode(self, message):
        "<код, который необходимо дешифровать> - дешифрует двоичный код."
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(
                message,
                (
                    "<emoji document_id=4985545282113503960>🖥</emoji> <b>Что"
                    " декодировать то?</b>"
                ),
            )
            return

        def from_bits(bits, encoding="utf-8", errors="surrogatepass"):
            n = int(bits, 2)
            return (
                n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors)
                or "\0"
            )

        result = from_bits(args)
        await utils.answer(
            message,
            (
                "<emoji document_id=4985930888572306287>🖥</emoji> <b>Результат"
                f" дешифровки:</b>\n<code>{result}</code>"
            ),
        )
