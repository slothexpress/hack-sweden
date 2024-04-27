import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.root import router as root_router


# Create an instance of the FastAPI class
app = FastAPI()

# Include routers
app.include_router(root_router)

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

#### TEST DATA STUFF HERE #####


# Run the FastAPI application using Uvicorn
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost", port=8000)
    