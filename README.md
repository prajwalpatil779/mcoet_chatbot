# MCOET Chatbot 🤖

A conversational AI chatbot for Malla Reddy College of Engineering & Technology (MCOET) that answers student queries using data scraped from the college website and uploaded documents. Powered by **Ollama** (local LLM) and **Chroma** vector database.

## Features ✨

- 🌐 **Web Scraping**: Automatically extracts info from MCOET website (40+ pages)
- 📚 **Document Integration**: Supports PDFs, DOCX files, and images (with OCR)
- 🔍 **Vector Search**: Semantic similarity search using HuggingFace embeddings
- 🤖 **Local LLM**: Uses Mistral 7B model via Ollama (no API costs)
- 💻 **User-Friendly UI**: Built with Streamlit
- 📊 **RAG Architecture**: Retrieval-Augmented Generation for accurate answers

## Project Structure

```
mcoet_chatbot/
├── chatbot.py                    # Streamlit app (main interface)
├── build_database.py             # Build vector database from documents
├── scrape_website.py             # Scrape MCOET website data
├── test_ollama.py                # Test Ollama connectivity
├── test_db.py                    # Test database retrieval
├── requirements.txt              # Python dependencies
├── college_data.json             # Scraped website content (40 pages)
├── college_pdfs/                 # User-uploaded documents
│   ├── 4. OOAD Syllabus.docx
│   ├── INSTITUTE POLICY*.pdf
│   ├── p.pdf
│   ├── p(5).pdf
│   ├── r.pdf
│   └── doc 1.jpeg
├── college_db/                   # Chroma vector database (210 chunks)
└── README.md                     # This file
```

## Prerequisites

- **Windows/Mac/Linux** with Python 3.8+
- **Ollama** installed (free local AI runtime)
- **4GB+ RAM** recommended
- **Internet** (for initial model download)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/prajwalpatil779/mcoet_chatbot.git
cd mcoet_chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama

**Windows:**
- Download from: https://ollama.ai/download
- Run the installer and follow setup
- Ollama will auto-start as a service

**Mac:**
```bash
brew install ollama
ollama serve  # Start in background
```

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
ollama serve  # Start in background
```

### 5. Download Mistral Model
```bash
ollama pull mistral
```
*First run takes ~5 minutes (4.4GB download)*

## Quick Start

### Option A: Full Setup (Scrape + Build Database)

```bash
# 1. Scrape MCOET website (40 pages)
python scrape_website.py

# 2. Build vector database with website data + documents
python build_database.py

# 3. Start chatbot
streamlit run chatbot.py
```

The app will open at **http://localhost:8501**

### Option B: Quick Start (Already Have Database)

```bash
python -m streamlit run chatbot.py
```

## How It Works

### Architecture
```
User Query
    ↓
Chatbot UI (Streamlit)
    ↓
Vector Search (Chroma DB)
    ↓
Retrieve Top 5 Documents
    ↓
Ollama LLM (Generate Response)
    ↓
Display Answer
```

### Workflow
1. **Scraping**: `scrape_website.py` extracts text from 40 MCOET web pages
2. **Documents**: Upload PDFs/DOCX to `college_pdfs/` folder
3. **Indexing**: `build_database.py` splits docs into chunks & creates vector embeddings
4. **Search**: User query is converted to embeddings and compared with database
5. **Generation**: Top 5 matching documents sent as context to Ollama LLM
6. **Response**: Model generates answer based on retrieved context

## Usage

### Launch Chatbot
```bash
streamlit run chatbot.py
```

### Ask Questions
- Type any question about MCOET
- Examples:
  - "What courses does MCOET offer?"
  - "What is the placement process?"
  - "Tell me about OOAD syllabus"
  - "What is the attendance policy?"

### Add New Documents
1. Place PDF, DOCX, or image files in `college_pdfs/` folder
2. Run `python build_database.py` to rebuild the database
3. Restart the chatbot

### Rebuild Database
```bash
python build_database.py
```
*Takes 3-5 minutes (loads embedding model on first run)*

## Configuration

### Ollama Settings
- **Model**: Mistral 7B (4.4GB)
- **API Endpoint**: `http://localhost:11434`
- **Timeout**: 180 seconds (for slow first responses)

