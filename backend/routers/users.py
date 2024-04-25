from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User with ID {user_id}"}

@router.post("/users/")
async def create_user(user: dict):
    if "username" not in user or "email" not in user:
        raise HTTPException(
            status_code=400, 
            detail="username and email are required"
        )

    return user