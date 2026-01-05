
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\temp_gemini.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

indices = [m.start() for m in re.finditer('Morris', content)]

print(f"Found {len(indices)} occurrences of 'Morris'")

for i, idx in enumerate(indices):
    print(f"--- Occurrence {i+1} ---")
    # Extract a chunk
    start = max(0, idx - 500)
    end = min(len(content), idx + 2500)
    chunk = content[start:end]
    # Try to clean up JSON string escapes if it looks like one
    try:
        # A simple replacement for common escaped chars
        clean_chunk = chunk.replace('\\n', '\n').replace('\\"', '"').replace('\\u003c', '<').replace('\\u003e', '>')
        print(clean_chunk)
    except:
        print(chunk)
    print("\n")
