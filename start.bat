@echo off
REM Batch script to start RAG Chatbot

echo Starting RAG Chatbot Application...

REM Start the backend server in a separate window
echo Starting backend server...
start cmd /k "cd /d app && uvicorn main:app --reload --port 8000"

REM Wait a bit for the backend to start
timeout /t 3 /nobreak >nul

REM Start the frontend server
echo Starting frontend server...
cd /d frontend
npm run dev