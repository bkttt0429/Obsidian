
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\樹.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = 'const htmlCode = `'
end_marker = '`;'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)
html_content = content[start_idx + len(start_marker):end_idx]

return_start = html_content.find('return (')
return_end = html_content.rfind(');', return_start)
jsx_content = html_content[return_start + len('return ('):return_end]

lines = jsx_content.split('\n')
depth = 0
for i, line in enumerate(lines):
    # This is a very crude tag counter
    # It ignores self-closing tags if they have /> at the end
    
    # Remove self-closing tags like <Play /> or <div />
    line_no_self = re.sub(r'<\w+[^>]*/>', '', line)
    
    opens = len(re.findall(r'<\w+[^>]*>', line_no_self))
    closes = len(re.findall(r'</\w+>', line_no_self))
    
    depth += opens
    depth -= closes
    
    print(f"Line {i+1} (Depth {depth}): {line.strip()}")
