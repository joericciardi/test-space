from pymongo import MongoClient

client = None
db = None

def init_db():
    global client, db
    # Use real MongoDB client; for MVP we'll default to localhost. Can be overridden by env variable later.
    client = MongoClient("mongodb://localhost:27017/")
    db = client.virtual_try_on

    if "users" not in db.list_collection_names():
        db.create_collection("users")
    if "clothes" not in db.list_collection_names():
        db.create_collection("clothes")

def get_db():
    return db
