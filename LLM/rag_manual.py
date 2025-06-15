from pathlib import Path

# Load markdown file
text = Path("data/Manual_cleaned.md").read_text(encoding="utf-8")

# Split by headings or sections (naive split)
chunks = [f"### {c.strip()}" for c in text.split("\n### ") if c.strip()]

from sentence_transformers import SentenceTransformer
import faiss

embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve_context(query, top_k=3):
    query_vec = embedder.encode([query])
    D, I = index.search(query_vec, top_k)
    return [chunks[i] for i in I[0]]

context = retrieve_context("se usan pronombres?")

print(context)