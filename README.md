# RAG Chatbot - Tourism Information Assistant

This is a Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about tourism using contextual information. The system combines local embeddings with Google's Gemini AI to provide accurate, context-aware responses.

## 🚀 Features

- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval with AI generation for accurate responses
- **Local Embeddings**: Uses Sentence Transformers for efficient semantic search
- **FAISS Indexing**: Fast similarity search using Facebook AI Similarity Search
- **MongoDB Integration**: Stores conversation history and metadata
- **React Frontend**: Modern UI for interacting with the chatbot
- **Gemini Integration**: Leverages Google's powerful Gemini AI model

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend     │────│   FastAPI        │────│   Gemini API    │
│   (React)      │    │   Backend        │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              │
                       ┌──────────────────┐
                       │   FAISS Index    │
                       │   (Vector DB)    │
                       └──────────────────┘
                              │
                       ┌──────────────────┐
                       │   Document Store │
                       │   (Pickle file)  │
                       └──────────────────┘
                              │
                       ┌──────────────────┐
                       │   MongoDB        │
                       │   (Chat History) │
                       └──────────────────┘
```

## 📁 Project Structure

```
rag-chatbot/
├── app/                    # Backend application
│   ├── main.py            # FastAPI application entry point
│   ├── embeddings.py      # Local embedding utilities
│   ├── gemini_helper.py   # Gemini API integration
│   ├── db.py             # MongoDB connection
│   ├── utils.py          # Utility functions
│   └── __init__.py       # Package initialization
├── frontend/              # React frontend
│   ├── src/
│   ├── package.json
│   └── ...
├── scripts/               # Data processing scripts
│   ├── ingest.py         # Data ingestion pipeline
│   ├── chunk_tourism_text.py
│   ├── extract_tourism_text.py
│   └── ...
├── data/                  # Source documents (to be added)
├── store/                 # Vector stores (generated)
│   ├── faiss.index       # FAISS vector index
│   └── docstore.pkl      # Document store mapping
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🛠️ Technologies Used

### Backend
- **Python 3.x**
- **FastAPI**: Modern, fast web framework
- **Sentence Transformers**: Local embedding generation
- **FAISS**: Efficient similarity search
- **Pydantic**: Data validation
- **MongoDB**: Conversation storage
- **Google Generative AI**: LLM integration

### Frontend
- **React**: UI library
- **Vite**: Build tool
- **CSS**: Styling

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 18+
- MongoDB (local or cloud instance)
- Google Gemini API key

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd rag-chatbot
```

2. **Set up Python virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies**
```bash
pip install fastapi uvicorn sentence-transformers faiss-cpu python-dotenv pymongo google-generativeai langchain-text-splitters
```

4. **Install Node.js dependencies**
```bash
cd frontend
npm install
```

5. **Set up environment variables**
Create a `.env` file in the root directory:
```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=rag_chatbot
MONGODB_COLLECTION=messages

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here
```

6. **Prepare data**
Add your source documents to the `data/` directory (e.g., `data/rag_source.txt`)

7. **Run data ingestion**
```bash
python scripts/ingest.py
```

## 🚀 Usage

### Running the Backend
```bash
cd rag-chatbot
uvicorn app.main:app --reload --port 8000
```

### Running the Frontend
```bash
cd rag-chatbot/frontend
npm run dev
```

The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:5173`.

### Using the API Directly
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the popular tourist destinations?"}'
```

## 📄 Scripts Overview

- `scripts/ingest.py`: Processes source documents and creates FAISS index
- `scripts/chunk_tourism_text.py`: Splits documents into chunks
- `scripts/extract_tourism_text.py`: Extracts text from various formats
- `scripts/generate_tourism_embeddings.py`: Generates embeddings for documents

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=rag_chatbot
MONGODB_COLLECTION=messages

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🤖 How It Works

1. **Data Ingestion**: Documents are processed, chunked, and converted to embeddings
2. **Indexing**: Embeddings are stored in a FAISS index for fast similarity search
3. **Query Processing**: User questions are embedded and matched against the index
4. **Context Retrieval**: Top matching document chunks are retrieved
5. **Response Generation**: Gemini generates a response using the retrieved context
6. **Storage**: Conversations are stored in MongoDB for analytics

## 🧪 Testing

To test the system:
1. Start the backend server
2. Open the frontend in your browser
3. Ask questions related to your tourism data
4. View the retrieved sources and generated responses

## 🚨 Troubleshooting

- **FAISS Index Not Found**: Run `python scripts/ingest.py` to create the index
- **Gemini API Error**: Check your API key in `.env` file
- **MongoDB Connection Error**: Verify your MongoDB URI in `.env` file
- **Embedding Model Issues**: Ensure internet connectivity for model download

## 📈 Future Enhancements

- Support for multiple document formats (PDF, DOCX, etc.)
- Advanced query routing
- Caching mechanisms
- User authentication
- Admin dashboard for content management
- Multi-language support

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.