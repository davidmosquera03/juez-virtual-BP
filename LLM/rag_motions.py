import json
import faiss
from groq import Groq

from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()

# CONFIG

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

TOP_K = 5

# LOAD JSON

with open("data/motions_spanish.json", encoding="utf-8") as f:
    data = json.load(f)

# CREATE TEXT DOCUMENTS

docs = [
    f"Motion: {item['motion']}\nInfo Slide: {item['info_slide']}"
    for item in data
]

print(f"Documents: {len(docs)}")

# EMBEDDINGS

embedder = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedder.encode(docs)

# FAISS INDEX

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# USER QUERY

query = input("Pregunta:")

# RETRIEVE

query_embedding = embedder.encode([query])

distances, indices = index.search(query_embedding, TOP_K)

retrieved_docs = [docs[i] for i in indices[0]]

context = "\n\n".join(retrieved_docs)

# PROMPT

prompt = f"""
Eres un experto en debate BP.

Usa el contexto para responder la pregunta.

CONTEXTO:
{context}

PREGUNTA:
{query}
"""

# GENERATE WITH GROQ

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.5,
)


# OUTPUT

print("\n===== ANSWER =====\n")
print(response.choices[0].message.content)

print("\n===== SOURCE DOCUMENTS =====\n")

for i, doc in enumerate(retrieved_docs, 1):
    print(f"\n--- Document {i} ---")
    print(doc)