
file_path = r'd:\obsidan\Note\obsidian\資料結構\divs_log.txt'
with open(file_path, 'r', encoding='utf-16') as f:
    lines = f.readlines()
    for line in lines:
        if "Line" in line:
            num = int(line.split(' ')[2])
            if 830 <= num <= 910:
                print(line.strip())
