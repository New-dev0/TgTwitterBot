# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from twitterbot import AUTH, HELP_MARKUP, TLOGO, HNDLR
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


START_MSG = """
Hi {frm}, I am Telegram-Twitter-Bot

You can use me Inline and do possible stuff on
Twitter from Telegram Only !

Send {HLR}help to explore !
"""


@Client.on_message(filters.command("start", prefixes=HNDLR)
                   & filters.user(AUTH))
async def startmsg(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Support Group",
                              url="t.me/FutureCodesChat")],
        [InlineKeyboardButton(
            text="Repo",
            url="https://github.com/New-dev0/TgTwitterBot")]])
    await message.reply_text(
        START_MSG.format(frm=message.from_user.mention,
                         HLR=HNDLR),
        reply_markup=reply_markup,
        quote=True)


@Client.on_inline_query(~filters.user(AUTH))
async def _adndshow(client, query):
    out = [InlineQueryResultArticle(
        title="You are Not Authorised to Use Me !",
        description="User Restricted Bot",
        thumb_url=TLOGO,
        input_message_content=InputTextMessageContent(
            "You are Not Authorised to Use Me !"
        ),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                text=r"<\ Deploy Your Own />",
                url="https://github.com/New-dev0/TgTwitterBot")]]
        ))]
    await query.answer(results=out, switch_pm_text="TgTwitterBot",
                       switch_pm_parameter="start")

"""
@Client.on_inline_query(filters.user(AUTH))
async def myinline(client, query):
    if not len(query.query) == 0:
        return
    out = [InlineQueryResultArticle(
        title="TwitterBot",
        description="Help Menu",
        thumb_url=TLOGO,
        input_message_content=InputTextMessageContent(
            "Telegram - Twitter - Bot"),
        reply_markup=HELP_MARKUP)]
    await query.answer(out,
                       switch_pm_text="HELP Portal",
                       switch_pm_parameter="start")"""


HEMENU = f"""
**Available Commands**

`{HNDLR}tweet <reply to a message>`
- Post the Replied Message as Tweet on Twitter.
"""


@Client.on_message(filters.command("help", prefixes=HNDLR)
                   & filters.user(AUTH))
async def shelpmsg(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="INLINE HELP", callback_data="openmenu")]])
    await message.reply_text(HEMENU,
                             reply_markup=reply_markup,
                             quote=True)
