import os
import yaml
import json
import hashlib
from markdown import Markdown
from anthropic import Anthropic
from typing import Dict, Any

class MarkdownToOpenAPI:
    def __init__(self, api_key: str):
        self.anthropic = Anthropic(api_key=api_key)
        self.md = Markdown()
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0
        self.metadata_file = os.path.join(os.path.dirname(__file__), './api/metadata.json')
        self.load_metadata()
        
        # Few-shot examples for Claude
        self.few_shot_prompt = """
以下のMarkdownからOpenAPI仕様のYAMLを生成してください。
入力と出力の例を示します：

入力例1:
# ウォッチ情報の取得
ウォッチの情報を取得します。

## メソッド
GET

## URL
/api/v2/watchings/:watchingId

## URLパラメーター
| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| watchingId | 数値 | ウォッチのID |

## レスポンス例
```json
{{
    "id": 1,
    "alreadyRead": true
}}
```

出力例1:
openapi: 3.0.0
info:
  title: Backlog API
  version: 2.0.0
paths:
  /api/v2/watchings/{{watchingId}}:
    get:
      summary: ウォッチ情報の取得
      description: ウォッチの情報を取得します。
      operationId: getWatching
      parameters:
        - name: watchingId
          in: path
          required: true
          schema:
            type: integer
          description: "ウォッチのID"
      responses:
        '200':
          description: "成功時のレスポンス"
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  alreadyRead:
                    type: boolean

以下のMarkdownをOpenAPI仕様のYAMLに変換してください：

{markdown_content}

YAMLのみを出力してください。コードブロック（```）は使用せず、直接YAMLを出力してください。説明などは不要です。
Yaml内でダブルクォーテーション（"）が含まれる場合はエスケープしてください。
security回りの記述は不要です。
スキーマを外側に定義する必要はありません。
パラメータ名に`[]`を含む場合、それを削除しないでください。
文字列の中に`:`が含まれる場合、文字列全体をダブルクォーテーションで囲んでください。
"""

    def load_metadata(self):
        """メタデータをロードします。ファイルが存在しない場合は空のデータを作成します。"""
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {'file_hashes': {}}

    def save_metadata(self):
        """メタデータを保存します。"""
        os.makedirs(os.path.dirname(self.metadata_file), exist_ok=True)
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)

    def calculate_file_hash(self, file_path: str) -> str:
        """ファイルのSHA-256ハッシュを計算します。"""
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()

    def should_convert_file(self, input_path: str) -> bool:
        """ファイルを変換する必要があるかどうかを判断します。"""
        current_hash = self.calculate_file_hash(input_path)
        stored_hash = self.metadata.get('file_hashes', {}).get(input_path)
        
        if stored_hash == current_hash:
            print(f"Skipping {os.path.basename(input_path)} (unchanged)")
            return False
            
        self.metadata.setdefault('file_hashes', {})[input_path] = current_hash
        return True
        

    def convert_markdown_to_openapi(self, markdown_content: str) -> Dict[Any, Any]:
        """
        MarkdownをOpenAPI形式に変換します。
        
        Args:
            markdown_content: 変換するMarkdownコンテンツ
            
        Returns:
            Dict: OpenAPI仕様のディクショナリ
        """
        prompt = self.few_shot_prompt.format(markdown_content=markdown_content)
        
        # Claudeに変換を依頼
        response = self.anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            temperature=0,
            system="あなたはMarkdownをOpenAPI仕様に変換する専門家です。",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # トークン数と料金を計算
        input_tokens = len(prompt.split())  # 簡易的なトークン数計算
        output_tokens = len(response.content[0].text.split())
        
        # Claude-3-Opus-20240229の料金を計算
        input_cost = (input_tokens / 1_000_000) * 15  # $15 per 1M tokens
        output_cost = (output_tokens / 1_000_000) * 75  # $75 per 1M tokens
        
        # 合計を更新
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += input_cost + output_cost
        
        # レスポンスからYAMLコンテンツを抽出
        yaml_content = response.content[0].text.strip()
        # コードブロックが含まれている場合は削除
        if yaml_content.startswith('```'):
            yaml_content = '\n'.join(yaml_content.split('\n')[1:-1])
        
        # YAMLをパースして文字列をエスケープ
        data = yaml.safe_load(yaml_content)
        self.escape_strings_in_dict(data)
        return data

    def escape_strings_in_dict(self, data: Any):
        """辞書内の文字列をエスケープします。"""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and ('"' in value or "'" in value or ":" in value):
                    data[key] = value.replace('"', '\\"')
                self.escape_strings_in_dict(value)
        elif isinstance(data, list):
            for item in data:
                self.escape_strings_in_dict(item)

    def convert_file(self, input_path: str, output_path: str):
        """
        Markdownファイルを読み込み、OpenAPI YAMLファイルとして保存します。
        
        Args:
            input_path: 入力Markdownファイルのパス
            output_path: 出力YAMLファイルのパス
        """
        # Markdownファイルを読み込み
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # OpenAPI形式に変換
        openapi_dict = self.convert_markdown_to_openapi(markdown_content)
        
        # YAMLとして保存
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(openapi_dict, f, allow_unicode=True, sort_keys=False)

    def convert_directory(self, input_dir: str, output_dir: str) -> float:
        """
        ディレクトリ内のすべてのMarkdownファイルを変換します。
        変更があったファイルのみを処理します。
        
        Args:
            input_dir: 入力Markdownディレクトリのパス
            output_dir: 出力YAMLディレクトリのパス
            
        Returns:
            float: 合計コスト
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for filename in os.listdir(input_dir):
            if filename.endswith('.md') and filename.startswith('ja_docs_backlog_api_2_'):
                input_path = os.path.join(input_dir, filename)
                # ファイル名から'ja_docs_backlog_api_2_'を削除し、.mdを.yamlに変更
                output_filename = filename.replace('ja_docs_backlog_api_2_', '').replace('.md', '.yaml')
                output_path = os.path.join(output_dir, output_filename)
                
                if self.should_convert_file(input_path):
                    print(f"Converting {filename} to {output_filename}...")
                    self.convert_file(input_path, output_path)
                    
                    # 合計コストを表示
                    print(f"\n=== Cost Summary ===")
                    print(f"Total Input Tokens: {self.total_input_tokens:,}")
                    print(f"Total Output Tokens: {self.total_output_tokens:,}")
                    print(f"Total Cost: ${self.total_cost:.4f}")
                    self.save_metadata()
        
        # 合計コストを表示
        print(f"\n=== Cost Summary ===")
        print(f"Total Input Tokens: {self.total_input_tokens:,}")
        print(f"Total Output Tokens: {self.total_output_tokens:,}")
        print(f"Total Cost: ${self.total_cost:.4f}")
        
        # メタデータを保存
        self.save_metadata()
        return self.total_cost
