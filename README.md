# 📘 AI-Doc — Intelligent Document Q&A & Summarizer (RAG-Based)

AI-Doc is a **Retrieval-Augmented Generation (RAG)** powered document assistant that allows you to **upload PDF or DOCX files**, ask natural language questions about them, and generate **AI-powered answers and summaries** using local LLMs.

The system combines **semantic search (FAISS + sentence embeddings)** with a **local Ollama LLM** to deliver fast, private, and context-aware responses — no cloud APIs required.

---

## 🚀 Features

* 📄 Upload & Parse **PDF and DOCX** documents
* 🧩 Automatic text chunking for large documents
* 🧠 Semantic search using **Sentence Transformers**
* ⚡ FAISS-powered vector similarity retrieval
* 🤖 Context-aware Q&A using **Ollama (LLaMA-based models)**
* 🧾 One-click **AI Document Summarization**
* 💻 Auto-detects **CPU / GPU** for embeddings
* 🔐 Fully **local & private** AI pipeline
* 🎛️ Clean and interactive **Streamlit UI**

---

## 🖥️ UI Preview

### 📄 Document Upload Interface

<img width="1919" height="377" alt="image" src="https://github.com/user-attachments/assets/0f4cff2d-9618-43e8-b5b8-846b34492536" />

<br/>

### 💬 Ask Questions About the Document

<img width="1919" height="896" alt="image" src="https://github.com/user-attachments/assets/15a56bd7-385b-451c-b25e-f1fa37171667" />


<br/>

### 🧾 AI-Generated Document Summary

<img width="419" height="891" alt="image" src="https://github.com/user-attachments/assets/58522f60-4a96-40ee-aa24-0d150be81449" />


<br/>

---

## 🧠 How It Works (High-Level)

1. 📥 User uploads a PDF or DOCX file
2. 📄 Text is extracted and split into chunks
3. 🧩 Chunks are converted into embeddings
4. 📦 FAISS stores vectors for fast retrieval
5. 🔍 User query retrieves top relevant chunks
6. 🤖 Ollama LLM generates an answer using context
7. 🧾 Optional full-document summarization

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-doc.git
cd ai-doc
```

### 2️⃣ Create & Activate Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

> **Note:** On macOS/Linux, use `source venv/bin/activate`

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install & Setup Ollama

* Download and install **Ollama**
* Pull a supported model (example):

```bash
ollama pull llama3.2:1b
```

> You can change the model name directly in `main.py`

### 5️⃣ Run the Application

```bash
streamlit run main.py
```

### 6️⃣ Open in Browser

The app will be available at:

```
http://localhost:8501
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — UI
* **Sentence-Transformers** — Embeddings
* **FAISS** — Vector Search
* **Ollama** — Local LLM Inference
* **PyMuPDF (fitz)** — PDF Parsing
* **python-docx** — DOCX Parsing
* **Torch** — Device acceleration

---

## 📌 Notes

* Designed for **local AI workflows**
* No external API keys required
* Best suited for **private documents**
* Scales well for long documents using RAG

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

🔥 Built with focus on **privacy, speed, and practical AI**
