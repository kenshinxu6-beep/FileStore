import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 6728678197

MSG_EFFECT = 5046509860389126442

SHORT_URL = "linkshortify.com"
SHORT_API = ""
SHORT_TUT = "https://t.me/KENSHIN_ANIME_CHAT/8524"

# Bot Configuration
SESSION = "kenshin_primary"
TOKEN = "8285265972:AAFJGq2UZbwQ-0py2XLFawXQLwA0Kbp5kCs"
API_ID = 37407868
API_HASH = "d7d3bff9f7cf9f3b111129bdbd13a065"
WORKERS = 5

DB_URI = "mongodb+srv://kenshinxu4:iammohitgurjar.1@kenshinfileshere.bhlhhjn.mongodb.net/?appName=Kenshinfileshere"
DB_NAME = "Kenshinfileshere"

FSUBS = [[-1002645612322, True, 01]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL =    # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 600
# Admin IDs
ADMINS = [6728678197]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>✨ ʏōᴋᴏsᴏ, {first} ♡\n\n<blockquote>𓆩 I'm Kenshin Anime File Shere 𓆪 — your personal File provider for 🌸 KENSHIN ANIME 🌸\n\nTap on the link provided to get your file 🤍</blockquote>\n\n‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/KENSHIN_ANIME_OWNER'>KENSHIN ANIME</a></b>",

    "FSUB": "<b><blockquote>» ʜᴇʏ {first} ×,</blockquote>\n\nʏᴏᴜʀ ꜰɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ..!</b>",

    "ABOUT": "<b>𓆩 Kenshin File shere 𓆪\n\n<blockquote expandable>‣ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/KENSHIN_ANIME'>🌸 KENSHIN ANIME 🌸</a>\n‣ ᴏᴡɴᴇʀ: <a href='https://t.me/KENSHIN_ANIME_OWNER'>KENSHIN ANIME</a>\n‣ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>\n‣ ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>\n‣ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a></blockquote></b>",

    "REPLY": "<b>🌸 ꜰᴏʀ ᴍᴏʀᴇ ᴀɴɪᴍᴇ ᴊᴏɪɴ — <a href='https://t.me/KENSHIN_ANIME'>KENSHIN ANIME</a></b>",

    "SHORT_MSG": "<b>📊 ʜᴇʏ {first},\n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇs ɪɴ ᴀ sɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪs ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",

    "START_PHOTO": "https://i.ibb.co/7d40j3xx/x.jpg",
    "FSUB_PHOTO": "https://i.ibb.co/pSQSKxV/x.jpg",
    "SHORT_PIC": "https://i.ibb.co/vC17k1rY/x.jpg",
    "SHORT": "https://i.ibb.co/67whTdy5/x.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
