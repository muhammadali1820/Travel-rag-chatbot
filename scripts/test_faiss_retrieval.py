# scripts/test_faiss_retrieval.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import faiss
import pickle
from app.embeddings import LocalEmbedder

# ✅ Load FAISS index and docstore
index = faiss.read_index("store/faiss.index")

with open("store/docstore.pkl", "rb") as f:
    docstore = pickle.load(f)

print(f"📚 Loaded FAISS index with {index.ntotal} vectors.")
print(f"🧾 Loaded docstore with {len(docstore)} chunks.")

# ✅ Initialize embedder
embedder = LocalEmbedder()

# ✅ Ask a sample question
question = "What are the travel guidelines for tourists visiting Pakistan?"
print(f"\n🧠 Query: {question}")

import numpy as np

# Convert question to embedding
query_embedding = embedder.embed_text(question)

# 🧩 Fix FAISS shape issue — FAISS expects 2D array (n, d)
if query_embedding.ndim == 1:
    query_embedding = np.array([query_embedding], dtype="float32")
else:
    query_embedding = query_embedding.astype("float32")

# ✅ Search FAISS index for top 3 similar chunks
top_k = 3
distances, indices = index.search(query_embedding, top_k)

print(f"\n🔍 Top {top_k} most relevant chunks retrieved:\n")

for i, idx in enumerate(indices[0]):
    if idx == -1:
        continue
    print(f"⭐ Result {i+1} (Distance: {distances[0][i]:.2f})")
    print(docstore.get(idx, "❌ No text found"))
    print("-" * 80)
