from fastapi import APIRouter

extra_router = APIRouter()

@extra_router.get("/extra")
async def extra():
    return {"message": "Extra route from v1"}
