# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Entziferrer
# Author: GD-alt
# Commands:
# .scancode
# ---------------------------------------------------------------------------------

# `7MMM.     ,MMF'`7MMM.     ,MMF'   `7MMM.     ,MMF'              `7MM
# MMMb    dPMM    MMMb    dPMM       MMMb    dPMM                  MM
# M YM   ,M MM    M YM   ,M MM       M YM   ,M MM  ,pW"Wq.    ,M""bMM  ,pP"Ybd
# M  Mb  M' MM    M  Mb  M' MM       M  Mb  M' MM 6W'   `Wb ,AP    MM  8I   `"
# M  YM.P'  MM    M  YM.P'  MM mmmmm M  YM.P'  MM 8M     M8 8MI    MM  `YMMMa.
# M  `YM'   MM    M  `YM'   MM       M  `YM'   MM YA.   ,A9 `Mb    MM  L.   I8
# .JML. `'  .JMML..JML. `'  .JMML.   .JML. `'  .JMML.`Ybmd9'   `Wbmd"MML.M9mmmP'
#
# (c) 2023 — licensed under Apache 2.0 — https://www.apache.org/licenses/LICENSE-2.0
# meta developer: @mm_mods
# meta pic: https://img.icons8.com/stickers/256/qr-code.png

import logging
import urllib.parse

import requests
from telethon.tl.patched import Message
from telethon.tl.types import InputGeoPoint, InputMediaGeoPoint

from .. import loader, utils

logger = logging.getLogger(__name__)


