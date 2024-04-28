from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, skaneled, root

# Create an instance of the FastAPI class
app = FastAPI()

app.include_router(root.router)
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

