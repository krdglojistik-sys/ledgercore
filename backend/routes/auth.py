from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

router = APIRouter(prefix="/api/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("JWT_SECRET", "secret")
ALGORITHM = "HS256"

def create_access_token(data: dict):
      to_encode = data.copy()
      expire = datetime.utcnow() + timedelta(days=7)
      to_encode.update({"exp": expire})
      return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register")
async def register(user: User):
      # Email kontrol
      if users_collection.find_one({"email": user.email}):
                raise HTTPException(status_code=400, detail="Email already registered")

      # Şifre hashle
      hashed = pwd_context.hash(user.password)
      user_dict = user.dict()
      user_dict["password"] = hashed

    # Kaydet
      result = users_collection.insert_one(user_dict)
      user_dict["_id"] = str(result.inserted_id)

    # Token oluştur
      token = create_access_token({"sub": user_dict["_id"]})
      return {"token": token, "user": user_dict}

@router.post("/login")
async def login(email: str, password: str):
      user = users_collection.find_one({"email": email})
      if not user:
                raise HTTPException(status_code=401, detail="Invalid credentials")

      if not pwd_context.verify(password, user["password"]):
                raise HTTPException(status_code=401, detail="Invalid credentials")

      token = create_access_token({"sub": str(user["_id"])})
      return {"token": token, "user": {**user, "_id": str(user["_id"]), "password": None}}
