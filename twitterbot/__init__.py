# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tweepy
from Configs import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton as Button


AUTH = list(set(int(a) for a in Var.AUTHUSERS.split(" ")))
HNDLR = Var.HNDLR

auth = tweepy.OAuthHandler(Var.CONSUMER_KEY, Var.CONSUMER_SECRET)
auth.set_access_token(Var.ACCESS_TOKEN, Var.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

TLOGO = "https://telegra.ph/file/845054582c76963620311.jpg"

HELP_MARKUP = InlineKeyboardMarkup(
    [[Button(text="Home Tweets",
             switch_inline_query_current_chat="home")],
     [Button(text="Favorites",
             switch_inline_query_current_chat="favorites")],
     [Button(text="Mentions",
             switch_inline_query_current_chat="mentions")],
     [Button(text="Search Tweets",
             switch_inline_query_current_chat="search quote")],
     [Button(text="Search User",
             switch_inline_query_current_chat="user NewDev0")]])
