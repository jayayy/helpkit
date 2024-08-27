import pandas as pd
import os

def split_csv(file_path, chunk_size=140, rows_size=1000):
    # Open the original CSV file
    chunk_number = 1
    chunk_size_bytes = chunk_size * 1024 * 1024  # Convert MB to bytes
    rows_per_chunk = rows_size  # Start with a fixed number of rows per chunk

    with pd.read_csv(file_path, chunksize=rows_per_chunk) as reader:
        for chunk in reader:
            chunk_file = f"chunk_{chunk_number}.csv"
            chunk.to_csv(chunk_file, index=False, mode='a', header=not os.path.exists(chunk_file))
            chunk_number += 1

            # Check if the file size exceeds the limit
            if os.path.getsize(chunk_file) >= chunk_size_bytes:
                chunk_number += 1  # Move to the next chunk

            print(f"Created: {chunk_file} with size {os.path.getsize(chunk_file) / (1024 * 1024):.2f} MB")

# Usage
split_csv('ivrJourneys.csv', chunk_size=140, rows_size=800)  # Replace 'your_large_file.csv' with your file path
