import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from app.cache.cache import get_cached, set_cache

import time


model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_chunks(query, top_k=3):
    start = time.time()
    cached = get_cached(query)
    if cached:
        return cached

    conn = sqlite3.connect("vector_db/embeddings.db")
    cursor = conn.cursor()

    cursor.execute("SELECT text, embedding, source FROM documents")
    rows = cursor.fetchall()

    query_emb = model.encode(query)

    scored = []
    for text, emb_blob, source in rows:
        emb = np.frombuffer(emb_blob, dtype=np.float32)
        score = cosine_similarity(query_emb, emb)
        scored.append((text, source, score))

    scored.sort(key=lambda x: x[2], reverse=True)

    result = [{"text": t, "source": s} for t, s, _ in scored[:top_k]]

    set_cache(query, result)
    print(f"⏱ Retrieval time: {time.time() - start:.3f}s")
    return result