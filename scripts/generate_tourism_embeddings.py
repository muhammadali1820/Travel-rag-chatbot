# scripts/generate_tourism_embeddings.py

# Step 1️⃣ — Import necessary libraries
from app.embeddings import LocalEmbedder  # Your custom class for embeddings
import pickle  # To save the results for later use

# Step 2️⃣ — Read the chunks from the previous step
with open("data/tourism_text_chunks.txt", "r", encoding="utf-8") as file:
    chunks = file.read().split("---CHUNK-END---")  # Split text by chunk separator

# Clean and remove empty lines
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

print(f"📄 Total chunks to embed: {len(chunks)}")

# Step 3️⃣ — Initialize the embedder
embedder = LocalEmbedder()  # This uses sentence-transformers model (e.g. MiniLM)

# Step 4️⃣ — Generate embeddings for all chunks
print("⚙️ Generating embeddings, please wait...")
embeddings = embedder.embed_texts(chunks)

# Step 5️⃣ — Save embeddings for later use
with open("data/tourism_embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print(f"✅ Embeddings generated for {len(chunks)} chunks and saved to 'data/tourism_embeddings.pkl'")
