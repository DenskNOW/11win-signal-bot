import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
CHANNEL_ID = os.getenv("CHANNEL_ID")
POSTBACK_SECRET = os.getenv("POSTBACK_SECRET")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
DB_URL = os.getenv("DB_URL")
LANGUAGES = ["ru", "en", "es", "hi", "br", "az", "pt", "tr", "ar"]