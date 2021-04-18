# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent
)


def mkease(counts, cstatus):
    text = str(counts)
    if cstatus:
        text += " ❤️"
    else:
        text += " ♡"
    return text


def simstuff(user, link):
    text = "#User #Twitterbot\n\n"
    text += "**⫸ Details\nName** -> " + user["name"]
    text += f"\n**Username** -> [@{user['screen_name']}]({link})\n\n"
    if user["description"]:
        text += f"**Description** -> \n`{user['description']}`"
    return text


def tweeteazy(bunch):
    results = []
    for one in bunch:
        ct = one._json
        uname = ct["user"]["screen_name"]
        cm = f"By [@{uname}](https://twitter.com/{uname})"
        ds = "#Tweet\n\n" + ct["text"]
        ds += "\n" + cm
        user = ct["user"]["id"]
        # at = ct["extended_entities"]
        # if (at and at["media"]):
        #    light = at["media"][0]["media_url_https"]
        #    ds += f"\n\n**Media Link** - [Click Here]({light})"
        link = f"https://twitter.com/{uname}/status/{ct['id']}"
        btext = mkease(ct["favorite_count"], ct["favorited"])
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="View", url=link),
             InlineKeyboardButton(text="User", callback_data=f"user{user}")],
            [InlineKeyboardButton(text=btext, callback_data=f"favr{ct['id']}")]
            ])
        results.append(InlineQueryResultArticle(
            title=ct["text"],
            description=cm,
            thumb_url=ct["user"]["profile_image_url"],
            reply_markup=reply_markup,
            input_message_content=InputTextMessageContent(
                ds,
                disable_web_page_preview=True)))
    return results[:50]


def user_eazy(bunch):
    result = []
    for one in bunch:
        user = one._json
        link = f"https://twitter.com/{user['screen_name']}"
        text = simstuff(user, link)
        udt = "Follow"
        if user["following"]:
            udt = "UnFollow"
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="View", url=link),
             InlineKeyboardButton(
                 text=udt, callback_data=f"fuflow{user['id']}")],
            [InlineKeyboardButton(text="Help Menu",
                                  callback_data="openmenu")]])
        result.append(InlineQueryResultArticle(
            title=user["name"],
            description=user["screen_name"],
            url=link,
            thumb_url=user["profile_image_url"],
            reply_markup=reply_markup,
            input_message_content=InputTextMessageContent(
                text, disable_web_page_preview=True)))
    return result[:50]
