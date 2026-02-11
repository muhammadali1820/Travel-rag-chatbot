# scripts/add_tourism_to_faiss.py

# ✅ Step 1 — Ensure we can import app/ modules
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ Step 2 — Imports
import faiss
import pickle
from app.utils import save_pickle, load_pickle

# ✅ Step 3 — Load the embeddings we created
with open("data/tourism_embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

print(f"📦 Loaded {len(embeddings)} embeddings from file.")

# ✅ Step 4 — Create or load FAISS index
store_path = "store/faiss.index"
if not os.path.exists("store"):
    os.makedirs("store")

try:
    index = faiss.read_index(store_path)
    print("📁 Existing FAISS index found — appending new data...")
except:
    print("🆕 No existing FAISS index found — creating new one...")
    # Create a new FAISS index based on the embedding dimension
    index = faiss.IndexFlatL2(embeddings[0].shape[0])

# ✅ Step 5 — Add the embeddings to the index
index.add(embeddings)
print(f"✅ Added {len(embeddings)} vectors to the FAISS index.")

# ✅ Step 6 — Save updated FAISS index
faiss.write_index(index, store_path)
print("💾 FAISS index saved successfully!")

# ✅ Step 7 — Save a docstore (to map each vector → original text)
chunks_path = "data/tourism_text_chunks.txt"
with open(chunks_path, "r", encoding="utf-8") as f:
    chunks = f.read().split("---CHUNK-END---")

chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

docstore_path = "store/docstore.pkl"
try:
    docstore = load_pickle(docstore_path)
except:
    docstore = {}

start_id = len(docstore)
for i, chunk in enumerate(chunks):
    docstore[start_id + i] = chunk

save_pickle(docstore, docstore_path)
print(f"🧾 Docstore updated with {len(chunks)} chunks.")
print("🎉 All done! Your FAISS index and docstore are ready.")
