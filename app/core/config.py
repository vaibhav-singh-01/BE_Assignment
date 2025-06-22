import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Crypto Tracker API"
    API_V1_STR: str = "/api/v1"
    COINGECKO_API_URL: str = "https://api.coingecko.com/api/v3"
    COINGECKO_API_KEY: str = os.getenv("COINGECKO_API_KEY", "")
    PINNED_CRYPTOS: list = []

settings = Settings()