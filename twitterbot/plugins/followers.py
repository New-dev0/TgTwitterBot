# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import api, AUTH
from twitterbot.funcs import user_eazy


@Client.on_inline_query(filters.regex("^followers$") & filters.user(AUTH))
async def getfollowers(client, query):
    flowers = api.followers()
    results = user_eazy(flowers)
    num = len(results)
    tet = f"Showing {num} Results !"
    if num == 0:
        tet = "Sad, You Dont have Any Follower."
    await query.answer(results,
                       switch_pm_text=tet,
                       switch_pm_parameter="start")
