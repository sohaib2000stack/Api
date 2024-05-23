from fastapi import FastAPI
from api.v1 import main_router, extra_router, arithmetic_router, add_numbers,  subtract_numbers, divide_numbers, multiply_numbers, calculate_lcm
from fastapi.middleware.cors import CORSMiddleware
# The line `from api.arithmetic_operations import router as arithmetic_router` is importing a router
# object from a module named `arithmetic_operations` within the `api` package. It is then assigning
# this imported router object to a variable named `arithmetic_router`. This allows the router defined
# in the `arithmetic_operations` module to be included in the FastAPI application by using
# `app.include_router(arithmetic_router)` or similar method.
# from api.arithmetic_operations import router as arithmetic_router
app = FastAPI()

app.include_router(main_router)
app.include_router(extra_router)
app.include_router(arithmetic_router, prefix="/api")
app.include_router(calculate_lcm)
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    import uvicorn
    from main import app

    uvicorn.run(app, host="0.0.0.0", port=8000)
