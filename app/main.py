# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import faiss, pickle, os, sys
from app.embeddings import LocalEmbedder
from app.gemini_helper import generate_answer
from app.db import collection

# ✅ Ensure base path is correct
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(title="RAG Chatbot", version="1.0")

# Allow local frontend dev servers to call this API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Load FAISS and docstore once (to avoid reloading every request)
INDEX_PATH = "store/faiss.index"
DOCSTORE_PATH = "store/docstore.pkl"

if not os.path.exists(INDEX_PATH) or not os.path.exists(DOCSTORE_PATH):
    raise RuntimeError("❌ FAISS index or docstore not found! Run indexing scripts first.")

index = faiss.read_index(INDEX_PATH)
with open(DOCSTORE_PATH, "rb") as f:
    docstore = pickle.load(f)

embedder = LocalEmbedder()

# ✅ Request schema
class ChatRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"ok": True, "message": "RAG Chatbot backend is running 🚀"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        question = req.question
        print(f"\n🧠 New question: {question}")

        # 1️⃣ Convert question → embedding
        query_vector = embedder.embed_text(question)

        import numpy as np
        if query_vector.ndim == 1:
            query_vector = np.array([query_vector], dtype="float32")
        else:
            query_vector = query_vector.astype("float32")

        # 2️⃣ Search FAISS for top-3 similar chunks
        distances, indices = index.search(query_vector, 3)
        sources = [docstore[i] for i in indices[0] if i in docstore]

        # 3️⃣ Generate answer from Gemini
        answer = generate_answer(sources, question)

        # 4️⃣ Save in MongoDB
        doc = {
            "user_message": question,
            "answer": answer,
            "sources": sources,
            "timestamp": __import__("datetime").datetime.utcnow()
        }
        collection.insert_one(doc)
        print("✅ Message stored in MongoDB.")

        # 5️⃣ Return response
        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
