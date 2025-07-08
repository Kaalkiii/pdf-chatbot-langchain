# pdf-chatbot-langchain
Chat with your PDFs locally using LangChain, Chroma, and Ollama — no API key required. Built with Streamlit.
📄 README.md
markdown
Copy
Edit
# 🤖 PDF Chatbot with LangChain + Ollama + Streamlit

A local, privacy-friendly AI chatbot that lets you **ask questions about one or more PDF files** using LLMs running **fully offline via Ollama**.

---

## 🚀 Features

- 📄 Upload multiple PDFs
- 🔎 Ask questions in plain English
- 🧠 Uses local embeddings + Chroma vector DB
- 🔗 Powered by LangChain, Ollama, and Streamlit
- 🔍 Shows chunks used for every answer
- 💻 100% runs on your machine (no API keys!)

---

## 📸 Demo Screenshot

*(Optional: Add a screenshot here if you want)*

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install and run Ollama
Download Ollama from: https://ollama.com

Then pull the model:

bash
Copy
Edit
ollama run llama3
4. Run the app
bash
Copy
Edit
streamlit run app.py
📁 Folder Structure
graphql
Copy
Edit
pdf-chatbot/
├── app.py                # Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── sample.pdf            # (Optional) Example PDF to test
🧠 How It Works
Loads your PDFs and extracts text using PyPDFLoader

Splits text into overlapping chunks using RecursiveCharacterTextSplitter

Converts chunks to embeddings using OllamaEmbeddings

Stores them in a local Chroma vector store

Uses RetrievalQA to:

Retrieve relevant chunks

Query a local LLM (llama3 via Ollama)

Return accurate answers with source context

🔧 Built With
LangChain

Ollama

Streamlit

Chroma

🙌 Contribute
Pull requests are welcome! Fork it, improve it, and submit a PR.
Feel free to open issues or suggest new features.

🛡️ License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Would you also like:
- A `Dockerfile` for deployment?
- A `streamlit_app.py` for public Streamlit Cloud hosting?
- A GitHub project banner/image?

Let me know — I’ll generate it for you.
