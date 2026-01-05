
file_path = r'd:\obsidan\Note\obsidian\資料結構\divs_log.txt'
with open(file_path, 'r', encoding='utf-16') as f:
    lines = f.readlines()
    for line in lines[-50:]:
        print(line.strip())
