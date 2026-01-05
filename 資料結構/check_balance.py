
file_path = r'd:\obsidan\Note\obsidian\資料結構\樹.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<script type="text/babel">'
end_marker = '</script>'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)
script_content = content[start_idx + len(start_marker):end_idx]

# Check balance of { }
b_stack = 0
for i, char in enumerate(script_content):
    if char == '{':
        b_stack += 1
    elif char == '}':
        b_stack -= 1
        if b_stack < 0:
            print(f"Excess closing brace at index {i}")

print(f"Final brace balance: {b_stack}")

# Check balance of ( )
p_stack = 0
for i, char in enumerate(script_content):
    if char == '(':
        p_stack += 1
    elif char == ')':
        p_stack -= 1
        if p_stack < 0:
            print(f"Excess closing parenthesis at index {i}")

print(f"Final parenthesis balance: {p_stack}")
