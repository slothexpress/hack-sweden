import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router
#from database import connect_to_db

# Create an instance of the FastAPI class
app = FastAPI()

# Include routers
app.include_router(users_router)

# Define allowed origins
allowed_origins = [
    "http://localhost:3000",
    "http://example.com",
]

# Allow CORS and requests from defined origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

test = {"id": "12", "name": "bagarsmurfen"}

# Root endpoint
@app.get("/")
def read_root():
    return test

# Run the FastAPI application using Uvicorn
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost", port=8000)