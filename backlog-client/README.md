# backlog-client

BacklogのREST APIを簡単に利用するためのPythonクライアントライブラリを生成するプロジェクトです。

## 概要

このプロジェクトは、BacklogのREST API仕様（OpenAPI/Swagger）からPythonクライアントライブラリを自動生成します。生成されたライブラリを使用することで、BacklogのAPIを簡単に利用することができます。

## 前提条件

- Python 3.8以上
- Docker（クライアントライブラリの生成に使用）

## インストール方法

### 1. クライアントライブラリの生成

以下のコマンドを実行して、OpenAPI Generatorを使用してPythonクライアントライブラリを生成します：

```bash
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate \
  -i /local/openapi.yaml \
  -g python \
  -o /local/src \
  --additional-properties=packageName=backlog_client
```

### 2. 生成されたライブラリのインストール

生成されたライブラリは以下の方法でインストールできます：

```bash
cd src
pip install -e .
```

## 使用方法

```python
import os
import backlog_client
from backlog_client.rest import ApiException

# APIクライアントの設定
configuration = backlog_client.Configuration(
    host="https://your-space.backlog.com"  # あなたのBacklogスペースのURLを指定
)

# APIキーの設定
configuration.api_key['apiKey'] = os.environ["BACKLOG_API_KEY"]

# APIクライアントの初期化
with backlog_client.ApiClient(configuration) as api_client:
    # APIインスタンスの作成
    api_instance = backlog_client.DefaultApi(api_client)
    
    try:
        # プロジェクト一覧の取得
        projects = api_instance.get_projects()
        print("プロジェクト一覧:")
        for project in projects:
            print(f"- {project.name} (ID: {project.id})")
            
    except ApiException as e:
        print(f"エラーが発生しました: {e}")
```

## 開発方法

1. OpenAPI仕様の更新
   - `openapi.yaml`ファイルを編集してAPI仕様を更新します

2. クライアントライブラリの再生成
   - 上記の「クライアントライブラリの生成」コマンドを実行して、最新の仕様からライブラリを再生成します

3. テストの実行
   ```bash
   cd src
   python -m pytest
   ```

## 利用可能なAPI

生成されたクライアントライブラリでは、以下のようなBacklog APIの機能が利用可能です：

- プロジェクト管理
- 課題管理
- Wiki管理
- Git管理
- ユーザー管理
- など

詳細なAPI仕様については、生成された`src/docs`ディレクトリ内のドキュメントを参照してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については`LICENSE`ファイルを参照してください。
