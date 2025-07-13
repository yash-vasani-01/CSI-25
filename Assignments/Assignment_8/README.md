
# 📊 Loan Eligibility RAG Chatbot

A **Streamlit-based Retrieval-Augmented Generation (RAG) chatbot** using Google Gemini (`models/gemini-1.5-flash-latest`) and LangChain. It helps answer questions about loan eligibility based on a custom dataset.

---

## 📁 Project Structure

```
loan_rag_chatbot/
├── Training Dataset.csv           
├── vector.py                
├── rag.py                
├── app.py                        
├── faiss_index/                   
└── README.md                      
```

---

## 🚀 Features

- ✅ Google **models/gemini-1.5-pro-latest** LLM for intelligent Q&A
- ✅ FAISS Vector DB for **fast semantic search**
- ✅ **Conversational memory** (multi-turn chat history)
- ✅ Clean **Streamlit UI**
- ✅ Custom dataset support (`Training Dataset.csv`)

---

## 🔧 Installation

### 1. Clone this project:

```bash
git clone https://github.com/yash-vasani-01/CSI-25/tree/master/Assignments/Assignment_8
cd Assignment_8
```

### 2. Create virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   

pip install -r requirements.txt
```

### 3. Set your Google Gemini API Key:

```bash
export GOOGLE_API_KEY=your-api-key   
```

---

## 📥 Create Vector Index

Run once to build the FAISS vector store from `Training Dataset.csv`:

```bash
python create_index.py
```

---

## 💬 Run Chatbot

Then launch the chatbot UI:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🧠 Tech Stack

- **LangChain** – Framework for RAG & chains
- **Google Generative AI** – `models/gemini-1.5-flash-latest` & `embedding-001`
- **FAISS** – Local vector store
- **Streamlit** – Chatbot front-end

---

## ✨ Example Questions

Try asking:

- `"Tell me about loan ID LP001002"`
- `"How does income affect approval?"`
- `"What is the credit history pattern?"`

---

## 📌 Notes

- This app uses `allow_dangerous_deserialization=True` to load your local FAISS index.
- Responses depend on your dataset's richness.

---

## 👤 Author

Made by [Yash Vasani]