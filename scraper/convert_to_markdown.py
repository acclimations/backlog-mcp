import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_markdown_content(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Markdownの部分を抽出
    match = re.search(r'<!-- Markdown start -->(.*?)<!-- Markdown end -->', content, re.DOTALL)
    if not match:
        return None
    
    html_content = match.group(1).strip()
    
    # BeautifulSoupでHTMLをパース
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 不要なdiv要素を削除
    for div in soup.find_all('div', {'class': ['break-all', 'markdown', 'md:pb-26']}):
        div.unwrap()
    
    # HTMLからMarkdownへの変換
    markdown = ''
    
    # 全ての要素を順番に処理
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'table']):
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            markdown += '#' * level + ' ' + element.get_text().strip() + '\n\n'
        
        elif element.name == 'p':
            markdown += element.get_text().strip() + '\n\n'
        
        elif element.name == 'pre':
            code = element.get_text().strip()
            markdown += '```\n' + code + '\n```\n\n'
        
        elif element.name == 'table':
            # ヘッダー行
            headers = []
            for th in element.find_all('th'):
                headers.append(th.get_text().strip())
            
            if headers:
                markdown += '| ' + ' | '.join(headers) + ' |\n'
                markdown += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'
            
            # データ行
            for tr in element.find_all('tr'):
                cells = []
                for td in tr.find_all('td'):
                    cells.append(td.get_text().strip())
                if cells:
                    markdown += '| ' + ' | '.join(cells) + ' |\n'
            markdown += '\n'
    
    return markdown.strip()

def process_all_files():
    docs_dir = Path('./backlog_docs')
    output_dir = Path('./docs')
    
    for html_file in docs_dir.glob('*.html'):
        markdown_content = extract_markdown_content(str(html_file))
        if markdown_content:
            output_file = output_dir / (html_file.stem + '.md')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f'Converted {html_file.name} to {output_file.name}')

if __name__ == '__main__':
    process_all_files()
