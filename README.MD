# 実装環境
- Windowes 11
- Docker v20.10.17
- VSCode

# Docekr起動

```
docker-compose up -d
```

## コンテナログイン
### Django

```
docker exec -it django sh
```

### Vue

```
docker exec -it vue sh
```

### Djangoカスタムコマンド実行

```
python manage.py ticket -a XX -c XX -s XX -sp
```

| 引数 | 説明 |
| ---- | ---- |
| -a, --adult | 整数:大人の人数 |
| -c, --child | 整数:子供の人数 |
| -s, --senior | 整数:シニアの人数 |
| -sp, --special | オプション:特別チケットプラン |

### Djangoテスト実行

```
python manage.py test app
```


### HTML Worksample実行

```
npm run dev
```