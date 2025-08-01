import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
PORT = os.environ.get("PORT", "8022")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "luffybot")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Anime_Community_India</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", """<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀɴɪᴍᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪɴᴅɪᴀ. ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ</b>""")
HELP = os.environ.get("HELP_MESSAGE", "🙏🏻")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by luffy @Luffy_Babu </blockquote>"
ABOUT_TXT = """<b><blockquote expandable>›› ᴏᴡɴᴇʀ: <a href='https://t.me/Luffy_Babu'>𝖫ᴜғғʏ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/NothingCopyright'>ᴀᴋᴀsʜ</a></b></blockquote>"""
CHANNELS_TXT = """<b><blockquote expandable>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Community_Indi>
›› ᴀɴɪᴍᴇ ᴍᴏᴠɪᴇ: <a href='https://t.me/+zdzoF1YaqeViZTJl'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴀʟʟ ᴀɴɪᴍᴇ: <a href='https://t.me/All_Anime_Hindi_India'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴀɴɪᴍᴇ ɢʀᴏᴜᴘ: <a href='https://t.me/Anime_Community_India_Chats'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b></blockquote>"""
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"
# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002256510517")) # Channel where user links >
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7932127170 8110231942").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(7932127170)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
