from fastapi import APIRouter
from fastapi.responses import Response


from app.sample_module import router as sample_module_router


router = APIRouter()

@router.get("/")
async def default():
    """Default page
    """
    return Response("Simplied Boilerplate Default Page")


router.include_router(sample_module_router.router,
                      prefix="/sample")
