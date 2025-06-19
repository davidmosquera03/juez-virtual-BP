from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter

import os
os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
# Load file
loader = TextLoader("data/Manual_cleaned.md", encoding="utf-8")
raw_docs = loader.load()

# Split using markdown headers
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")])
docs = splitter.split_text(raw_docs[0].page_content)

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
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

query = "Diferencia entre alternativas y contra modelo"
response = rag_chain.invoke({"query": query})
print(response["result"])
print(response["source_documents"])