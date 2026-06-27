# TG Psychology Bot

Telegram-бот для ознакомительного психологического интервью с использованием искусственного интеллекта.

Возможности
Проведение интервью из 10 вопросов
Анализ ответов с помощью DeepSeek через OpenRouter
Формирование отчёта о психологическом благополучии
Сохранение отчётов в SQLite
Свободный диалог с ИИ после прохождения интервью
Повторное прохождение интервью

## Используемые технологии
Python 3.11+, Aiogram 3, OpenRouter API, DeepSeek Chat V3, SQLite, Aiosqlite

# Структура проекта:
tg_psychology_bot/
├── ai/

│ └── openai_client.py

├── config/

│ └── config.py

├── database/

│ └── database.py

├── .env

├── .gitignore

├── main.py

├── requirements.txt

└── README.md

# Установка. Как развернуть проект на локальной машине
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/elikman/tg-psychology-bot.git
```

```
cd tg-psychology-bot
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла `requirements.txt`:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Настройка

Создать файл .env:
```
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```
Запуск
```
python main.py

Использование
Отправить команду:

/start

Ответить на вопросы интервью.
Получить персональный отчёт.
Продолжить общение с ИИ через режим:
💬 Диалог
или начать заново:
🔄 Новое интервью
