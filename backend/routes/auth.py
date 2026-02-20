from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection
from bson import ObjectId

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
async def register(user: User):
        result = users_collection.insert_one(user.dict())
            return {"id": str(result.inserted_id), **user.dict()}

            @router.post("/login")
            async def login(email: str, password: str):
                    user = users_collection.find_one({"email": email})
                        if user and user["password"] == password:
                                    user["_id"] = str(user["_id"])
                                            return User    raise HTTPException(status_code=401, detail="Invalid credentials")
