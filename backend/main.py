from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException, Depends, UploadFile, File, Form
from fastapi.security import OAuth2PasswordBearer
from typing import List
import os
import shutil
import jwt
from .database import init_db, get_db
from .auth import get_password_hash, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from .models import UserCreate, UserLogin, Token, ProfileUpdate
from .seed import seed_clothes

app = FastAPI(title="Virtual Try-On MVP")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return email
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()
    seed_clothes()

@app.get("/")
def read_root():
    return {"message": "Virtual Try-On API is running."}

@app.get("/catalog")
def get_catalog():
    db = get_db()
    items = list(db.clothes.find({}, {"_id": 0}))
    return items

@app.post("/signup", response_model=Token)
def signup(user: UserCreate):
    db = get_db()
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    user_dict = user.model_dump()
    user_dict["password"] = hashed_password

    # insert user
    result = db.users.insert_one(user_dict)

    # generate token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/profile")
def update_profile(profile: ProfileUpdate, current_user: str = Depends(get_current_user)):
    db = get_db()
    result = db.users.update_one(
        {"email": current_user},
        {"$set": {
            "chest": profile.chest,
            "body_length": profile.body_length,
            "shoulder_width": profile.shoulder_width,
            "sleeve_length": profile.sleeve_length
        }}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Profile updated successfully"}

@app.post("/upload_photos")
def upload_photos(files: List[UploadFile] = File(...), current_user: str = Depends(get_current_user)):
    if len(files) < 3 or len(files) > 5:
        raise HTTPException(status_code=400, detail="Must upload between 3 and 5 photos")

    file_paths = []
    upload_dir = "backend/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    for file in files:
        import re
        safe_filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', file.filename)
        safe_filename = safe_filename.lstrip('.')
        file_location = os.path.join(upload_dir, f"{current_user}_{safe_filename}")
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_location)

    db = get_db()
    db.users.update_one(
        {"email": current_user},
        {"$set": {"photos": file_paths}}
    )

    return {"message": "Photos uploaded successfully", "paths": file_paths}

@app.post("/login", response_model=Token)
def login(user: UserLogin):
    db = get_db()
    db_user = db.users.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
