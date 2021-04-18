# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from twitterbot import AUTH, api, HELP_MARKUP
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from twitterbot.funcs import simstuff

HELPBUT = [InlineKeyboardButton(text="Help Menu", callback_data="openmenu")]


@Client.on_callback_query(~filters.user(AUTH))
async def forunauth(client, query):
    text = "❌ You are Not Authorised to Use Me !"
    await query.answer(text, show_alert=True)


@Client.on_callback_query(filters.regex("^user(.*)"))
async def callie(client, query):
    match = query.matches[0].group(1)
    user = api.get_user(match)._json
    mt = "Follow"
    if user["following"]:
        mt = "UnFollow"
    un = user['screen_name']
    uli = f"https://twitter.com/{un}"
    text = simstuff(user, uli)
    await query.edit_message_text(text, disable_web_page_preview=True)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="View on Twitter", url=uli)],
        [InlineKeyboardButton(text=mt, callback_data=f"fuflow{match}")],
        HELPBUT])
    await query.edit_message_reply_markup(reply_markup)


@Client.on_callback_query(filters.regex("^openmenu$"))
async def quetme(client, query):
    await query.edit_message_text(
        "[**Telegram - Twitter - Bot**]" + 
        "(https://github.com/New-dev0/TgTwitterBot)")
    await query.edit_message_reply_markup(HELP_MARKUP)


@Client.on_callback_query(filters.regex("^favr(.*)"))
async def favunfav(client, query):
    t_id = query.matches[0].group(1)
    tweet = api.get_status(t_id)._json
    user = tweet["user"]
    stf = tweet["favorited"]
    count = tweet["favorite_count"]
    btext = "UnLike ♡"
    if stf:
        text = "Unliked !"
        api.destroy_favorite(t_id)
        count = count - 1
        btext = "Like ❤️"
    else:
        text = "Liked !"
        api.create_favorite(t_id)
        count = count + 1
    text += f"\nTotal Counts - {count}"
    lpo = f"https://twitter.com/{user['screen_name']}/status/{t_id}"
    await query.answer(text, show_alert=True)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="View", url=lpo),
         InlineKeyboardButton(text="User", callback_data=f"user{user['id']}")],
        [InlineKeyboardButton(text=btext, callback_data=f"favr{t_id}")]])
    await query.edit_message_reply_markup(reply_markup)


@Client.on_callback_query(filters.regex("^fuflow(.*)"))
async def folowunf(client, query):
    t_id = query.matches[0].group(1)
    user = api.get_user(t_id)._json
    stf = user["following"]
    count = user["followers_count"]
    uname = user['screen_name']
    if stf:
        text = f"Unfollowed @{uname}!"
        fum = "Follow"
        api.destroy_friendship(t_id)
    else:
        text = f"Starting Following @{uname} !"
        api.create_friendship(t_id)
        fum = "UnFollow"
    text += f"\nTotal Followings - {count}"
    lpo = f"https://twitter.com/{uname}"
    await query.answer(text, show_alert=True)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="View", url=lpo),
         InlineKeyboardButton(text=fum, callback_data=f"fuflow{t_id}")],
        HELPBUT])
    await query.edit_message_reply_markup(reply_markup)


@Client.on_callback_query(filters.regex("^del(.*)"))
async def delstatus(client, query):
    status = query.matches[0].group(1)
    api.destroy_status(status)
    await query.edit_message_text("**Deleted !**")
    await query.edit_message_reply_markup(None)


@Client.on_callback_query(filters.regex("^block(.*)"))
async def blockuser(client, query):
    u_id = query.matches[0].group(1)
    api.create_block(u_id)
    await query.answer("Blocked !", show_alert=True)
    await query.edit_message_reply_markup(InlineKeyboardMarkup([
        [InlineKeyboardButton(text="UnBlock", callback_data=f"ubk{u_id}")],
        HELPBUT]))


@Client.on_callback_query(filters.regex("^ubk(.*)"))
async def unblockuser(client, query):
    u_id = query.matches[0].group(1)
    api.create_block(u_id)
    await query.answer("UnBlocked !", show_alert=True)
    await query.edit_message_reply_markup(InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Block", callback_data=f"block{u_id}")],
        HELPBUT]))
