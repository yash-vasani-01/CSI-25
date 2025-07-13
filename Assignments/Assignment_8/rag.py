
import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain.chains import ConversationalRetrievalChain


def load_vector_db():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.environ["GOOGLE_API_KEY"]
    )
    return FAISS.load_local(
        "faiss_index",
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

def create_chat_chain():
    vectordb = load_vector_db()
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash-latest",
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.3
    )
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=False
    )