async def check_photo(reply_message: Message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            return reply_message.photo
        else:
            return False
    else:
        return False


class Parsers:
    @staticmethod
    def parse_mecard(data: str):
        if not data.startswith("MECARD:"):
            return False

        data = data.replace("MECARD:", "")
        data = data.split(";")

        result = {}

        for item in data:
            try:
                datatype, value = item.split(":")
            except ValueError:
                continue

            if datatype == "N":
                result["name"] = value
            elif datatype == "TEL":
                result["phone"] = value
            elif datatype == "EMAIL":
                result["email"] = value
            elif datatype == "ADR":
                result["address"] = value
            elif datatype == "URL":
                result["url"] = value
            elif datatype == "ORG":
                result["organisation"] = value
            elif datatype == "NOTE":
                result["note"] = value
            else:
                continue

        return result

    @staticmethod
    def parse_wifi(data: str):
        if not data.startswith("WIFI:"):
            return False

        data = data.replace("WIFI:", "")
        data = data.split(";")

        result = {}

        for item in data:
            try:
                datatype, value = item.split(":")
            except ValueError:
                continue
            if datatype == "S":
                result["ssid"] = value
            elif datatype == "P":
                result["password"] = value
            elif datatype == "T":
                result["encryption"] = value
            else:
                continue

        if "ssid" not in result:
            return False

        if "password" not in result:
            result["password"] = "[none]"

        if "encryption" not in result:
            result["encryption"] = "[none]"

        return result

    @staticmethod
    def parse_geo(data: str):
        if not data.startswith("geo:"):
            return False

        data = data.replace("geo:", "")
        lat, lon = data.split(",")

        result = {"lat": lat, "lon": lon}

        return [result, InputMediaGeoPoint(InputGeoPoint(lat, lon))]

    @staticmethod
    def parse_sms(data: str):
        if not data.startswith("smsto:"):
            return False

        data = data.replace("smsto:", "")
        data = data.split(":")
        phone = data[0]
        try:
            message = data[1]
        except IndexError:
            message = "[none]"

        result = {"phone": phone, "message": message}

        return result

    @staticmethod
    def parse_phone(data: str):
        if not data.startswith("tel:"):
            return False

        data = data.replace("tel:", "")
        result = {"phone": data}

        return result

    @staticmethod
    def parse_email(data: str):
        if (not data.startswith("mailto:")) and (not data.startswith("MATMSG:")):
            return False

        if_expanded = True if data.startswith("MATMSG:TO:") else False

        if if_expanded:
            result = {}
            data = data.replace("MATMSG:", "")
            data = data.split(";")
            for item in data:
                try:
                    datatype, value = item.split(":")
                except ValueError:
                    continue
                if datatype == "TO":
                    result["email"] = value
                elif datatype == "SUB":
                    result["subject"] = value
                elif datatype == "BODY":
                    result["body"] = value
                else:
                    continue

            if "email" not in result:
                return False

            if "subject" not in result:
                result["subject"] = "[none]"

            if "body" not in result:
                result["body"] = "[none]"

        else:
            data = data.replace("mailto:", "")

            result = {"email": data}

        return result

    @staticmethod
    def parse_vevent(data: str):
        if not data.startswith("BEGIN:VEVENT"):
            return False

        data = data.split("\n")
        result = {}

        for item in data:
            try:
                datatype, value = item.split(":")
            except ValueError:
                continue
            if datatype == "SUMMARY":
                result["summary"] = value
            elif datatype == "LOCATION":
                result["location"] = value
            elif datatype == "DESCRIPTION":
                result["description"] = value
            elif datatype == "DTSTART":
                result["start"] = (
                    f'{value.split("T")[0][:4]}.{value.split("T")[0][4:6]}.{value.split("T")[0][6:8]} '
                    f'{value.split("T")[1][:2]}:{value.split("T")[1][2:4]}:{value.split("1")[0][4:]}'
                    if "T" in value
                    else f"{value[:4]}.{value[4:6]}.{value[6:8]}"
                )
            elif datatype == "DTEND":
                result["end"] = (
                    f'{value.split("T")[0][:4]}.{value.split("T")[0][4:6]}.{value.split("T")[0][6:8]} '
                    f'{value.split("T")[1][:2]}:{value.split("T")[1][2:4]}:{value.split("1")[0][4:]}'
                    if "T" in value
                    else f"{value[:4]}.{value[4:6]}.{value[6:8]}"
                )
            else:
                continue

        if "summary" not in result:
            return False

        if "location" not in result:
            result["location"] = "[none]"

        if "description" not in result:
            result["description"] = "[none]"

        if "start" not in result:
            result["start"] = "[none]"

        if "end" not in result:
            result["end"] = "[none]"

        return result


class EntziffererMod(loader.Module):
    """Decoding QR codes."""

    strings = {
        "name": "Entzifferer",
        "media?": "🖼 <b>Reply to a message, containing code to scan.</b>",
        "qr?!": "❌ <b>There's no code to scan.</b>",
        "decoding": "🔍 <b>Decoding…</b>",
        "uploading": "📤 <b>Uploading your file…</b>",
        "processing": "📊 <b>Processing result…</b>",
        "error": "❌ <b>Something went wrong.</b>\nError: <code>{}</code>",
        "result": "📄 <b>Result:</b>",
        "qr": "🔍 <b>QR code:</b>",
        "data": "Data: <code>{}</code>",
        "contact": "Contact:\n{}",
        "phone": "Phone: <code>{}</code>",
        "sms": "SMS: <code>{}</code> to <code>{}</code>",
        "geolocation": (
            "Geolocation: latitude: <code>{}</code>, longitude: <code>{}</code>"
        ),
        "email": "Email: <code>{}</code>",
        "email_exp": (
            "Email: <code>{}</code> (subject: <code>{}</code>, body: <code>{}</code>)"
        ),
        "wifi": (
            "Wi-Fi:\nSSID: <code>{}</code> | Password: <code>{}</code> | Encryption:"
            " <i>{}</i>"
        ),
        "url": "URL: {}",
        "calendar": "Event: {}",
        "MC-name": "👤 Name: <code>{}</code>",
        "MC-phone": "☎ Phone: <code>{}</code>",
        "MC-email": "📮 Email: <code>{}</code>",
        "MC-address": "🏡 Address: <code>{}</code>",
        "MC-note": "📝 Note: <code>{}</code>",
        "MC-url": "🔗 URL: <code>{}</code>",
        "MC-organisation": "💼 Organisation: <code>{}</code>",
        "VE-summary": "🎯 Summary: <code>{}</code>",
        "VE-location": "🗺 Location: <code>{}</code>",
        "VE-description": "📜 Description: <code>{}</code>",
        "VE-start": "➡ Start: <code>{}</code>",
        "VE-end": "⬅ End: <code>{}</code>",
    }

    strings_ru = (
        {
            "name": "Entzifferer",
            "media?": (
                "🖼 <b>Ответьте на сообщение, содержащее код, для сканирования.</b>"
            ),
            "qr?!": "❌ <b>Нет кода для сканирования.</b>",
            "decoding": "🔍 <b>Сканирую…</b>",
            "uploading": "📤 <b>Загружаю…</b>",
            "processing": "📊 <b>Обрабатываю результат…</b>",
            "error": "❌ <b>Что-то пошло не так.</b>\nОшибка: <code>{}</code>",
            "result": "📄 <b>Результат:</b>",
            "qr": "🔍 <b>QR-код:</b>",
            "data": "Данные: <code>{}</code>",
            "contact": "Контакт:\n{}",
            "phone": "Телефон: <code>{}</code>",
            "sms": "SMS: <code>{}</code> на номер <code>{}</code>",
            "geolocation": (
                "Геолокация: широта: <code>{}</code>, долгота: <code>{}</code>"
            ),
            "email": "Почта: <code>{}</code>",
            "email_exp": (
                "Почта: <code>{}</code> (тема: <code>{}</code>, текст: <code>{}</code>)"
            ),
            "wifi": (
                "Wi-Fi:\nSSID: <code>{}</code> | Пароль: <code>{}</code> | Шифрование:"
                " <i>{}</i>"
            ),
            "url": "URL: {}",
            "calendar": "Событие: {}",
            "MC-name": "👤 Имя: <code>{}</code>",
            "MC-phone": "☎ Телефон: <code>{}</code>",
            "MC-email": "📮 Почта: <code>{}</code>",
            "MC-address": "🏡 Адрес: <code>{}</code>",
            "MC-note": "📝 Примечание: <code>{}</code>",
            "MC-url": "🔗 URL: <code>{}</code>",
            "MC-organisation": "💼 Организация: <code>{}</code>",
            "VE-summary": "🎯 Заголовок: <code>{}</code>",
            "VE-location": "🗺 Место: <code>{}</code>",
            "VE-description": "📜 Описание: <code>{}</code>",
            "VE-start": "➡ Начало: <code>{}</code>",
            "VE-end": "⬅ Конец: <code>{}</code>",
            "_cls_doc": "Декодирует QR-коды.",
            "_cmd_doc_scancode": "Сканировать QR-код",
        },
    )

    strings_de = {
        "name": "Entzifferer",
        "media?": "🖼 <b>Antworte auf eine Nachricht, die einen Code enthält.</b>",
        "qr?!": "❌ <b>Es gibt keinen Code zum Scannen.</b>",
        "decoding": "🔍 <b>Scanne…</b>",
        "uploading": "📤 <b>Lade deine Datei hoch…</b>",
        "processing": "📊 <b>Verarbeite das Ergebnis…</b>",
        "error": "❌ <b>Etwas ist schief gelaufen.</b>\nFehler: <code>{}</code>",
        "result": "📄 <b>Ergebnis:</b>",
        "qr": "🔍 <b>QR-Code:</b>",
        "data": "Daten: <code>{}</code>",
        "сontact": "Kontakt:\n{}",
        "phone": "Telefon: <code>{}</code>",
        "sms": "SMS: <code>{}</code> zu <code>{}</code>",
        "geolocation": "Geolocation: Breite: <code>{}</code>, Länge: <code>{}</code>",
        "email": "E-Mail: <code>{}</code>",
        "email_exp": (
            "E-Mail: <code>{}</code> (Betreff: <code>{}</code>, Text: <code>{}</code>)"
        ),
        "wifi": (
            "WLAN:\nSSID: <code>{}</code> | Passwort: <code>{}</code> |"
            " Verschlüsselung: <i>{}</i>"
        ),
        "url": "URL: {}",
        "calendar": "Ereignis: {}",
        "MC-name": "👤 Name: <code>{}</code>",
        "MC-phone": "☎ Telefon: <code>{}</code>",
        "MC-email": "📮 E-mail: <code>{}</code>",
        "MC-address": "🏡 Address: <code>{}</code>",
        "MC-note": "📝 Notiz: <code>{}</code>",
        "MC-url": "🔗 URL: <code>{}</code>",
        "MC-organisation": "💼 Arbeitsplatz: <code>{}</code>",
        "VE-summary": "🎯 Zusammenfassung: <code>{}</code>",
        "VE-location": "🗺 Ort: <code>{}</code>",
        "VE-description": "📜 Beschreibung: <code>{}</code>",
        "VE-start": "➡ Start: <code>{}</code>",
        "VE-end": "⬅ Ende: <code>{}</code>",
        "_cls_doc": "Entziffere QR-Codes.",
        "_cmd_doc_scancode": "Scanne einen QR-Code",
    }

    # noinspection PyCallingNonCallable
    async def scancodecmd(self, m: Message):
        """Scan a QR code."""
        reply = await m.get_reply_message()

        if not reply:
            return await utils.answer(m, self.strings("media?", m))

        if not (await check_photo(reply)):
            return await utils.answer(m, self.strings("qr?!", m))

        await utils.answer(m, self.strings("uploading", m))

        file = await m.client.download_file(reply.photo, bytes)

        path = requests.post(
            "https://te.legra.ph/upload", files={"file": ("file", file, None)}
        ).json()

        try:
            link = "https://te.legra.ph" + path[0]["src"]
        except KeyError:
            link = path["error"]

        await utils.answer(m, self.strings("decoding"))

        path = urllib.parse.quote_plus(link)
        url = f"https://api.qrserver.com/v1/read-qr-code/?fileurl={path}"

        try:
            r = requests.get(url).json()
        except Exception as e:
            logging.error(e)
            return await utils.answer(m, self.strings("error").format(f"{e}"))

        if r[0]["symbol"][0]["error"]:
            return await utils.answer(m, self.strings("qr?!"))

        r = r[0]["symbol"][0]["data"]

        await utils.answer(m, self.strings("processing"))

        res = ""

        if len(r.split("\nQR-Code:")) > 1:
            r = r.split("\nQR-Code:")

            for i in r:
                res += f'{self.strings("qr")}\n{self.classify(i)}\n\n'

        else:
            res = f"{self.strings('qr')}\n{str(self.classify(r))}"

        await utils.answer(m, f'<u>{self.strings("result")}</u>\n\n{res}')

    # noinspection PyCallingNonCallable
    def classify(self, r: str):
        if_url = urllib.parse.urlparse(r)
        if all([if_url.scheme, if_url.netloc]):
            r = self.strings("url").format(r)

        elif Parsers.parse_mecard(r):
            mecard = Parsers.parse_mecard(r)

            r = ""

            for key, value in mecard.items():
                r = r + self.strings(f"MC-{key}").format(value) + "\n"

            r = self.strings("contact").format(r)

        elif Parsers.parse_wifi(r):
            wifi = Parsers.parse_wifi(r)

            r = self.strings("wifi").format(
                wifi["ssid"], wifi["password"], wifi["encryption"]
            )

        elif Parsers.parse_geo(r):
            r = Parsers.parse_geo(r)
            r = self.strings("geolocation").format(r[0]["lat"], r[0]["lon"])

        elif Parsers.parse_sms(r):
            r = self.strings("sms").format(
                Parsers.parse_sms(r)["message"], Parsers.parse_sms(r)["phone"]
            )

        elif Parsers.parse_phone(r):
            r = Parsers.parse_phone(r)
            r = self.strings("phone").format(r["phone"])

        elif Parsers.parse_email(r):
            if len(list(Parsers.parse_email(r).keys())) > 1:
                r = self.strings("email_exp").format(
                    Parsers.parse_email(r)["email"],
                    Parsers.parse_email(r)["subject"],
                    Parsers.parse_email(r)["body"],
                )
            else:
                r = self.strings("email").format(Parsers.parse_email(r)["email"])

        elif Parsers.parse_vevent(r):
            vevent = Parsers.parse_vevent(r)

            r = ""

            for key, value in vevent.items():
                r = r + self.strings(f"VE-{key}").format(value) + "\n"

            r = self.strings("calendar").format(r)

        else:
            r = self.strings("data").format(r)

        return r
