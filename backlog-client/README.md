```
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate -i /local/openapi.yaml -g python -o /local/src --additional-properties=packageName=backlog_client
```

変換を実行