from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:user@usersdb.jza2h.mongodb.net/?retryWrites=true&w=majority&appName=UsersDB")
client = AsyncIOMotorClient(MONGO_URI)
db = client.notification_service  # Database name

def get_db():
    return db
