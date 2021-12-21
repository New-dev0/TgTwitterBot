# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import AUTH, api
from twitterbot.funcs import user_eazy, tweeteazy


@Client.on_inline_query(filters.regex("^search") & filters.user(AUTH))
async def searchthing(client, query):
    try:
        match = query.query.split(maxsplit=1)[1]
    except IndexError:
        return await query.answer(
            [], switch_pm_text="Enter Query to Search", switch_pm_parameter="start"
        )
    outex = api.search_tweets(q=match)
    results = tweeteazy(outex)
    await query.answer(
        results,
        is_personal=True,
        switch_pm_text=f"Showing {len(results)} Results",
        switch_pm_parameter="start",
    )


@Client.on_inline_query(filters.regex("^user") & filters.user(AUTH))
async def searchuser(client, query):
    try:
        match = query.query.split(maxsplit=1)[1]
    except IndexError:
        return await query.answer(
            [], switch_pm_text="Enter Query to Search", switch_pm_parameter="start"
        )
    user = api.search_users(q=match)
    results = user_eazy(user)
    await query.answer(
        results,
        is_personal=True,
        switch_pm_text=f"Showing {len(results)} Result !",
        switch_pm_parameter="start",
    )
