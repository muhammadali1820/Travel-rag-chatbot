# app/db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import time

# .env load karte hain
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB", "rag_chatbot")
COLL_NAME = os.getenv("MONGODB_COLLECTION", "messages")

# MongoClient banana
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLL_NAME]

def save_message(user_message: str, answer: str = None, sources: list = None):
    """
    Ye function ek message document MongoDB me insert karta hai
    """
    record = {
        "user_message": user_message,
        "answer": answer,
        "sources": sources or [],
        "timestamp": int(time.time() * 1000)
    }
    collection.insert_one(record)
    print("✅ Message stored in MongoDB.")
