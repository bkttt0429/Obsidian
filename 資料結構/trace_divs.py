
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
return_offset = content.find('return (', start_idx)
line_offset = content[:return_offset].count('\n') + 1

return_end = html_content.rfind(');', return_start)
jsx_content = html_content[return_start + len('return ('):return_end]

lines = jsx_content.split('\n')
div_depth = 0
for i, line in enumerate(lines):
    curr_line_no = line_offset + i
    
    # Count occurrences of <div and </div>
    # Use word boundary to avoid matching <div> and <div-something
    opens = len(re.findall(r'<div[\s>]', line))
    closes = len(re.findall(r'</div>', line))
    
    div_depth += opens
    div_depth -= closes
    
    if opens > 0 or closes > 0:
        print(f"Line {curr_line_no} (Div Depth {div_depth}): {line.strip()}")

print(f"Final Div Depth: {div_depth}")
