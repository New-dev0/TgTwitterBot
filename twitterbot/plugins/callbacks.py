# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from twitterbot import AUTH, api, HELP_MARKUP
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from twitterbot.funcs import simstuff, status_reply_markup, user_reply_markup
from .. import LOGGER

HELPBUT = [InlineKeyboardButton(text="Help Menu", callback_data="openmenu")]


@Client.on_callback_query(~filters.user(AUTH))
async def forunauth(_, query):
    text = "❌ You are Not Authorised to Use Me !"
    await query.answer(text, show_alert=True)


@Client.on_callback_query(filters.regex("^user(.*)"))
async def callie(_, query):
    match = query.matches[0].group(1)
    try:
        user = api.get_user(user_id=match)
    except Exception as er:
        await query.answer(str(er), show_alert=True)
        return LOGGER.exception(er)
    text = simstuff(user._json)
    reply_markup = InlineKeyboardMarkup(user_reply_markup(user))
    await query.edit_message_text(
        text, reply_markup=reply_markup, disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^openmenu$"))
async def quetme(client, query):
    await query.edit_message_text(
        "**[Telegram - Twitter - Bot]" + "(https://github.com/New-dev0/TgTwitterBot)**",
        reply_markup=HELP_MARKUP,
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("^favr_(.*)"))
async def favunfav(client, query):
    match = query.matches[0].group(1).split("_")
    todo = match[0]
    t_id = int(match[1])
    try:
        if todo == "lk":
            text = "Unliked !"
            stat = api.destroy_favorite(id=t_id)
        else:
            text = "Liked !"
            stat = api.create_favorite(id=t_id)
    except Exception as er:
        await query.answer(str(er), show_alert=True)
        return LOGGER.exception(er)
    await query.answer(text, show_alert=True)
    reply_markup = InlineKeyboardMarkup(status_reply_markup(stat))
    await query.edit_message_reply_markup(reply_markup)


@Client.on_callback_query(filters.regex("^fuflow_(.*)"))
async def folowunf(_, query):
    to_ = query.matches[0].group(1).split("_")
    todo = to_[0]
    t_id = int(to_[1])
    try:
        if todo == "fl":
            text = "Unfollowed !"
            user = api.destroy_friendship(user_id=t_id)
        else:
            text = "Starting Following!"
            user = api.create_friendship(user_id=t_id)
    except Exception as er:
        await query.answer(str(er), show_alert=True)
        return LOGGER.exception(er)
    user = api.get_user(user_id=user._json["id"])
    text += f"\nTotal Followings - {user._json['followers_count']}"
    await query.answer(text, show_alert=True)
    reply_markup = InlineKeyboardMarkup(user_reply_markup(user))
    await query.edit_message_reply_markup(reply_markup)


@Client.on_callback_query(filters.regex("^rtt_(.*)"))
async def retweet(_, query):
    match = query.matches[0].group(1).split("_")
    to_do = match[0]
    status_id = match[1]
    try:
        if to_do == "rt":
            api.retweet(id=status_id)
            mk = "ReTweeted !"
        else:
            api.unretweet(id=status_id)
            mk = "Deleted ReTweet !"
    except Exception as er:
        await query.answer(str(er), show_alert=True)
        return LOGGER.exception(er)
    status = api.get_status(id=status_id)
    await query.answer(mk, show_alert=True)
    reply_markup = status_reply_markup(status)
    await query.edit_message_reply_markup(InlineKeyboardMarkup(reply_markup))


@Client.on_callback_query(filters.regex("^del(.*)"))
async def delstatus(_, query):
    status = query.matches[0].group(1)
    try:
        api.destroy_status(id=status)
    except Exception as er:
        await query.answer(str(er), show_alert=True)
        return LOGGER.exception(er)
    await query.edit_message_text("**Deleted !**", reply_markup=None)
