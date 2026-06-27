import asyncio

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config.config import BOT_TOKEN

from ai.openai_client import (
    generate_final_report,
    free_chat
)

from database.database import (
    init_db,
    add_user,
    save_report
)

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

user_answers = {}


#Список вопросов ознакомительного психологического интервью.
INTERVIEW_QUESTIONS = [
    "Что вас сейчас беспокоит больше всего?",
    "Как давно вы испытываете это состояние?",
    "Насколько сильно это влияет на вашу повседневную жизнь?",
    "Как бы вы описали своё настроение в последние недели?",
    "Как обстоят дела со сном?",
    "Чувствуете ли вы усталость или нехватку энергии в течение дня?",
    "Есть ли сейчас стрессовые ситуации в работе, учёбе или личной жизни?",
    "Есть ли люди, с которыми вы можете открыто поговорить о своих переживаниях?",
    "Что помогает вам справляться с этим состоянием?",
    "Что бы вы хотели изменить в своём состоянии в первую очередь?"]


@dp.message(CommandStart())
async def start(message: Message):
    """
    Обрабатывает команду /start.

    Регистрирует пользователя в базе данных,
    очищает предыдущие ответы и запускает
    ознакомительное психологическое интервью.

    Args:
        message (Message): Сообщение пользователя.
    """
    user_id = message.from_user.id

    await add_user(
        user_id,
        message.from_user.username
    )

    user_answers[user_id] = []

    await message.answer(
        "Здравствуйте.\n\n"
        "Я проведу ознакомительное интервью.\n\n"
        f"{INTERVIEW_QUESTIONS[0]}"
    )


@dp.message()
async def chat(message: Message):
    """
    Обрабатывает сообщения пользователя.

    Сохраняет ответы пользователя,
    последовательно задаёт вопросы интервью,
    а после завершения интервью генерирует
    итоговый отчёт с помощью искусственного интеллекта.

    Args:
        message (Message): Сообщение пользователя.
    """
    user_id = message.from_user.id

    if user_id not in user_answers:
        user_answers[user_id] = []

    user_answers[user_id].append(
        message.text
    )

    current = len(
        user_answers[user_id]
    )

    if current >= len(INTERVIEW_QUESTIONS):

        report = await generate_final_report(
            INTERVIEW_QUESTIONS,
            user_answers[user_id]
        )

        await save_report(
            user_id,
            report
        )

        await message.answer(report)

        user_answers[user_id] = []

        return

    await message.answer(
        INTERVIEW_QUESTIONS[current]
    )


async def main():
    """
    Запускает Telegram-бота.

    Выполняет инициализацию базы данных
    и начинает получение сообщений
    от пользователей.
    """
    await init_db()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
