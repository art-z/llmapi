# FastAPI + YandexGPT + Postgres

Простой API-сервис для общения с моделью **YandexGPT** через FastAPI, с сохранением истории диалогов в **Postgres**.

---

## 📦 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/art-z/llmapi.git
cd llmapi
```
### 2. Создать файл окружения
```bash
cp .env.example .env
```

DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres<br>
YANDEX_API_KEY=api_ключ<br>
YANDEX_MODEL_URI=gpt://<ID_каталога>/yandexgpt-lite  

### 3. Запустить контейнеры
```bash
docker-compose up --build
```

После запуска:<br>
API доступен на http://localhost:8000<br>
Swagger UI → http://localhost:8000/docs  


### Отправить запрос к модели
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Привет, как дела?"}'
```

### Пример ответа:
```bash
{
  "id": 1,
  "prompt": "Привет, как дела?",
  "response": "Здравствуйте! Всё хорошо, спасибо"
}
```

## 📜 Лицензия
MIT — [оригинал](./LICENSE), [русский](./LICENSE.ru)