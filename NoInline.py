# `7MMM.     ,MMF'`7MMM.     ,MMF'   `7MMM.     ,MMF'              `7MM
# MMMb    dPMM    MMMb    dPMM       MMMb    dPMM                  MM
# M YM   ,M MM    M YM   ,M MM       M YM   ,M MM  ,pW"Wq.    ,M""bMM  ,pP"Ybd
# M  Mb  M' MM    M  Mb  M' MM       M  Mb  M' MM 6W'   `Wb ,AP    MM  8I   `"
# M  YM.P'  MM    M  YM.P'  MM mmmmm M  YM.P'  MM 8M     M8 8MI    MM  `YMMMa.
# M  `YM'   MM    M  `YM'   MM       M  `YM'   MM YA.   ,A9 `Mb    MM  L.   I8
# .JML. `'  .JMML..JML. `'  .JMML.   .JML. `'  .JMML.`Ybmd9'   `Wbmd"MML.M9mmmP'
#
# (c) 2022 — licensed under Apache 2.0 — https://www.apache.org/licenses/LICENSE-2.0

# meta pic: https://img.icons8.com/emoji/344/mechanical-arm.png
# meta developer: @mm_mods

import logging

from telethon.tl.types import Message, PeerChannel

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class NoInlineMod(loader.Module):
    """Turns on/off inline bots using ability."""

    strings = {
        "name": "NoInline",
        "group?!": "👥 <b>This command must be used in group.</b>",
        "on": "👤 <b>Now only admins can use inline bots.</b>",
        "off": "🤖 <b>Now all members can use inline bots.</b>",
        "status-on": "👤❕ <b>Only admins can use inline bots here.</b>",
        "status-off": "🤖❕ <b>All members can use inline bots here.</b>",
        "rights?!": "😔 <b>Error….</b>\nCode: <code>{}</code>",
    }

    strings_ru = {
        "name": "NoInline",
        "group?!": "👥 <b>Работает лишь в группах.</b>",
        "on": "👤 <b>Теперь лишь админы могут использовать инлайн-ботов.</b>",
        "off": "🤖 <b>Теперь все могут использовать инлайн-ботов.</b>",
        "status-on": "👤❕ <b>Здесь лишь админы могут использовать инлайн-ботов.</b>",
        "status-off": "🤖❕ <b>Здесь все могут использовать инлайн-ботов.</b>",
        "rights?!": "😔 <b>Ошибка…</b>\nКод: <code>{}</code>",
        "_cls_doc": "Переключает и проверяет права на использование инлайн-ботов.",
        "_cmd_doc_switchib": "Переключает права на использование инлайн-ботов",
        "_cmd_doc_checkib": "Проверяет права на использование инлайн-ботов",
    }

    async def switchibcmd(self, m: Message):
        """Switches inline bots using rights."""
        if not isinstance(m.peer_id, PeerChannel):
            return await utils.answer(m, self.strings("group?!"))
        if not (await m.client.get_permissions(utils.get_chat_id(m))).send_inline:
            try:
                await m.client.edit_permissions(utils.get_chat_id(m), send_inline=False)
            except Exception as e:
                return await utils.answer(m, self.strings("rights?!").format(e))
            return await utils.answer(m, self.strings("on"))
        else:
            try:
                await m.client.edit_permissions(utils.get_chat_id(m), send_inline=True)
            except Exception as e:
                return await utils.answer(m, self.strings("rights?!").format(e))
            return await utils.answer(m, self.strings("off"))

    async def checkibcmd(self, m: Message):
        """Checks inline bots using rights."""
        if not isinstance(m.peer_id, PeerChannel):
            return await utils.answer(m, self.strings("group?!"))
        if not (await m.client.get_permissions(utils.get_chat_id(m))).send_inline:
            return await utils.answer(m, self.strings("status-off"))
        else:
            return await utils.answer(m, self.strings("status-on"))
