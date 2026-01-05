
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
depth = 0
for i, line in enumerate(lines):
    curr_line_no = line_offset + i
    # Very simple tag counting
    line_no_self = re.sub(r'<\w+[^>]*/>', '', line)
    opens = len(re.findall(r'<\w+[^>]*>', line_no_self))
    closes = len(re.findall(r'</\w+>', line_no_self))
    depth += opens
    depth -= closes
    
    # Only print if depth changes or it's a tag line
    if opens > 0 or closes > 0 or depth < 0:
        print(f"File Line {curr_line_no} (Depth {depth}): {line.strip()}")
