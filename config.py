import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20838202"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fde3e78e3256ae13e868b39088c83838")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5387859888"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vk0634912:OKMino2da3dSzlZB@cluster0.pdtg3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
