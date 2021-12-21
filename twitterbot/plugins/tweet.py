# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from .. import LOGGER
from twitterbot import AUTH, api
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command("tweet") & filters.user(AUTH))
async def twitter(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a Message !")
    event = await message.reply_text("Work on Progress...", quote=True)
    msg = message.reply_to_message
    MSG = "**Tweeted Successfully !!**"
    ca, dl = "#PostFromTG", None
    try:
        if msg.text:
            twish = api.update_status(msg.text + "\n\n" + ca)
        elif msg.photo or msg.animation or msg.video:
            if msg.caption:
                ca = msg.caption + "\n\n" + ca
            dl = await msg.download()
            media = api.media_upload(filename=dl)
            twish = api.update_status(status=ca, media_ids=[media.media_id])
            os.remove(dl)
        else:
            MSG = "Invalid Content"
            twish = None
    except Exception as e:
        LOGGER.exception(e)
        if dl:
            os.remove(dl)
        return await event.edit_text(
            str(e)
            + "\n\nIf you think that, this is error with Bot Codes.\n"
            + "You can create an Issue [here](https://github.com/New-dev0/TgTwitterBot)",
            disable_web_page_preview=True,
        )
    reply_markup = None
    if twish:
        twe = twish._json
        t_id = twe["id"]
        user = twe["user"]
        link = f"https://twitter.com/{user['screen_name']}/status/{t_id}"
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="View", url=link),
                    InlineKeyboardButton(text="Delete", callback_data=f"del{t_id}"),
                ]
            ]
        )
    await event.delete()
    await message.reply_text(MSG, reply_markup=reply_markup, quote=True)
