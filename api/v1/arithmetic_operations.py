from fastapi import APIRouter

arithmetic_router = APIRouter()

@arithmetic_router.get("/add")
async def add_numbers(x: float, y: float):
    return {"result": x + y}

@arithmetic_router.get("/subtract")
async def subtract_numbers(x: float, y: float):
    return {"result": x - y}

@arithmetic_router.get("/multiply")
async def multiply_numbers(x: float, y: float):
    return {"result": x * y}

@arithmetic_router.get("/divide")
async def divide_numbers(x: float, y: float):
    if y == 0:
        return {"error": "Division by zero"}
    return {"result": x / y}
