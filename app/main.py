from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.core.config import settings
from app.core.logging import log
from app.middleware.logging import log_middleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Add middleware
app.middleware("http")(log_middleware)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Crypto Tracker API"}


@app.on_event("startup")
async def startup_event():
    log.info("Starting Crypto Tracker API")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down Crypto Tracker API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}