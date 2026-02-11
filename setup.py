"""
Setup script for the RAG Chatbot project
"""
from setuptools import setup, find_packages

setup(
    name="rag-chatbot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.122.0",
        "uvicorn==0.38.0",
        "sentence-transformers==5.1.2",
        "faiss-cpu==1.13.0",
        "python-dotenv==1.0.1",
        "pymongo==4.15.4",
        "google-generativeai==0.8.5",
        "langchain-text-splitters==0.3.2",
        "pydantic==2.12.4",
        "numpy==2.2.6",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A RAG chatbot for tourism information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rag-chatbot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)