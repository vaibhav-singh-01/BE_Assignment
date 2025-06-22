from pydantic import BaseModel

class CryptoPriceResponse(BaseModel):
    crypto_id: str
    price: float
    currency: str = "USD"

class PinCryptoRequest(BaseModel):
    crypto_id: str

class PinnedCryptoResponse(BaseModel):
    crypto_id: str
    price: float
    currency: str = "USD"