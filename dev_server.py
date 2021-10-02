import uvicorn

from app import config

if __name__ == "__main__":
    uvicorn.run("app.main:app", log_level="debug", port=config.port, reload=True)