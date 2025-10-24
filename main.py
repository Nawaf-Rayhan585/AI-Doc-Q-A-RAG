import os
import faiss
import numpy as np
import fitz
import docx
import streamlit as st
from tqdm import tqdm
import subprocess
from sentence_transformers import SentenceTransformer

# ---------------- CPU-SAFE EMBEDDINGS ----------------
# Use a tiny model that works on CPU only
embed_model = SentenceTransformer("paraphrase-MiniLM-L3-v2")  # <--- fully CPU compatible

# ---------------- OLLAMA LLM FUNCTION ----------------
def run_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:1b"],
            input=prompt,
            capture_output=True,
            text=True  # ensures string input/output
        )
        if result.returncode != 0:
            return f"Ollama error: {result.stderr}"
        return result.stdout.strip()
    except Exception as e:
        return f"Error running Ollama: {e}"

# ---------------- TEXT EXTRACTION ----------------
def extract_text(file_path):
    text = ""
    if file_path.endswith('.pdf'):
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

# ---------------- CHUNKING ----------------
def chunk_text(text, chunk_size=1000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# ---------------- VECTOR STORE ----------------
def create_vector_store(chunks):
    embeddings = []
    for chunk in tqdm(chunks, desc="Embedding chunks"):
        emb = embed_model.encode(chunk)
        embeddings.append(emb)
    embeddings = np.array(embeddings, dtype='float32')
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, chunks

# ---------------- RETRIEVAL ----------------
def retrieve(query, index, chunks, top_k=3):
    query_emb = embed_model.encode(query)
    query_emb = np.array([query_emb], dtype='float32')
    D, I = index.search(query_emb, top_k)
    return [chunks[i] for i in I[0]]

# ---------------- ANSWERING ----------------
def generate_answer(context_chunks, query):
    context = "\n".join(context_chunks)
    prompt = f"""You are a helpful AI assistant.
Answer the question based only on the context below.

Context:
{context}

Question: {query}
Answer:"""
    return run_ollama(prompt)

# ---------------- SUMMARIZATION ----------------
def summarize_document(text):
    short_text = text[:12000]
    prompt = f"""Summarize the following document into clear bullet points and main highlights:

{short_text}

Return a professional summary."""
    return run_ollama(prompt)

# ---------------- STREAMLIT UI ----------------
st.title("📘 AI Document Q&A (CPU-safe Ollama + MiniLM)")

uploaded_file = st.file_uploader("📄 Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file is not None:
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Extracting text... ⏳")
    text = extract_text(file_path)
    chunks = chunk_text(text)

    st.info("Creating vector index... ⚙️")
    index, chunks = create_vector_store(chunks)

    query = st.text_input("💬 Ask a question about the document:")
    if query:
        relevant_chunks = retrieve(query, index, chunks)
        st.info("Generating answer using Ollama LLaMA 1B... ⚡")
        answer = generate_answer(relevant_chunks, query)
        st.success(answer)

    if st.button("🧾 Summarize Document"):
        st.info("Generating summary using Ollama... 🧠")
        summary = summarize_document(text)
        st.subheader("📋 Document Summary:")
        st.write(summary)
