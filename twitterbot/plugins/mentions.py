# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from twitterbot import AUTH, api
from twitterbot.funcs import tweeteazy


@Client.on_inline_query(filters.regex("^mentions$") & filters.user(AUTH))
async def showmentions(client, query):
    mentions = api.mentions_timeline()
    results = tweeteazy(mentions)
    await query.answer(
        results,
        is_personal=True,
        switch_pm_text=f"Got {len(results)} Mentions",
        switch_pm_parameter="start",
    )
