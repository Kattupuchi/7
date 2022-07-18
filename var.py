from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", "8da8adb41f654ba374788eb88003c3c4")
    BOT_TOKEN = config("BOT_TOKEN", "5477433237:AAG3jSQ9yAY-seD8ZHUO8CdbcOea9gRQvOw")
    SUDO = list(map(int, getenv("SUDO", "5587651146").split()))
