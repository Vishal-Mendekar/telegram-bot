from app.rag.retriever import retrieve_chunks
from app.llm.client import generate_answer


def rag_pipeline(query, history=None):
    chunks = retrieve_chunks(query)

    context = "\n\n".join([c["text"] for c in chunks])
    sources = list(set([c["source"] for c in chunks]))

    history_text = ""
    if history:
        history_text = "\n".join([f"Q: {q}\nA: {a}" for q, a in history])

    prompt = f"""
You are a helpful assistant.

Previous conversation:
{history_text}

Context:
{context}

Question:
{query}

Answer:
"""

    answer = generate_answer(prompt)

    return f"{answer}\n\nSources:\n" + "\n".join(sources)