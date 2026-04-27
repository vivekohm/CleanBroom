from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle
from config import *

model = SentenceTransformer(EMBEDDING_MODEL)

def load_pdf(file):
    reader = PdfReader(file)
    return " ".join([page.extract_text() or "" for page in reader.pages])

def chunk_text(text):
    words = text.split()
    return [" ".join(words[i:i+CHUNK_SIZE]) for i in range(0, len(words), CHUNK_SIZE)]

def create_index(chunks):
    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, embeddings

def save_index(index, chunks):
    os.makedirs("data/vector_store", exist_ok=True)

    faiss.write_index(index, VECTOR_DB_PATH)

    with open("data/vector_store/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)