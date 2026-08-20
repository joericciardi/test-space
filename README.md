# Virtual Try-On MVP

This is a Minimum Viable Product (MVP) for a web-based application that creates a digital twin from user-uploaded images and allows users to virtually try on clothing items.

## Tech Stack
- **Frontend:** React, React Router DOM, Axios
- **Backend:** Python, FastAPI, Passlib, PyJWT, PyMongo (with MongoMock for tests)
- **Database:** MongoDB
- **Testing:** Pytest (backend), React Testing Library (frontend)

## Requirements
- Node.js & npm
- Python 3.12+
- A running MongoDB instance locally (default: `mongodb://localhost:27017/`). *(Note: you can skip this to just run tests which use `mongomock`)*

## Setup Instructions

### 1. Backend Setup
Navigate to the `backend` directory and set up a Python virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Backend API
Make sure you have a local MongoDB server running. Then, start the FastAPI server:
```bash
source venv/bin/activate
uvicorn backend.main:app --port 8000 --reload
```
The backend API will run on `http://localhost:8000`. On startup, it automatically seeds the database with the predefined catalog items (T-Shirts, Dress Shirts, Pants, Jeans).

### 3. Frontend Setup
Open a new terminal window, navigate to the `frontend` directory, and install the dependencies:
```bash
cd frontend
npm install
```

### 4. Run the Frontend App
Start the React development server:
```bash
npm start
```
The frontend application will be available at `http://localhost:3000`.

## Testing

### Backend Tests
To run the automated backend test suite (which mocks MongoDB using `mongomock` so a live server isn't required):
```bash
cd backend
source venv/bin/activate
PYTHONPATH=.. pytest tests/test_api.py
```

### Frontend Tests
To run the frontend rendering tests:
```bash
cd frontend
npm test
```
