## Сборка контейнера

```bash
docker build --no-cache --squash -t python_2025_20 -f Dockerfile .
```

## Запуск контейнера

```bash
docker run -v ~/PycharmProjects/python_2025_20:/src -p 8000:8000 -it python_2025_20 /bin/bash
```

## Из docker

### Установка зависимостей

```bash
uv sync
```


### Запуск сервера

```bash
uv run uvicorn main:app --host 0.0.0.0 --reload
```

## Проверка сервиса (на хост машине)


```bash
curl -X 'POST' 'http://localhost:8000/get_text_tonality/' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I hate something"}'
```

"most probable tonality is bad"

```bash
curl -X 'POST' 'http://localhost:8000/get_text_tonality/' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I love something"}'
```

"most probable tonality is good"
