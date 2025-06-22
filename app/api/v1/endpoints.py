from fastapi import APIRouter, HTTPException
from app.services.crypto import CryptoService
from app.api.v1.models import (
    CryptoPriceResponse,
    PinCryptoRequest,
    PinnedCryptoResponse
)

router = APIRouter()
crypto_service = CryptoService()

@router.get("/price/{crypto_id}", response_model=CryptoPriceResponse)
async def get_crypto_price(crypto_id: str):
    try:
        price = crypto_service.get_price(crypto_id.lower())
        return {"crypto_id": crypto_id, "price": price}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/pin", response_model=PinnedCryptoResponse)
async def pin_crypto(request: PinCryptoRequest):
    try:
        crypto_id = request.crypto_id.lower()
        price = crypto_service.get_price(crypto_id)
        crypto_service.pin_crypto(crypto_id)
        return {"crypto_id": crypto_id, "price": price}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/unpin/{crypto_id}")
async def unpin_crypto(crypto_id: str):
    try:
        crypto_service.unpin_crypto(crypto_id.lower())
        return {"message": f"{crypto_id} unpinned successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pinned", response_model=list[PinnedCryptoResponse])
async def get_pinned_cryptos():
    try:
        return crypto_service.get_pinned_cryptos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))