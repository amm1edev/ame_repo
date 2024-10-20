# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: Gitinfo
# Author: DziruModules
# Commands:
# .gitinfo
# ---------------------------------------------------------------------------------

#
# █▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
# █▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://raw.githubusercontent.com/DziruModules/assets/master/DziruModules.jpg
# meta banner: https://raw.githubusercontent.com/DziruModules/assets/master/GitInfo.png
# scope: hikka_only
# version: 1.0

import requests

from .. import loader, utils


class GitInfoMod(loader.Module):
    """Get Github user info, simply type username"""

    strings = {
        "name": "GitInfo",
    }

    async def gitinfocmd(self, message):
        """<username>"""
        args = utils.get_args_raw(message)
        gitapi = "https://api.github.com/users/{}".format(args)
        s = requests.get(gitapi)
        if s.status_code != 404:
            b = s.json()
            avatar_url = b["avatar_url"]
            html_url = b["html_url"]
            name = b["name"]
            blog = b["blog"]
            location = b["location"]
            bio = b["bio"]
            created_at = b["created_at"]
            await self._client.send_file(
                message.chat_id,
                caption=(
                    "<emoji document_id=5974038293120027938>👤</emoji> <b>Name:"
                    " </b><code>{}</code>\n<emoji"
                    " document_id=5974492756494519709>🔗</emoji> <b>Link:"
                    " </b><code>{}</code>\n\n<emoji"
                    " document_id=5972183258090179945>💬</emoji> <b>Blog:"
                    " </b><code>{}</code>\n<emoji"
                    " document_id=5979027086612892618>📍</emoji> <b>Location:"
                    " </b><code>{}</code>\n\n<emoji"
                    " document_id=5972158252790582632>🗒</emoji> <b>Bio:"
                    " </b><code>{}</code>\n<emoji"
                    " document_id=6039550820855319523>🔎</emoji> <b>Profile Created:"
                    " </b><code>{}</code>".format(
                        name, html_url, blog, location, bio, created_at
                    )
                ),
                file=avatar_url,
                force_document=False,
                allow_cache=False,
                reply_to=message,
            )
            await message.delete()
        else:
            await message.edit(
                "<emoji document_id=5974097404754922968>🚫</emoji> <b>Username"
                " </b><code> {} </code><b>is not available</b>".format(args, s.text)
            )
