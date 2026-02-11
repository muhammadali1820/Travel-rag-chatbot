# scripts/ingest.py
from pathlib import Path
import faiss
from app.embeddings import LocalEmbedder
from app.utils import split_text, save_pickle

# File paths define kar rahe hain
DATA_PATH = "data/rag_source.txt"
INDEX_PATH = "store/faiss.index"
DOCSTORE_PATH = "store/docstore.pkl"

def main():
    # Step 1: File read karna
    text = Path(DATA_PATH).read_text(encoding="utf-8")
    print("📖 Data file loaded successfully!")

    # Step 2: Text ko chunks me todna
    chunks = split_text(text, chunk_size=600, chunk_overlap=100)
    print(f"✅ Total chunks created: {len(chunks)}")

    # Step 3: Chunks ke embeddings banana
    embedder = LocalEmbedder()
    embs = embedder.embed_texts(chunks)  # (N, d) float32
    print("🔢 Embeddings created successfully!")

    # Step 4: FAISS index banana
    d = embs.shape[1]  # vector dimension
    index = faiss.IndexFlatIP(d)  # cosine similarity (inner product)
    index.add(embs)
    print("💾 FAISS index created and vectors added!")

    # Step 5: Store folder banana (agar nahi hai)
    Path("store").mkdir(parents=True, exist_ok=True)

    # Step 6: Index aur docstore save karna
    faiss.write_index(index, INDEX_PATH)
    save_pickle({i: c for i, c in enumerate(chunks)}, DOCSTORE_PATH)
    print("🎉 Done! Index and docstore saved in 'store/' folder")

if __name__ == "__main__":
    if not Path(DATA_PATH).exists():
        raise FileNotFoundError("❌ Data file not found. Make sure 'data/rag_source.txt' exists.")
    main()
