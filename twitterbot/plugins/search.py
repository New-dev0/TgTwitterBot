# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import AUTH, api
from twitterbot.funcs import user_eazy, tweeteazy


@Client.on_inline_query(filters.regex("^search (.*)") & filters.user(AUTH))
async def searchthing(client, query):
    match = query.matches[0].group(1)
    outex = api.search(match)
    results = tweeteazy(outex)
    await query.answer(results,
                       switch_pm_text=f"Showing {len(results)} Results",
                       switch_pm_parameter="start")


@Client.on_inline_query(filters.regex("^user (.*)") & filters.user(AUTH))
async def searchuser(client, query):
    match = query.matches[0].group(1)
    user = api.search_users(match)
    results = user_eazy(user)
    await query.answer(results,
                       switch_pm_text=f"Showing {len(results)} Result !",
                       switch_pm_parameter="start")
