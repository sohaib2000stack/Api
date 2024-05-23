from fastapi import APIRouter

# Create a new router
router = APIRouter()

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(num1: int, num2: int) -> int:
    if num1 == 0 or num2 == 0:
        return 0
    return abs(num1 * num2) // gcd(num1, num2)

@router.get("/lcm/{num1}/{num2}")
async def calculate_lcm(num1: int, num2: int):
    result = lcm(num1, num2)
    return {"result": result}