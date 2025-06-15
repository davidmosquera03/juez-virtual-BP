
from langchain_core.documents import Document
import json
import os 
os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
with open("data/motions.json",encoding="utf-8") as f:
    data = json.load(f)

docs = [
    Document(
        page_content=f"Motion: {item['motion']}\nInfo Slide: {item['info_slide']}",
        metadata={}
    )
    for item in data
]

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Gemini embed model
db = FAISS.from_documents(docs, embedding)

retriever = db.as_retriever()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

from langchain.chains import RetrievalQA

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

query = "mociones sobre estados unidos o USA o terminos similares"
response = rag_chain.invoke({"query": query})
print(response["result"])
print(response["source_documents"])