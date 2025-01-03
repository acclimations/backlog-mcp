# backlog api scraper

APIのドキュメントをスクレイピングして、Markdown化＆OpenAPI Spec化します

```
poetry run python main.py scrape
poetry run python convert_to_markdown.py
poetry run python main.py convert
poetry run python main.py merge-openapi
```

でできる

```
cp scraper/merged_openapi.yaml backlog-client/openapi.yaml
```
で後工程に回す