# backlog api scraper

APIのドキュメントをスクレイピングして、Markdown化＆OpenAPI Spec化します

## セットアップ

```bash
uv venv
.venv\Scripts\activate
uv pip install -e ".[dev]"
```

## 使用方法

```bash
python main.py scrape
python convert_to_markdown.py
python main.py convert
python main.py merge-openapi
```

でできる

```bash
cp scraper/merged_openapi.yaml backlog-client/openapi.yaml
```
で後工程に回す
