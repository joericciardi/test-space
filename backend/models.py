from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mailing_preferences: Optional[bool] = False

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class ProfileUpdate(BaseModel):
    chest: str
    body_length: str
    shoulder_width: str
    sleeve_length: str
