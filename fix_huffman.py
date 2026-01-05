
import os

source_path = r'd:\obsidan\Note\obsidian\huffman_files\shim.html'
target_path = r'd:\obsidan\Note\obsidian\資料結構\樹.md'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Full escaping logic for putting into a JS template literal
# 1. Backslashes
escaped = content.replace('\\', '\\\\')
# 2. Backticks
escaped = escaped.replace('`', '\\`')
# 3. Dollar signs before braces
escaped = escaped.replace('${', '\\${')

# Prepare the dataviewjs block
# NOTE: We use a multi-line string for the block itself, 
# and the outer JS uses a regular template literal (NOT String.raw) 
# so the escapes work.
block = f"""
## 🎬 哈夫曼樹演算法動態演示

```dataviewjs
const htmlCode = `{escaped}`;

dv.el("iframe", "", {{
    attr: {{
        srcdoc: htmlCode,
        style: "width: 100%; height: 600px; border: none; border-radius: 1rem; box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);"
    }}
}});
```
"""

with open(target_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove old Huffman block if exists
new_lines = []
skip = False
for line in lines:
    if '## 🎬 哈夫曼樹演算法動態演示' in line:
        skip = True
        continue
    if skip:
        if line.startswith('```') and 'dataviewjs' not in line: # End of code block
             # Check if next few lines are blank or another section
             skip = False
             continue
        continue
    new_lines.append(line)

# Find insertion point: After "# 三、霍夫曼樹"
insertion_index = -1
for i, line in enumerate(new_lines):
    if '# 三、霍夫曼樹' in line:
        insertion_index = i + 1
        break

if insertion_index != -1:
    new_lines.insert(insertion_index, block + "\n")
else:
    # Fallback to appending at the end if not found
    new_lines.append(block)

with open(target_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Successfully fixed and moved Huffman visualizer to index {insertion_index}")
