
from bs4 import BeautifulSoup

file_path = r'd:\obsidan\Note\obsidian\disjoinset.html'

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

scripts = soup.find_all('script')
print(f"Found {len(scripts)} script tags.")

for i, script in enumerate(scripts):
    content = script.string if script.string else ""
    if 'Union' in content and 'Find' in content:
        print(f"Script {i} matches!")
        with open(f'script_{i}.js', 'w', encoding='utf-8') as out:
            out.write(content)

# Also check for markdown code blocks in the HTML text
texts = soup.find_all(string=True)
for text in texts:
    if '```javascript' in text or '```jsx' in text or '```html' in text:
        if 'Union' in text and 'Find' in text:
            print("Found markdown code block in text!")
            with open('found_markdown.md', 'w', encoding='utf-8') as out:
                out.write(text)
