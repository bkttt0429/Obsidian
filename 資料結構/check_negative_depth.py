
import re

file_path = r'd:\obsidan\Note\obsidian\資料結構\depth_log.txt'
with open(file_path, 'r', encoding='utf-16') as f:
    lines = f.readlines()

for line in lines:
    if "Depth" in line:
        # Extract depth number
        match = re.search(r'Depth (-?\d+)', line)
        if match:
            d = int(match.group(1))
            if d < 0 or "</div>" in line:
                print(line.strip())
