
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\depth_log_improved.txt'
with open(file_path, 'r', encoding='utf-16') as f:
    lines = f.readlines()

for line in lines:
    if "(Depth " in line:
        match = re.search(r'Depth (-?\d+)', line)
        if match:
            d = int(match.group(1))
            if d <= 0:
                print(line.strip())
            elif d > 10: # Maybe something went wrong and it's too high?
                 pass
