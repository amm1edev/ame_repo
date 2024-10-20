# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MineEVO
# Author: sqlmerr
# Commands:
# .mprofile | .mcases     | .mmine     | .mperevod | .mautobonus
# .mautothx | .mautopromo | .mautosell
# ---------------------------------------------------------------------------------

# ░██████╗░██████╗░██╗░░░░░███╗░░░███╗███████╗██████╗░██████╗░
# ██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔════╝██╔══██╗██╔══██╗
# ╚█████╗░██║██╗██║██║░░░░░██╔████╔██║█████╗░░██████╔╝██████╔╝
# ░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗
# ██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║
# ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
# ---------------------------------------------------------------------------------------------
# Name: MineEVO
# Description: Полезный модуль для бота @mine_evo_bot
# Author: sqlmerr
# Commands:
# .mprofile | .mcases | .mperevod | .mmine | .mautobonus | .mautopromo | .mautothx | .mautosell
# ---------------------------------------------------------------------------------------------

# версия модуля
__version__ = (1, 1, 3)
# meta developer: @sqlmerr_m
# only hikka

# импортируем нужные библиотеки
import asyncio
import logging
import re

from telethon import events, functions, types
from telethon.tl.types import ChatAdminRights, Message

from .. import loader, utils

logger = logging.getLogger(__name__)


