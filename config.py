LOG_FILE_NAME   = "bot.log"
PORT            = int(os.environ.get("PORT", 5010))
OWNER_ID        = int(os.environ.get("OWNER_ID", 6728678197))
MSG_EFFECT      = 5046509860389126442

SHORT_URL       = os.environ.get("SHORT_URL", "linkshortify.com")
SHORT_API       = os.environ.get("SHORT_API", "")
SHORT_TUT       = os.environ.get("SHORT_TUT", "https://t.me/KENSHIN_ANIME_CHAT/8524")

SESSION         = os.environ.get("SESSION_NAME", "kenshin_primary")
TOKEN           = os.environ.get("BOT_TOKEN", "8285265972:AAGJ9sp52xcN2bBROyF-PuEWNLKOvGVfrow")
API_ID          = int(os.environ.get("API_ID", 37407868))
API_HASH        = os.environ.get("API_HASH", "d7d3bff9f7cf9f3b111129bdbd13a065")
WORKERS         = 5

DB_URI          = os.environ.get("MONGO_URI", "mongodb+srv://kenshinxu4:iammohitgurjar.1@kenshinfileshere.bhlhhjn.mongodb.net/?appName=Kenshinfileshere")
DB_NAME         = os.environ.get("DB_NAME", "Kenshinfileshere")

# ⚠️ IMPORTANT: Put your DB channel ID here
DB_CHANNEL      = int(os.environ.get("DB_CHANNEL","-1003854811216" ))

FSUBS           = [
    [int(os.environ.get("FSUB_CHANNEL", "-1002645612322")), True, 1]
]

AUTO_DEL        = int(os.environ.get("AUTO_DEL", 600))
ADMINS          = [OWNER_ID]
DISABLE_BTN     = False
PROTECT         = False

MESSAGES = {
    "START": (
        "<b>✨ ʏōᴋᴏsᴏ, {first} ♡\n\n"
        "<blockquote>𓆩 I'm Kenshin Anime File Shere 𓆪 — your personal File provider"
        " for 🌸 KENSHIN ANIME 🌸\n\nTap on the link provided to get your file 🤍</blockquote>\n\n"
        "‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/KENSHIN_ANIME_OWNER'>KENSHIN ANIME</a></b>"
    ),
    "FSUB": (
        "<b><blockquote>» ʜᴇʏ {first} ×,</blockquote>\n\n"
        "ʏᴏᴜʀ ꜰɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ"
        " ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ..!</b>"
    ),
    "ABOUT": (
        "<b>𓆩 Kenshin File shere 𓆪\n\n"
        "<blockquote expandable>"
        "‣ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/KENSHIN_ANIME'>🌸 KENSHIN ANIME 🌸</a>\n"
        "‣ ᴏᴡɴᴇʀ: <a href='https://t.me/KENSHIN_ANIME_OWNER'>KENSHIN ANIME</a>\n"
        "‣ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>\n"
        "‣ ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>\n"
        "‣ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>"
        "</blockquote></b>"
    ),
    "REPLY":     "<b>🌸 ꜰᴏʀ ᴍᴏʀᴇ ᴀɴɪᴍᴇ ᴊᴏɪɴ — <a href='https://t.me/KENSHIN_ANIME'>KENSHIN ANIME</a></b>",
    "SHORT_MSG": (
        "<b>📊 ʜᴇʏ {first},\n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇs ɪɴ ᴀ sɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n"
        "⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪs ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>"
    ),
    "START_PHOTO": "https://i.ibb.co/7d40j3xx/x.jpg",
    "FSUB_PHOTO":  "https://i.ibb.co/pSQSKxV/x.jpg",
    "SHORT_PIC":   "https://i.ibb.co/vC17k1rY/x.jpg",
    "SHORT":       "https://i.ibb.co/67whTdy5/x.jpg",
}
