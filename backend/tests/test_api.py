import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.database import init_db

client = TestClient(app)

import mongomock
from backend.database import db

@pytest.fixture(autouse=True)
def setup_db():
    # Monkeypatch the database client for testing
    import backend.database
    backend.database.client = mongomock.MongoClient()
    backend.database.db = backend.database.client.virtual_try_on
    from backend.seed import seed_clothes
    seed_clothes()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Virtual Try-On API is running."}

def test_signup():
    response = client.post("/signup", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123",
        "mailing_preferences": True
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

    # Try duplicate email
    response_dup = client.post("/signup", json={
        "name": "Test User 2",
        "email": "test@example.com",
        "password": "password456"
    })
    assert response_dup.status_code == 400

def test_login():
    client.post("/signup", json={
        "name": "Test User",
        "email": "login_test@example.com",
        "password": "password123",
        "mailing_preferences": True
    })
    response = client.post("/login", json={
        "email": "login_test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_profile_update():
    client.post("/signup", json={
        "name": "Test User",
        "email": "profile@example.com",
        "password": "password123",
        "mailing_preferences": True
    })
    # Login to get token
    login_res = client.post("/login", json={
        "email": "profile@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]

    response = client.post("/profile", json={
        "chest": "40",
        "body_length": "29",
        "shoulder_width": "18.5",
        "sleeve_length": "34"
    }, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json() == {"message": "Profile updated successfully"}

def test_upload_photos(tmp_path):
    client.post("/signup", json={
        "name": "Test User",
        "email": "upload@example.com",
        "password": "password123",
        "mailing_preferences": True
    })
    # Login to get token
    login_res = client.post("/login", json={
        "email": "upload@example.com",
        "password": "password123"
    })
    token = login_res.json()["access_token"]

    # Create dummy files
    files = [
        ("files", ("photo1.jpg", b"image data 1", "image/jpeg")),
        ("files", ("photo2.jpg", b"image data 2", "image/jpeg")),
        ("files", ("photo3.jpg", b"image data 3", "image/jpeg")),
    ]

    response = client.post(
        "/upload_photos",
        files=files,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "paths" in response.json()

def test_catalog():
    response = client.get("/catalog")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    assert len(items) > 0  # Should be seeded on startup
