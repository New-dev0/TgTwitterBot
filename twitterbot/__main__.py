# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from Configs import Var
from pyrogram import Client, idle

import logging
logging.basicConfig(level=logging.WARNING)

Client = Client("TgTwitterBot",
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=Var.BOT_TOKEN,
                plugins=dict(
                    root="twitterbot/plugins"
                    )
                )

Client.start()

Client = Client.get_me()
print(f"@{Client.username} Deployed Successfully!")
print("Your Tg-Twitter-Bot is Alive 🎉")

idle()
