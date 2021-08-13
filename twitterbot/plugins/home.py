# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import AUTH, api
from twitterbot.funcs import tweeteazy


@Client.on_inline_query(filters.regex("^home$") & filters.user(AUTH))
async def homeline(client, query):
    tweets = api.home_timeline()
    res = tweeteazy(tweets)
    await query.answer(results=res,
                       switch_pm_text="Home",
                       switch_pm_parameter="start")

