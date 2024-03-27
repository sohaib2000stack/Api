from fastapi import APIRouter

main_router = APIRouter()

@main_router.get("/")
async def main():
    return {"message": "Hello from v1"}
