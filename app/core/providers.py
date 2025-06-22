from abc import ABC, abstractmethod
from app.core.config import settings
import requests

class CryptoProvider(ABC):
    @abstractmethod
    def get_price(self, crypto_id: str) -> float:
        pass

class CoinGeckoProvider(CryptoProvider):
    def get_price(self, crypto_id: str) -> float:
        url = f"{settings.COINGECKO_API_URL}/simple/price"
        params = {
            "ids": crypto_id,
            "vs_currencies": "usd",
            "x_cg_demo_api_key": settings.COINGECKO_API_KEY
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data[crypto_id]["usd"]
        except Exception as e:
            raise ValueError(f"Error fetching price: {str(e)}")

# Add new providers here
PROVIDERS = {
    "coingecko": CoinGeckoProvider
}