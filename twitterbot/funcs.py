# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)


def mkease(counts, cstatus):
    text = str(counts)
    if cstatus:
        text += " ❣"
    else:
        text += " ♡"
    return text


def simstuff(user):
    uname = user["screen_name"]
    text = "#User #Twitterbot\n\n"
    text += "**⫸ Details\nName** -> " + user["name"]
    text += f"\n**Username** -> [@{uname}](https://twitter.com/{uname})\n\n"
    if user["description"]:
        text += f"**Description** -> \n`{user['description']}`"
    return text


def tweeteazy(bunch):
    results = []
    for one in bunch:
        ct = one._json
        uname = ct["user"]["screen_name"]
        cm = f"By [@{uname}](https://twitter.com/{uname})"
        ds = "#Tweet"
        ds += "\n\n" + ct["text"] + "\n" + cm
        reply_markup = status_reply_markup(one)
        results.append(
            InlineQueryResultArticle(
                title=ct["text"],
                description=f"@{uname}",
                thumb_url=ct["user"]["profile_image_url"],
                reply_markup=InlineKeyboardMarkup(reply_markup),
                input_message_content=InputTextMessageContent(
                    ds, disable_web_page_preview=True
                ),
            )
        )
    return results[:50]


def user_eazy(bunch):
    result = []
    for one in bunch:
        user = one._json
        text = simstuff(user)
        uname = user["screen_name"]
        reply_markup = InlineKeyboardMarkup(user_reply_markup(one))
        result.append(
            InlineQueryResultArticle(
                title=user["name"],
                description=f"@{uname}",
                url="https://twitter.com/" + uname,
                thumb_url=user["profile_image_url"],
                reply_markup=reply_markup,
                input_message_content=InputTextMessageContent(
                    text, disable_web_page_preview=True
                ),
            )
        )
    return result[:50]


def status_reply_markup(status):
    OUT = []
    status = status._json
    user = status["user"]
    is_fav = "ulk"
    favbutn = mkease(status["favorite_count"], status["favorited"])
    if status["favorited"]:
        is_fav = "lk"
    rt_ = "urt"
    rt_btn = "Undo Re-Tweet"
    if not status["retweeted"]:
        rt_ = "rt"
        rt_btn = "Re-Tweet"
    Link = "https://twitter.com/" + user["screen_name"]
    Link += "/status/" + str(status["id"])
    COL_1 = [
        InlineKeyboardButton("View", url=Link),
        InlineKeyboardButton("User", callback_data=f"user{user['id']}"),
    ]
    OUT.append(COL_1)
    OUT.append(
        [InlineKeyboardButton(favbutn, callback_data=f"favr_{is_fav}_{status['id']}")]
    )
    OUT.append(
        [InlineKeyboardButton(rt_btn, callback_data=f"rtt_{rt_}_{status['id']}")]
    )
    return OUT


def user_reply_markup(user):
    OUT = []
    user = user._json
    fl = "ufl"
    fl_but = "Follow"
    if user["following"]:
        fl = "fl"
        fl_but = "UnFollow"
    Link = "https://twitter.com/" + user["screen_name"]
    OUT.append(
        [
            InlineKeyboardButton("View", url=Link),
            InlineKeyboardButton(fl_but, callback_data=f"fuflow_{fl}_{user['id']}"),
        ]
    )
    OUT.append([InlineKeyboardButton(text="Help Menu", callback_data="openmenu")])
    return OUT
