import uvicorn

from app import main, config

if __name__ == "__main__":
    uvicorn.run(main.app, log_level="info", port=config.port, reload=False)