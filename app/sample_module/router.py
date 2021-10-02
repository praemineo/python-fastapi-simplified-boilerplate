from fastapi import APIRouter
# from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/")
async def home():
    return "Hello World"