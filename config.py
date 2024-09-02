import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 28394860
API_HASH = "07b4fad3981e64c0554add6f249f7c07"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7261208882:AAFVXE5Rih3RwTkcNHK1yzidJhadacBwjjU"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://combinado:combinado@cluster0.2a7qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUSIC_BOT_NAME = "COMBINADO MUSIC"
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002246269016
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002246269016"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = 672466909

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandrdXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/combinadomusic")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/combinadomusic")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = "GO FUCK"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/40d2a2e7e036ca734419f.png"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/adc241f65e920429b824f.png"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/14eb59ea7d31229d8d751.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4310ea5f523520b2b765b.jpg"
TELEGRAM_AUDIO_URL = getenv("IMAGEM_AQUI", None)
TELEGRAM_VIDEO_URL = getenv("IMAGEM_AQUI", None)
STREAM_IMG_URL = getenv("IMAGEM_AQUI", None)
SOUNCLOUD_IMG_URL = getenv("IMAGEM_AQUI", None)
YOUTUBE_IMG_URL = getenv("IMAGEM_AQUI", None)
SPOTIFY_ARTIST_IMG_URL = getenv("IMAGEM_AQUI", None)
SPOTIFY_ALBUM_IMG_URL = getenv("IMAGEM_AQUI", None)
SPOTIFY_PLAYLIST_IMG_URL = getenv("IMAGEM_AQUI", None)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
