import os
import re
import logging
from logging.handlers import RotatingFileHandler

# Environment Variables
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "0") or 0)
API_HASH = os.environ.get("API_HASH", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "0") or 0)
PORT = os.environ.get("PORT", "8022")

DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "link")

# Auto approve
id_pattern = re.compile(r"^-?\d+$")  # Add regex pattern for ID validation
CHAT_ID = [
    int(app_chat_id) if id_pattern.match(app_chat_id) else app_chat_id
    for app_chat_id in os.environ.get('CHAT_ID', '').split()
]
TEXT = os.environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))

# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴀɴɪᴍᴇ, ᴍᴏᴠɪᴇs ᴀɴᴅ ᴍᴏʀᴇ!</b>")
HELP = os.environ.get("HELP_MESSAGE", "🙏🏻")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by</blockquote></b>")
ABOUT_TXT = """<b><blockquote expandable>›› ᴏᴡɴᴇʀ: <a href='https://t.me/Luffy_Babu'>𝖫ᴜғғʏ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/NothingCopyright'>ᴀᴋᴀsʜ</a></b></blockquote>"""
CHANNELS_TXT = """<b><blockquote expandable>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Community_Indi'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇ: <a href='https://t.me/+zdzoF1YaqeViZTJl'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴀʟʟ ᴀɴɪᴍᴇ: <a href='https://t.me/All_Anime_Hindi_India'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴀɴɪᴍᴇ ɢʀᴏᴜᴘ: <a href='https://t.me/Anime_Community_India_Chats'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b></blockquote>"""

# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002256510517"))

try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "7932127170").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
if 7932127170 not in ADMINS:
    ADMINS.append(7932127170)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
