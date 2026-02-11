# RAG Chatbot API Documentation

## Base URL
`http://localhost:8000` (when running locally)

## Endpoints

### GET /
**Description:** Health check endpoint to verify the server is running.

**Response:**
```json
{
  "ok": true,
  "message": "RAG Chatbot backend is running 🚀"
}
```

### POST /chat
**Description:** Send a question to the RAG chatbot and receive an AI-generated response based on the indexed documents.

**Request Body:**
```json
{
  "question": "Your question here"
}
```

**Response:**
```json
{
  "question": "Your question here",
  "answer": "Generated answer from the AI",
  "sources": [
    "Source document chunk 1",
    "Source document chunk 2",
    "Source document chunk 3"
  ]
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the popular tourist destinations in Pakistan?"}'
```

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful request
- `422 Unprocessable Entity`: Invalid request format
- `500 Internal Server Error`: Server error during processing

## Headers

- `Content-Type: application/json` - Required for POST requests

## CORS Policy

The API allows requests from the following origins:
- `http://localhost:5173`
- `http://localhost:3000`
- `http://127.0.0.1:5173`
- `http://127.0.0.1:3000`

## Data Flow

1. User sends a question to `/chat`
2. Question is converted to an embedding vector
3. FAISS index is searched for similar document chunks
4. Top 3 matching chunks are retrieved
5. Gemini API generates a response using the context
6. Response and metadata are stored in MongoDB
7. Answer and sources are returned to the user