from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", "8da8adb41f654ba374788eb88003c3c4")
    BOT_TOKEN = config("BOT_TOKEN", "5234005906:AAFutd-Kx3L1_Os5C0125oO1Btp5AiPPth8")
    SUDO = list(map(int, getenv("SUDO", "5587651146").split()))
