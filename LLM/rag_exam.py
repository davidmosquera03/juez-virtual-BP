# Using Rag on Debate Manual, tries to pass an Exam
import os
import faiss
from groq import Groq

from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# CONFIG

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

MANUAL_PATH = "data/Manual_cleaned.md"
QUESTION_PATH = "data/tdu_examen.md"

CHUNK_SIZE = 1200
TOP_K = 5

# LOAD FILE

with open(MANUAL_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# SIMPLE CHUNKING

chunks = []

for i in range(0, len(text), CHUNK_SIZE):
    chunk = text[i:i + CHUNK_SIZE]
    chunks.append(chunk)

print(f"Chunks: {len(chunks)}")


# EMBEDDINGS

embedder = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedder.encode(chunks)

# FAISS INDEX

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# LOAD QUESTION

with open(QUESTION_PATH, "r", encoding="utf-8") as f:
    question = f.read()


# RETRIEVE

question_embedding = embedder.encode([question])

distances, indices = index.search(question_embedding, TOP_K)

retrieved_chunks = [chunks[i] for i in indices[0]]

context = "\n\n".join(retrieved_chunks)


# PROMPT

prompt = f"""
Eres un juez experto en debate BP.

Usa SOLAMENTE el contexto proporcionado para responder.

CONTEXTO:
{context}

PREGUNTA:
{question}
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

print("\n===== ANSWER =====\n")
print(response.choices[0].message.content)