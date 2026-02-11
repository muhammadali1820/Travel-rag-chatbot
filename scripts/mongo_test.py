# scripts/mongo_test.py
from app.db import save_message

def main():
    save_message("Hello from test!", "Hi there!", ["test context"])
    print("🎉 Test completed — check MongoDB Compass!")

if __name__ == "__main__":
    main()
