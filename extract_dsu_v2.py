
import re
import html

file_path = r'd:\obsidan\Note\obsidian\disjoinset.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try finding srcdoc with different quotes and escapes
matches = re.findall(r'srcdoc=([\'"])(.*?)\1', content, re.DOTALL)

print(f"Found {len(matches)} srcdoc blocks.")

for i, (quote, data) in enumerate(matches):
    decoded = html.unescape(data)
    if 'Union' in decoded and 'Find' in decoded:
        print(f"Block {i} looks like DSU code!")
        with open(f'dsu_block_{i}.html', 'w', encoding='utf-8') as out:
            out.write(decoded)
    else:
        print(f"Block {i} prefix: {decoded[:100]}")
