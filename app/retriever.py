import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from config import *

model = SentenceTransformer(EMBEDDING_MODEL)

index = faiss.read_index(VECTOR_DB_PATH)

with open("data/vector_store/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

def search(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=TOP_K)
    return [chunks[i] for i in I[0]]