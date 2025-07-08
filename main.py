import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain_community.llms.ollama import Ollama

# Load and split PDFs
def load_and_split_pdfs(pdf_files):
    all_text = ""
    for uploaded_file in pdf_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        loader = PyPDFLoader(tmp_path)
        pages = loader.load()
        all_text += "\n".join([page.page_content for page in pages])
        os.remove(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    chunks = splitter.split_text(all_text)
    return chunks

# Create vector store
def create_vectorstore(chunks):
    documents = [Document(page_content=chunk) for chunk in chunks]
    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = Chroma.from_documents(documents, embedding=embeddings)
    return vectorstore

# Build QA system
def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 3})
    llm = Ollama(model="llama3")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa_chain

# Streamlit UI
st.set_page_config(page_title="PDF Chatbot 💬", layout="wide")
st.title("🤖 Chat with Your PDFs")

uploaded_pdfs = st.file_uploader("Upload one or more PDFs", type="pdf", accept_multiple_files=True)

if uploaded_pdfs:
    with st.spinner("Processing PDFs..."):
        chunks = load_and_split_pdfs(uploaded_pdfs)
        vectorstore = create_vectorstore(chunks)
        qa_chain = get_qa_chain(vectorstore)
    st.success("PDFs processed! Start asking questions.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask a question about your PDFs:", key="user_input")

    if user_input:
        with st.spinner("Thinking..."):
            result = qa_chain.invoke({"query": user_input})
            answer = result["result"]
            sources = result.get("source_documents", [])

            st.session_state.chat_history.append((user_input, answer, sources))

    # Display chat history
    for q, a, srcs in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
        if srcs:
            with st.expander("🔍 Sources"):
                for i, doc in enumerate(srcs):
                    st.markdown(f"**Chunk {i+1}:**\n{doc.page_content[:500]}...")
    st.title("🤖 Chat with Your PDFs")
    st.write("👋 App loaded successfully!")
    