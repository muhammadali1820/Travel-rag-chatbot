# app/embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

class LocalEmbedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        # Pretrained model load kar rahe hain
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        """
        Ye function multiple text chunks ko embeddings me convert karta hai
        """
        embs = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return np.array(embs, dtype="float32")

    def embed_text(self, text):
        """
        Ye ek single text ka embedding return karta hai
        """
        return self.embed_texts([text])[0]
