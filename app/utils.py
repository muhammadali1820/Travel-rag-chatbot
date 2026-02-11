# app/utils.py
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle
from pathlib import Path

# Yeh function bada text ko chhoti chhoti chunks me todta hai
def split_text(text: str, chunk_size: int = 600, chunk_overlap: int = 100) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

# Yeh function kisi bhi Python object ko pickle file me save karta hai
def save_pickle(obj, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)

# Yeh function saved pickle file ko wapas load karta hai
def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)