# сам класс модуля
@loader.tds
class MineEVO(loader.Module):
    """Полезный модуль для бота @mine_evo_bot"""

    # нужные переменные
    strings = {
        "name": "MineEVO",
        "lvl": "Ваш уровень",
        "mine_interval": "⏳ Интервал копания",
        "mine_status": "⚙️ Ну тип копаете вы или нет",
        "perevod_interval": "⏳ Интервал перевода лимитов",
        "autobonus_status": "⚙️ Получаете ли вы автоматически ежедневный бонус или нет",
        "autopromo_status": "⚙️ Пишите ли вы автоматически промо или нет",
        "autothx_status": "⚙️ Пишите ли вы автоматически Thx или нет",
        "autosell_status": "⚙️ Продаете ли вы руду или нет",
        "autoboost_status": (
            "⚙️ Используете ли вы буст денег 1.5 во время авто-продажи или нет"
        ),
    }

    # когда клиент готов к работе:
    async def client_ready(self):
        # создается чат
        self._mineevo_channel, _ = await utils.asset_channel(
            self._client,
            "MineEVO - чат",
            "Не пишите сюда. Этот чат предназначет для модуля MineEVO от @sqlmerr_m",
            silent=True,
            archive=True,
            _folder="hikka",
        )
        # в этот чат добавляется бот @mine_evo_bot
        await self.client(
            functions.channels.InviteToChannelRequest(
                self._mineevo_channel, ["@mine_evo_bot"]
            )
        )
        # и этому боту выдаются права админа, для корректной работы бота
        await self.client(
            functions.channels.EditAdminRequest(
                channel=self._mineevo_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(
                    ban_users=True, post_messages=True, edit_messages=True
                ),
                rank="MineEVO",
            )
        )

    # функция, связанная с ООП и нужная для создания конфига
    def __init__(self):
        self.thx = False
        self.mine = False
        self.perevod = False
        self.bonus = False
        self.sell = False
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "mine_interval",
                2.0,
                lambda: self.strings("mine_interval"),
                validator=loader.validators.Float(),
            ),
            loader.ConfigValue(
                "perevod_interval",
                2.0,
                lambda: self.strings("perevod_interval"),
                validator=loader.validators.Float(),
            ),
            loader.ConfigValue(
                "autopromo_status",
                True,
                lambda: self.strings("autopromo_status"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "autothx_status",
                False,
                lambda: self.strings("autothx_status"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "autoboost_status",
                False,
                lambda: self.strings("autoboost_status"),
                validator=loader.validators.Boolean(),
            ),
        )

    # .mprofile
    @loader.command()
    async def mprofile(self, message: Message):
        """отправляет в текущий чат ваш профиль в боте @mine_evo_bot"""
        await utils.answer(
            message, "<emoji document_id=5451882707875276247>🕯</emoji> Выполняю..."
        )
        # юб начинает диалог в чате с ассетами который создаётся автоматически
        async with self._client.conversation(self._mineevo_channel) as conv:
            await conv.send_message("профиль")
            # получаем ответ
            response = await conv.get_response()
        # пересылаем ответ
        await response.forward_to(message.to_id)
        await message.delete()

    # .mcases
    @loader.command()
    async def mcases(self, message: Message):
        """отправляет в текущий чат ваши кейсы в боте @mine_evo_bot"""
        await utils.answer(
            message, "<emoji document_id=5451882707875276247>🕯</emoji> Выполняю..."
        )
        # юб начинает диалог в чате с ассетами который создаётся автоматически
        async with self._client.conversation(self._mineevo_channel) as conv:
            await conv.send_message("кейсы")  # upload step
            response = await conv.get_response()  # first message
            # получаем ответ
        # пересылаем ответ
        await response.forward_to(message.to_id)
        await message.delete()

    # .mmine
    @loader.command()
    async def mmine(self, message: Message):
        """Автоматически копает за вас"""
        self.mine = not self.mine
        status = (
            "Копаю <emoji document_id=5282855481121976759>⛏</emoji>"
            if self.mine
            else "Больше не копаю <emoji document_id=5282855481121976759>⛏</emoji>"
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

        if self.mine:
            interval = self.config["mine_interval"]

            logger.debug("start mining...")
            # юб копает за вас
            while self.mine:
                await self.client.send_message("@mine_evo_bot", "коп")
                await asyncio.sleep(interval)
        else:
            return

    # .mperevod <кол-во лимитов> <ник чела в боте>
    @loader.command()
    async def mperevod(self, message: Message):
        """<кол-во лимитов> <ник чела в боте> - Автоматически переводит лимиты за вас"""
        self.perevod = not self.perevod
        status = (
            "Начинаю переводить лимиты <emoji"
            " document_id=5309799327093236710>🫥</emoji> "
            if self.perevod
            else (
                "Авто-перевод выключен <emoji document_id=5307675706283533118>🫥</emoji>"
            )
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

        if self.perevod:
            interval = self.config["perevod_interval"]
            # получаем аргументы
            args = utils.get_args_raw(message).split()

            # если аргументов нет
            if not args:
                await utils.answer(
                    message,
                    "введите аргументы: .mperevod <кол-во лимитов> <ник чела в боте>",
                )
                return
            limits = int(args[0])

            async with self._client.conversation(self._mineevo_channel) as conv:
                a = await conv.send_message(f"Перевести {args[1]} лимит")

                b = await conv.get_response()
                list_msgs_id = [a.id, b.id]

            if "перевел(а) игроку" in b.text:
                await self.client.delete_messages(
                    entity=self._mineevo_channel, message_ids=list_msgs_id
                )
            else:
                await utils.answer(
                    message,
                    (
                        "<emoji document_id=5447644880824181073>⚠️</emoji> Произошла"
                        f" ошибка:\n\n{b.text}"
                    ),
                )
                return await self.client.delete_messages(
                    entity=self._mineevo_channel, message_ids=list_msgs_id
                )

            logger.debug("starting to transfer limits...")
            # юб переводит лимиты
            while limits > 0:
                limits -= 1

                await self.client.send_message(
                    "@mine_evo_bot", f"Перевести {args[1]} лимит"
                )
                await asyncio.sleep(interval)

            await self.client.send_message(
                self._mineevo_channel,
                (
                    "<emoji document_id=5447644880824181073>⚠️</emoji> Все лимиты"
                    " переведены!\n\n<emoji document_id=5210956306952758910>👀</emoji>"
                    f" Кому: <code>{args[1]}</code>  |  <emoji"
                    " document_id=5456140674028019486>⚡️</emoji> Сколько:"
                    f" <b>{args[0]}</b>"
                ),
            )
        else:
            return

    # .mautobonus
    @loader.command()
    async def mautobonus(self, message: Message):
        """автоматически забирает ежедневный бонус"""
        self.bonus = not self.bonus
        status = (
            "Авто-еб включено <emoji document_id=5416081784641168838>🟢</emoji> "
            if self.bonus
            else "Авто-еб выключено <emoji document_id=5411225014148014586>🔴</emoji> "
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

        if self.bonus:
            while self.bonus:
                await self.client.send_message(self._mineevo_channel, "еб")
                await asyncio.sleep(86400)

        else:
            return

    # .mautothx
    @loader.command()
    async def mautothx(self, message: Message):
        """автоматически пишет thx"""
        self.thx = not self.thx
        status = "Авто-thx включено" if self.thx else "Авто-thx выключено"

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

        while self.thx:
            async with self._client.conversation(self._mineevo_channel) as conv:
                a = await conv.send_message("thx")
                # получаем ответ
                b = await conv.get_response()
                list_msgs_id = [a.id, b.id]

            if "благодарить некого." in b.text:
                await self.client.delete_messages(
                    entity=self._mineevo_channel, message_ids=list_msgs_id
                )
            elif "этого игрока за глобальный бустер!" in b.text:
                await self.client.delete_messages(
                    entity=self._mineevo_channel, message_ids=list_msgs_id
                )
            await asyncio.sleep(3600)

    # .mautopromo
    @loader.command()
    async def mautopromo(self, message: Message):
        """Включить/выключить авто-промо"""
        self.config["autopromo_status"] = not self.config["autopromo_status"]
        status = (
            "Авто-промо включено <emoji document_id=5424972470023104089>🔥</emoji>"
            if self.config["autopromo_status"]
            else "Авто-промо выключено <emoji document_id=5424972470023104089>🔥</emoji>"
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )

        while self.config["autothx"]:
            if self.config["autothx_status"]:
                async with self._client.conversation(self._mineevo_channel) as conv:
                    a = await conv.send_message("thx")
                    # получаем ответ
                    b = await conv.get_response()
                    list_msgs_id = [a.id, b.id]

                if "благодарить некого." in b.text:
                    await self.client.delete_messages(
                        entity=self._mineevo_channel, message_ids=list_msgs_id
                    )
                elif "этого игрока за глобальный бустер!" in b.text:
                    await self.client.delete_messages(
                        entity=self._mineevo_channel, message_ids=list_msgs_id
                    )
                await asyncio.sleep(3600)

    # auto-promo (idea: https://t.me/Demchik347), autothx
    @loader.watcher(only_messages=True)
    async def watcher(self, message: Message):
        if self.config["autopromo_status"] and message.chat_id == -1001892345917:
            promo_start = message.text.index("Промо ") + len(
                "Промо "
            )  # находим началопромокода
            promo_end = message.text.index("\n", promo_start)  # находим конец промокода
            promo_code = message.text[
                promo_start:promo_end
            ]  # извлекаем код из сообщения
            await self.client.send_message(self._mineevo_channel, f"Промо {promo_code}")

            logger.debug("было введено промо")

    # .mautosell
    @loader.command()
    async def mautosell(self, message: Message):
        """Включить/выключить авто-продажу"""
        self.sell = not self.sell
        status = (
            "Авто-продажа включена <emoji document_id=5409048419211682843>💲</emoji> "
            if self.sell
            else (
                "Авто-продажа выключена <emoji"
                " document_id=5409048419211682843>💲</emoji> "
            )
        )

        await utils.answer(
            message,
            "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(
                status
            ),
        )
        if self.sell:
            while self.sell:
                async with self._client.conversation(self._mineevo_channel) as conv:
                    if self.config["autoboost_status"]:
                        o = await conv.send_message("буст д 1.5")
                        oo = await conv.get_response()
                    a = await conv.send_message("инв")
                    # получаем ответ
                    b = await conv.get_response()
                    list_msgs_id = [a.id, b.id]
                await b.click(0)
                await asyncio.sleep(605)
                await self.client.delete_messages(
                    entity=self._mineevo_channel, message_ids=list_msgs_id
                )
        else:
            return
