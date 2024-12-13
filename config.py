import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20838202"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fde3e78e3256ae13e868b39088c83838")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vk0634912:OKMino2da3dSzlZB@cluster0.pdtg3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
