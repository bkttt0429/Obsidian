
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\temp_gemini.html'

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Look for patterns that look like JS code for Morris Traversal
# e.g., "while (curr", "while(current", "predecessor", "threads"
patterns = [
    r'while\s*\(\s*curr',
    r'while\s*\(\s*current',
    r'visitor',
    r'Morris'
]

for p in patterns:
    indices = [m.start() for m in re.finditer(p, content)]
    if indices:
        print(f"Found '{p}' at {len(indices)} locations.")
        for i, idx in enumerate(indices[:3]): # Check first 3
            print(f"--- Context for '{p}' #{i+1} ---")
            start = max(0, idx - 200)
            end = min(len(content), idx + 800)
            chunk = content[start:end]
            # Clean up JSON
            clean_chunk = chunk.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\u003c', '<').replace('\\u003e', '>')
            print(clean_chunk)
            print("-" * 40)
