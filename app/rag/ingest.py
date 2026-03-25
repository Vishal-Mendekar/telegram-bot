import os
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
DB_PATH = "vector_db/embeddings.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE documents (
        id INTEGER PRIMARY KEY,
        text TEXT,
        embedding BLOB,
        source TEXT
    )
    """)

    conn.commit()
    conn.close()


def chunk_text(text, chunk_size=100):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]


def ingest():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for file in os.listdir("data/docs"):
        with open(f"data/docs/{file}", "r") as f:
            text = f.read()

        chunks = chunk_text(text)

        for chunk in chunks:
            emb = model.encode(chunk).astype(np.float32)
            cursor.execute(
                "INSERT INTO documents (text, embedding, source) VALUES (?, ?, ?)",
                (chunk, emb.tobytes(), file)
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    os.makedirs("vector_db", exist_ok=True)
    create_db()
    ingest()
    print("Ingestion complete")