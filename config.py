import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
MY_CHAT_ID = os.getenv('MY_CHAT_ID')
TG_BASE_URL = 'https://api.telegram.org/bot'
CAT_BASE_URL = 'https://cataas.com/cat?json=true'