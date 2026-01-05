
import re

file_path = r'd:\obsidan\Note\obsidian\disjoinset.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for blocks that might contain the DSU code
# Commonly found in srcdoc attributes or script tags
patterns = [
    r'srcdoc="([^"]+)"',
    r'<script[^>]*>(.*?)</script>'
]

found = False
for pattern in patterns:
    matches = re.finditer(pattern, content, re.DOTALL)
    for i, match in enumerate(matches):
        data = match.group(1)
        # Check if DSU related keywords are in the block
        if 'Union' in data and 'Find' in data and ('parent' in data or 'root' in data):
            print(f"Found match in {pattern}, index {i}")
            print("Content Snippet:")
            print(data[:500] + "...")
            found = True
            # Save the extracted code to a file for review
            with open(f'extracted_dsu_code_{i}.txt', 'w', encoding='utf-8') as out:
                out.write(data)

if not found:
    print("No DSU code found using regex patterns.")
