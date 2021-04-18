# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import AUTH, api
from twitterbot.funcs import tweeteazy


@Client.on_inline_query(filters.regex("^favorites$") & filters.user(AUTH))
async def showfav(client, query):
    favs = api.favorites()
    res = tweeteazy(favs)
    await query.answer(res[:50],
                       switch_pm_text="Showing Favorites !",
                       switch_pm_parameter="start")
