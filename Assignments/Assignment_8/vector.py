import os
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings


df = pd.read_csv("C:\\Users\\YASH\\Desktop\\CSI\\Assignments\\Assignment_8\\Training Dataset.csv")

docs = [
    Document(
        page_content=f"Loan ID {row['Loan_ID']} requested by a {row['Gender']} {row['Married']} applicant "
                     f"with income {row['ApplicantIncome']}, loan status {row['Loan_Status']}, "
                     f"credit history {row['Credit_History']}."
    )
    for _, row in df.iterrows()
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

vectordb = FAISS.from_documents(docs, embedding=embeddings)
vectordb.save_local("faiss_index")

print("FAISS vector database created and saved.")
