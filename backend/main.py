from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.root import router as root_router
from routers import users, skaneled


# Create an instance of the FastAPI class
app = FastAPI()

# Include root router only!
app.include_router(root_router)
app.include_router(users.router)
app.include_router(skaneled.router)

# TODO: Define allowed origins
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

