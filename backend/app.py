import sys
from fastapi import FastAPI
from routers.users import router as users_router

# Create an instance of the FastAPI class
app = FastAPI()

# Include routers
app.include_router(users_router)

test = {"id": "1234", "name": "bagarsmurfen"}

# Root endpoint
@app.get("/")
def read_root():
    return test

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)