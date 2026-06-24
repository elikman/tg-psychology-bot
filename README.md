####TG Psychology Bot

Telegram-бот для ознакомительного психологического интервью с использованием искусственного интеллекта.

Возможности
Проведение интервью из 10 вопросов
Анализ ответов с помощью DeepSeek через OpenRouter
Формирование отчёта о психологическом благополучии
Сохранение отчётов в SQLite
Свободный диалог с ИИ после прохождения интервью
Повторное прохождение интервью
Используемые технологии
Python 3.11+
Aiogram 3
OpenRouter API
DeepSeek Chat V3
SQLite
Aiosqlite
Структура проекта

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

Установка

Клонировать репозиторий:

git clone https://github.com/YOUR_USERNAME/tg-psychology-bot.git

Перейти в папку проекта:

cd tg-psychology-bot

Создать виртуальное окружение:

python -m venv venv

Активировать виртуальное окружение:

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

Установить зависимости:

pip install -r requirements.txt

Настройка

Создать файл .env:

BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY

##Запуск
```bash
python main.py
```
Использование
Отправить команду:

/start

Ответить на вопросы интервью.
Получить персональный отчёт.
Продолжить общение с ИИ через режим:
💬 Диалог
или начать заново:
🔄 Новое интервью

**Важно**
Бот предназначен исключительно для ознакомительных целей.
Он не ставит диагнозы, не определяет психические расстройства и не заменяет консультацию специалиста.
Все результаты являются информационными и не должны использоваться в качестве медицинского заключения.
