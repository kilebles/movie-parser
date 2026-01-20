# Movie Parser

Парсер топ-10 фильмов с Кинопоиска с экспортом в Excel.

## Установка

```bash
uv sync
```

## Настройка

1. Получить API-ключ на [kinopoiskapiunofficial.tech](https://kinopoiskapiunofficial.tech)
2. Скопировать `.env.example` в `.env`

## Запуск

```bash
uv run main.py
```

Результат сохраняется в `top_movies.xlsx` с ссылками на фильмы.

## Структура проекта

```
src/
├── config/ # Настройки из .env
├── entities/ # Модель данных (Movie)
├── exporters/ # Экспорт в Excel
├── parsers/ # Парсер Кинопоиска
└── services/ # Бизнес-логика
```
