# scripts/save_test.py
from app.db import save_message

def main():
    print("Inserting test query...")
    save_message("Testing save from script", "This is a test answer", ["chunk 1", "chunk 2"])
    print("✅ Test complete! Check MongoDB Compass.")

if __name__ == "__main__":
    main()
