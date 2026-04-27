import os
from app.ingest import load_pdf, chunk_text, create_index, save_index

DATA_PATH = "data/raw/"

all_chunks = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        file_path = os.path.join(DATA_PATH, file)
        print(f"Processing: {file}")

        text = load_pdf(file_path)
        chunks = chunk_text(text)

        all_chunks.extend(chunks)

index, _ = create_index(all_chunks)
save_index(index, all_chunks)

print("All documents indexed successfully")