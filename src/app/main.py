"""
    Main script of AI Service Template.

    This script setups the API server using FastAPI.

"""

import os
from fastapi import FastAPI
from app.routers import register_routers
from contextlib import asynccontextmanager
from loguru import logger
import gradio as gr

from app.version import __version__
from app.interface import gr_interface
from app.utils.eureka import register_service, unregister_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.debug("starting up the app...".upper())
    await register_service()

    yield
    
    print("shutting down gracefully...".upper())
    await unregister_service()


app = FastAPI(
    lifespan=lifespan, 
    title="FastAPI AI Service Template", 
    version=__version__,
    root_path=os.environ.get("FASTAPI_ROOT_PATH", "/api/v1/ai-service-template"),
    docs_url=os.environ.get("FASTAPI_DOCS_URL", "/public/ai-service-template/swagger.html"),
    openapi_url=os.environ.get("FASTAPI_OPENAPI_URL", "/public/ai-service-template/api-docs"),
)

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
