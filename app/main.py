"""
    Main script of AI Service Template.

    This script setups the API server using FastAPI.

"""

from fastapi import FastAPI
from app.routers import register_routers
from contextlib import asynccontextmanager
from loguru import logger

from app.version import VERSION


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("starting up the app...".upper())
    yield
    logger.debug("shutting down gracefully...".upper())


app = FastAPI(lifespan=lifespan, title="FastAPI AI Service Template", version=VERSION)

register_routers(app)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI AI Service Template"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
