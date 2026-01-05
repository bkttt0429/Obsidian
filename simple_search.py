
file_path = r'd:\obsidan\Note\obsidian\disjoinset.html'
with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'Union' in line or 'Find' in line:
            print(f"Line {i}: {line[:200]}")
            if i > 1000: # limit output
                break
