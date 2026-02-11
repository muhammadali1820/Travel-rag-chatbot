# scripts/chunk_tourism_text.py

def split_text_streaming(file_path, output_path, chunk_size=800, chunk_overlap=100):
    """
    Split large text files into smaller chunks safely without using much memory.
    """
    print("⏳ Processing large file safely...")

    buffer = ""
    chunks_count = 0

    with open(file_path, "r", encoding="utf-8", errors="ignore") as infile, \
     open(output_path, "w", encoding="utf-8", errors="ignore") as outfile:
        for line in infile:
            buffer += line.strip() + " "

            # When buffer reaches chunk_size, save a chunk
            if len(buffer) >= chunk_size:
                chunk = buffer[:chunk_size]
                outfile.write(chunk.strip() + "\n---CHUNK-END---\n")
                chunks_count += 1

                # keep a bit of overlap for context
                buffer = buffer[chunk_size - chunk_overlap:]

        # save last leftover text
        if buffer.strip():
            outfile.write(buffer.strip() + "\n---CHUNK-END---\n")
            chunks_count += 1

    print(f"✅ Done! Created {chunks_count} chunks and saved to {output_path}")


# 🔹 Run the function
split_text_streaming(
    file_path="data/extracted_tourism_text.txt",
    output_path="data/tourism_text_chunks.txt",
    chunk_size=800,
    chunk_overlap=100
)
