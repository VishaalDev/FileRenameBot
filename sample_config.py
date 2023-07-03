import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6022881684:AAFqDjt6iFNDTzPdhKaE8bBr92qH9xpDy9I")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 6357458))
    API_HASH = os.environ.get("API_HASH", "0a8a7fc9c3be210a33f07ba73d225123")
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001658172006")
    # log channel
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001860957419")
    # Get these values from my.telegram.org
    CHAT_ID = os.environ.get("CHAT_ID", "1130052935")
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1130052935").split())
    # Banned Unwanted Members..
    BANNED_USERS = []
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://graph.org/file/40b0f2ffb2b00df9d34f8.jpg/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "182.74.243.47:3128")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mgvishaal:vishaal@cluster0.hergr.mongodb.net/?retryWrites=true&w=majority")
    
