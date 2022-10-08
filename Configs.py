from decouple import config
from dotenv import load_dotenv

load_dotenv()


class Var:
    API_ID = config("API_ID", default=6)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN", None)
    CONSUMER_KEY = config("CONSUMER_KEY", None)
    CONSUMER_SECRET = config("CONSUMER_SECRET", None)
    ACCESS_TOKEN = config("ACCESS_TOKEN", None)
    ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET", None)
    AUTHUSERS = config("AUTHUSERS", None)
    HNDLR = config("HNDLR", "/")
