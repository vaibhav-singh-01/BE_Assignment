from app.core.providers import PROVIDERS
from app.core.config import settings

class CryptoService:
    def __init__(self, provider_name: str = "coingecko"):
        self.provider = PROVIDERS[provider_name]()

    def get_price(self, crypto_id: str) -> float:
        return self.provider.get_price(crypto_id)

    def pin_crypto(self, crypto_id: str):
        if crypto_id not in settings.PINNED_CRYPTOS:
            settings.PINNED_CRYPTOS.append(crypto_id)

    def unpin_crypto(self, crypto_id: str):
        if crypto_id in settings.PINNED_CRYPTOS:
            settings.PINNED_CRYPTOS.remove(crypto_id)

    def get_pinned_cryptos(self):
        return [
            {"crypto_id": crypto_id, "price": self.get_price(crypto_id)}
            for crypto_id in settings.PINNED_CRYPTOS
        ]