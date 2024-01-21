"""
    Main script of AI Service Template.

    This script setups the API server using FastAPI.

"""

from fastapi import FastAPI
from app.routers import register_routers
from contextlib import asynccontextmanager
from loguru import logger
import gradio as gr

from app.version import __version__
from app.interface import gr_interface


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("starting up the app...".upper())
    yield
    logger.debug("shutting down gracefully...".upper())


app = FastAPI(lifespan=lifespan, title="FastAPI AI Service Template", version=__version__)
app = gr.mount_gradio_app(app, gr_interface, path="/ui")

register_routers(app)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI AI Service Template"}


def run_service():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run_service()
