#!/bin/bash
# Startup script for RAG Chatbot

echo "Starting RAG Chatbot Application..."

# Start the backend server
echo "Starting backend server..."
cd app
uvicorn main:app --reload --port 8000 &
BACKEND_PID=$!

# Give backend time to start
sleep 3

# Start the frontend server (if in development)
echo "Starting frontend server..."
cd ../frontend
npm run dev

# Kill backend when frontend exits
trap "kill $BACKEND_PID" EXIT