### Database Settings
- **Chunk Size**: 600 characters
- **Chunk Overlap**: 60 characters
- **Embedding Model**: all-MiniLM-L6-v2 (HuggingFace)
- **Vector DB**: Chroma (persisted to `./college_db`)

### Streamlit Settings
Edit `~/.streamlit/config.toml` for UI customization

## Troubleshooting

### Issue: "Connection refused - Ollama not running"
**Solution:**
```bash
# Windows
Start-Process -FilePath "C:\Users\YourUsername\AppData\Local\Programs\Ollama\ollama.exe" -ArgumentList "serve"

# Mac/Linux
ollama serve
```

### Issue: "No module named 'pytesseract'"
**Solution:** OCR is optional. Images will be skipped if Tesseract isn't installed.
- To enable: Install Tesseract-OCR from: https://github.com/UB-Mannheim/tesseract/wiki

### Issue: "Timeout waiting for response"
**Solution:** First query with Mistral takes time. Wait 30-60 seconds for initial response.

### Issue: "Database locked error during rebuild"
**Solution:** Close Streamlit app before running `build_database.py`:
```bash
taskkill /IM python.exe /F  # Windows
```

### Issue: "CUDA/GPU not detected"
**Solution:** CPU mode is fine. Mistral runs well on modern CPUs (2GB RAM during inference).

## Dependencies

```
Core:
- streamlit          # Web UI
- langchain          # RAG framework
- langchain-community # LangChain extensions
- chromadb           # Vector database
- sentence-transformers # Embeddings model

Document Processing:
- pypdf              # PDF parsing
- python-docx        # DOCX parsing
- Pillow             # Image support
- pytesseract        # OCR (optional)

Web Scraping:
- beautifulsoup4     # HTML parsing
- requests           # HTTP requests
```

See `requirements.txt` for full dependency list.

## File Descriptions

| File | Purpose |
|------|---------|
| `chatbot.py` | Main Streamlit application - user interface for asking questions |
| `build_database.py` | Creates/updates Chroma vector database from documents |
| `scrape_website.py` | Scrapes MCOET website and saves to `college_data.json` |
| `test_ollama.py` | Tests Ollama API connectivity |
| `test_db.py` | Tests vector database retrieval |
| `college_data.json` | Extracted text from 40 MCOET web pages |
| `college_pdfs/` | Folder for user-uploaded documents |
| `college_db/` | Chroma vector database (persisted) |

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4GB | 8GB+ |
| Storage | 6GB | 10GB+ |
| CPU | 2-core | 4-core+ |
| GPU | Optional | RTX/A series for speed |
| Python | 3.8 | 3.10+ |

## Performance

- **First Query**: 30-60 seconds (model warm-up)
- **Subsequent Queries**: 5-15 seconds
- **Database Search**: <100ms
- **Model Inference**: 4-10 seconds (mistral 7B on CPU)

## Future Enhancements

- [ ] Web UI upload for PDFs (without server restart)
- [ ] Add Claude/LLaMA model options
- [ ] Conversation history & follow-up questions
- [ ] Multi-language support
- [ ] Deploy to cloud (HuggingFace Spaces, Streamlit Cloud)
- [ ] Admin dashboard for content management
- [ ] Feedback mechanism for answer quality

## Deployment

### Deploy to Streamlit Cloud
```bash
git push
# Go to https://share.streamlit.io → Connect GitHub repo
```

### Deploy to HuggingFace Spaces
```bash
git clone https://huggingface.co/spaces/your-username/mcoet-chatbot
# Copy files, push to HF
```

### Docker Deployment
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "chatbot.py"]
```

## License

This project is open source. Modify and share freely.

## Contributors

- **Developer**: GitHub [prajwalpatil779](https://github.com/prajwalpatil779)

## Support

- 📧 For issues: Open an issue on GitHub
- 💬 For questions: Check troubleshooting section above

---

**Last Updated**: February 2026  
**Status**: Production Ready ✅  
**Ollama Model**: Mistral 7B  
**Database Size**: 210 chunks (40 pages + 4 PDFs + 1 DOCX)
