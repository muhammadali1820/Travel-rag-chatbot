# Contributing to RAG Chatbot

Thank you for your interest in contributing to the RAG Chatbot project! This document outlines the guidelines for contributing to this repository.

## Table of Contents
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/rag-chatbot.git
   cd rag-chatbot
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

## Development Workflow

1. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b bugfix/issue-description
   ```

2. Make your changes following the code style guidelines

3. Test your changes thoroughly

4. Commit your changes with a descriptive commit message:
   ```bash
   git add .
   git commit -m "Add amazing feature that does X"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/amazing-feature
   ```

## Code Style

### Python
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small when possible

### JavaScript/React
- Use consistent naming conventions
- Follow Airbnb JavaScript Style Guide
- Add comments for complex logic
- Use functional components with hooks when possible

### Documentation
- Update README.md if adding new features
- Add inline comments for complex algorithms
- Keep API documentation up to date

## Pull Request Process

1. Ensure your PR addresses a single issue or adds a single feature
2. Update the README.md with details of changes if applicable
3. Add tests if applicable
4. Ensure all tests pass
5. Submit your pull request with a clear title and description
6. Link any related issues in the PR description

## Reporting Issues

When reporting issues, please include:
- A clear title and description
- Steps to reproduce the issue
- Expected vs. actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots if applicable

## Development Commands

### Backend
```bash
# Start the backend server
cd app
uvicorn main:app --reload --port 8000

# Run tests (if any exist)
python -m pytest
```

### Frontend
```bash
# Start the frontend development server
cd frontend
npm run dev

# Build for production
npm run build
```

### Data Processing
```bash
# Process and index new documents
python scripts/ingest.py
```

## Questions?

If you have any questions about contributing, feel free to open an issue with the "question" label.