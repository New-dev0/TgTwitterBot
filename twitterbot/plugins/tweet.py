# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from twitterbot import AUTH, api
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command("tweet") & filters.user(AUTH))
async def twitter(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a Message !")
    msg = message.reply_to_message
    MSG = "**Tweeted Successfully !!**"
    ca = "#PostFromTG"
    if msg.text:
        twish = api.update_status(msg.text + "\n\n" + ca)
    elif msg.photo or msg.video:
        if msg.caption:
            ca = msg.caption + "\n\n" + ca
        dl = await msg.download()
        twish = api.update_with_media(dl, ca)
        os.remove(dl)
    else:
        MSG = "Invalid Content"
    reply_markup = None
    if twish:
        twe = twish._json
        t_id = twe["id"]
        user = twe["user"]
        link = f"https://twitter.com/{user['screen_name']}/status/{t_id}"
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="View", url=link)],
            [InlineKeyboardButton(text="Delete", callback_data=f"del{t_id}")]])
    await message.reply_text(MSG,
                             reply_markup=reply_markup,
                             quote=True)
