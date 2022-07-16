from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "9531120" default=6, cast=int)
    API_HASH = config("API_HASH", "8da8adb41f654ba374788eb88003c3c4")
    BOT_TOKEN = config("BOT_TOKEN", "5581135260:AAFuQsBYVrMhe12x--x19OXn5nXQHk0oyKE")
    SUDO = list(map(int, getenv("SUDO", "5599715194").split()))
