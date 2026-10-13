import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API credentials — get these from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Telegram bot token — get this from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")

# MongoDB connection URI
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# OneGrab API configuration
YTPROXY_URL = getenv(
    "YTPROXY_URL",
    "https://api.onegrab.fun"
).rstrip("/")

YT_API_KEY = getenv("YT_API_KEY", None)

# Duration limit in minutes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Logging group chat ID
LOGGER_ID = int(getenv("LOGGER_ID"))

# Owner's Telegram user ID
OWNER_ID = int(getenv("OWNER_ID"))

# Heroku configuration
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Upstream repository configuration
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/xbitcode/music.git"
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support links
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/ffzvcu"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/youandme_public_hai0"
)

# Assistant auto-leaving configuration
AUTO_LEAVING_ASSISTANT = (
    getenv("AUTO_LEAVING_ASSISTANT", "True").lower()
    in ("true", "1", "yes")
)

ASSISTANT_LEAVE_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 5400)
)

# Spotify API credentials
SPOTIFY_CLIENT_ID = getenv(
    "SPOTIFY_CLIENT_ID",
    "1c21247d714244ddbb09925dac565aed"
)

SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET",
    "709e1a2969664491b58200860623ef19"
)

# Maximum tracks fetched per playlist
PLAYLIST_FETCH_LIMIT = int(
    getenv("PLAYLIST_FETCH_LIMIT", 25)
)

# Telegram file-size limits (bytes)
TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600)
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824)
)

# Private bot mode
PRIVATE_BOT_MODE_MEM = int(
    getenv("PRIVATE_BOT_MODE_MEM", 1)
)

# Pyrogram session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Internal bot data
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
file_cache: dict[str, float] = {}

# Images
START_IMG_URL = [
    "https://te.legra.ph/file/5fd13f2cc0d03bce9f7f2.jpg",
    "https://te.legra.ph/file/c15d01b3e6b40ea141dc9.jpg",
    "https://te.legra.ph/file/5fd13f2cc0d03bce9f7f2.jpg"
]

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/87f680aead03443f291b0.jpg"
)

PLAYLIST_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
STATS_IMG_URL = "https://telegra.ph/file/edd388a42dd2c499fd868.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
STREAM_IMG_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"


# Convert time in HH:MM:SS or MM:SS format to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:360")
)


# Validate support URLs
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL URL is wrong. "
            "Ensure it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT URL is wrong. "
            "Ensure it starts with https://"
        )
