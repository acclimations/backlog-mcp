import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class BacklogScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.session = requests.Session()

    def is_valid_url(self, url):
        """URLが有効なBacklog APIドキュメントのURLかチェック"""
        parsed = urlparse(url)
        return (
            parsed.netloc == "developer.nulab.com"
            and "/ja/docs/backlog/" in parsed.path
            and not url.endswith((".png", ".jpg", ".jpeg", ".gif", ".pdf"))
        )

    def get_filename_from_url(self, url):
        """URLからファイル名を生成"""
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if path.endswith("/"):
            path += "index"
        return os.path.join(self.output_dir, f"{path.replace('/', '_')}.html")

    def save_html(self, url, html_content):
        """HTMLコンテンツをファイルに保存"""
        filename = self.get_filename_from_url(url)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # リンクを相対パスに変換
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all(["a", "link", "script", "img"]):
            for attr in ["href", "src"]:
                if link.get(attr):
                    absolute_url = urljoin(url, link[attr])
                    if self.is_valid_url(absolute_url):
                        link[attr] = os.path.relpath(
                            self.get_filename_from_url(absolute_url),
                            os.path.dirname(filename)
                        )

        # DOCTYPE宣言を追加
        html_content = "<!DOCTYPE html>\n" + html_content
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"保存完了: {filename}")

    def extract_links(self, url, html_content):
        """ページから有効なリンクを抽出"""
        soup = BeautifulSoup(html_content, "html.parser")
        links = set()
        
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                absolute_url = urljoin(url, href)
                if self.is_valid_url(absolute_url):
                    links.add(absolute_url)
        
        return links

    def scrape_page(self, url):
        """ページをスクレイピング"""
        if url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        print(f"スクレイピング中: {url}")
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            response.encoding = 'utf-8'  # 明示的にUTF-8を指定
            
            # メタタグのcharsetを追加
            soup = BeautifulSoup(response.text, "html.parser")
            if not soup.find("meta", charset=True):
                meta_charset = soup.new_tag("meta")
                meta_charset["charset"] = "utf-8"
                if soup.head:
                    soup.head.insert(0, meta_charset)
                else:
                    head = soup.new_tag("head")
                    head.append(meta_charset)
                    soup.insert(0, head)
            
            self.save_html(url, str(soup))
            links = self.extract_links(url, response.text)
            
            # 抽出したリンクを再帰的にスクレイピング
            for link in links:
                # time.sleep(1)  # サーバーへの負荷を軽減
                self.scrape_page(link)
                
        except Exception as e:
            print(f"エラー ({url}): {str(e)}")

    def run(self):
        """スクレイピングを開始"""
        self.scrape_page(self.base_url)

def main():
    base_url = "https://developer.nulab.com/ja/docs/backlog/"
    output_dir = "backlog_docs"
    
    scraper = BacklogScraper(base_url, output_dir)
    scraper.run()

if __name__ == "__main__":
    main()
