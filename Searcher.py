# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the CC BY-NC-ND 4.0.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Searcher
# Author: D4n13l3k00
# Commands:
# .srch
# ---------------------------------------------------------------------------------

# .------.------.------.------.------.------.------.------.------.------.
# |D.--. |4.--. |N.--. |1.--. |3.--. |L.--. |3.--. |K.--. |0.--. |0.--. |
# | :/\: | :/\: | :(): | :/\: | :(): | :/\: | :(): | :/\: | :/\: | :/\: |
# | (__) | :\/: | ()() | (__) | ()() | (__) | ()() | :\/: | :\/: | :\/: |
# | '--'D| '--'4| '--'N| '--'1| '--'3| '--'L| '--'3| '--'K| '--'0| '--'0|
# `------`------`------`------`------`------`------`------`------`------'
#
#                     Copyright 2023 t.me/D4n13l3k00
#           Licensed under the Creative Commons CC BY-NC-ND 4.0
#
#                    Full license text can be found at:
#       https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
#
#                           Human-friendly one:
#            https://creativecommons.org/licenses/by-nc-nd/4.0

# meta developer: @D4n13l3k00


from .. import loader, utils  # type: ignore


def register(cb):
    cb(SearcherMod())


class SearcherMod(loader.Module):
    strings = {"name": "Searcher"}

    def __init__(self):
        self.name = self.strings["name"]

    async def srchcmd(self, m):
        """.srch <канал/чат> <запрос>
        Найти пост в канале/чате сообщение и переслать
        """
        args = utils.get_args_raw(m)
        if not args:
            return await m.edit("[Search] Укажите аргументы!")
        if len(args.split(" ")) == 1:
            return await m.edit("[Search] Укажите запрос!")
        ch = args.split(" ")[0]
        req = args.split(" ", 1)[1]
        try:
            ms = await m.client.get_messages(ch, search=req, limit=100)
        except Exception as e:
            return await m.edit("[Searcher] " + str(e.args))
        if ms.total == 0:
            return await m.edit("[Searcher] Данных по запросу нет")
        for i in ms:
            await i.forward_to(m.to_id)
        await m.delete()
