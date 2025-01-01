import os
import argparse
from backlog_scraper.markdown_to_openapi import MarkdownToOpenAPI
from backlog_scraper.scraper import BacklogScraper
from backlog_scraper.openapi_merger import OpenAPIMerger
import json

def main():
    parser = argparse.ArgumentParser(description='Backlog API Documentation Tool')
    subparsers = parser.add_subparsers(dest='command', help='利用可能なコマンド')

    # OpenAPI YAMLファイルをマージ
    merge_openapi_parser = subparsers.add_parser('merge-openapi', help='OpenAPI YAMLファイルをマージ')

    # スクレイピングコマンド
    scrape_parser = subparsers.add_parser('scrape', help='BacklogのAPIドキュメントをスクレイピング')
    scrape_parser.add_argument('--output', default='docs', help='出力先ディレクトリ（デフォルト: docs）')

    # Markdown to YAML変換コマンド
    convert_parser = subparsers.add_parser('convert', help='MarkdownをOpenAPI YAMLに変換')
    convert_parser.add_argument('--input', default='docs', help='入力元ディレクトリ（デフォルト: docs）')
    convert_parser.add_argument('--output', default='api', help='出力先ディレクトリ（デフォルト: api）')

    args = parser.parse_args()

    if args.command == 'scrape':
        # スクレイピング実行
        scraper = BacklogScraper()
        scraper.scrape_all_pages(args.output)
    elif args.command == 'convert':
        # ANTHROPIC_API_KEYを環境変数から取得
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

        # 入力と出力のディレクトリパス
        input_dir = os.path.join(os.path.dirname(__file__), args.input)
        output_dir = os.path.join(os.path.dirname(__file__), args.output)

        # MarkdownToOpenAPIコンバーターを初期化して実行
        converter = MarkdownToOpenAPI(api_key)
        converter.convert_directory(input_dir, output_dir)
    elif args.command == 'merge-openapi':
        # OpenAPI YAMLファイルのマージを実行
        merger = OpenAPIMerger()
        api_dir = os.path.join(os.path.dirname(__file__), 'api')
        output_path = os.path.join(os.path.dirname(__file__), 'merged_openapi.yaml')
        
        merger.merge_files(api_dir)
        merger.save_merged_spec(output_path)
        print(f"OpenAPI仕様をマージしました: {output_path}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
