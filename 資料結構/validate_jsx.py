
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\樹.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the dataviewjs block or at least the htmlCode content
start_marker = 'const htmlCode = `'
end_marker = '`;'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find htmlCode block")
    exit()

html_content = content[start_idx + len(start_marker):end_idx]

# Look for the return statement in App
return_start = html_content.find('return (')
return_end = html_content.rfind(');', return_start) # last ); before end of script

if return_start == -1 or return_end == -1:
    print("Could not find return statement")
    exit()

jsx_content = html_content[return_start + len('return ('):return_end]

# Count tags
tags = re.findall(r'<(/?\w+)', jsx_content)
stack = []
for tag in tags:
    if tag.startswith('/'):
        tag_name = tag[1:]
        if not stack:
            print(f"Error: Unexpected closing tag </{tag_name}>")
        else:
            last = stack.pop()
            if last != tag_name:
                print(f"Error: Mismatched tags <{last}> and </{tag_name}>")
    else:
        # Check if self-closing
        # Very simple check: find index and see if /> follows
        # This is tricky because of the simple regex
        stack.append(tag)

print(f"Final stack after processing: {stack}")

# Simple check for { }
open_braces = jsx_content.count('{')
close_braces = jsx_content.count('}')
print(f"Braces: {{ {open_braces}, }} {close_braces}")

# Print line by line with numbering to matching 216
lines = jsx_content.split('\n')
for i, line in enumerate(lines):
    print(f"{i+1}: {line}")
