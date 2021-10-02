from fastapi import FastAPI

from fastapi.middleware.gzip import GZipMiddleware


import app.config as app_config
from app.config import default_route_str

from app.router import router as main_router



app = FastAPI(title="Sample Python Backend", version="0")

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(main_router, prefix=app_config.default_route_str)


@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts
    """
    print(f"Starting App")


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown
    """
    print("Closing App")
