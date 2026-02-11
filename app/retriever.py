# app/retriever.py
import faiss
import numpy as np
from typing import List, Tuple
from pathlib import Path
from .utils import load_pickle

class FaissRetriever:
    def __init__(self, index_path: str, store_path: str):
        # Check kar rahe hain ke FAISS index file exist karti hai ya nahi
        if not Path(index_path).exists():
            raise FileNotFoundError("FAISS index missing. Run scripts/ingest.py first.")
        
        # FAISS index load kar rahe hain (vector data)
        self.index = faiss.read_index(index_path)
        
        # Docstore (id → text) mapping load kar rahe hain
        self.docstore = load_pickle(store_path)  # {int_id: chunk_text}

    def search(self, query_emb: np.ndarray, k: int = 4) -> List[Tuple[str, float]]:
        """
        query_emb = question ka embedding vector
        k = kitne similar results chahiye
        """
        D, I = self.index.search(query_emb.reshape(1, -1), k)  # D = distance, I = ids
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx == -1:
                continue
            text = self.docstore.get(int(idx), "")
            results.append((text, float(dist)))  # (chunk_text, similarity_score)
        return results
