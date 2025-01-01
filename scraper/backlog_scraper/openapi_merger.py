import os
import yaml
from typing import Dict, Any

class OpenAPIMerger:
    def __init__(self):
        self.merged_spec = {
            'openapi': '3.0.0',
            'info': {
                'title': 'Backlog API',
                'version': '1.0.0',
                'description': 'Backlog REST API specification'
            },
            'paths': {},
            'components': {
                'schemas': {},
                'securitySchemes': {
                    'apiKey': {
                        'type': 'apiKey',
                        'in': 'query',
                        'name': 'apiKey'
                    }
                }
            },
            "security": [{"apiKey": []}]
        }

    def _load_yaml(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _merge_operation(self, path: str, method: str, operation: Dict[str, Any]) -> None:
        if path not in self.merged_spec['paths']:
            self.merged_spec['paths'][path] = {}
        self.merged_spec['paths'][path][method] = operation

    def merge_files(self, api_dir: str) -> None:
        for filename in os.listdir(api_dir):
            if not filename.endswith('.yaml'):
                continue

            file_path = os.path.join(api_dir, filename)
            spec = self._load_yaml(file_path)

            # 各ファイルには1つのパスと1つのメソッドのみが含まれていることを想定
            for path, path_item in spec.get('paths', {}).items():
                for method, operation in path_item.items():
                    self._merge_operation(path, method, operation)

            # コンポーネントのマージ（存在する場合）
            if 'components' in spec and 'schemas' in spec['components']:
                self.merged_spec['components']['schemas'].update(
                    spec['components']['schemas']
                )

    def save_merged_spec(self, output_path: str) -> None:
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.merged_spec, f, allow_unicode=True, sort_keys=False)
