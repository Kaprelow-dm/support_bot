# 🤖 Бот-поддержка (Rule-based NLP)
   - Telegram-бот для автоматизации ответов на частые вопросы клиентов.
   - Бот снимает с поддержки большинство типовых вопросов без LLM и без затрат на API
   - Не использует LLM, работает на анализе ключевых слов и нечетком поиске (fuzzy matching).

## Функционал
   - Распознавание текста с опечатками (fuzzy matching, rapidfuzz).
   - Мультикатегорийность (до 3 ответов в одном сообщении).
   - Защита от неадекватных запросов.
   - Удобное меню с кнопками.

## Стек
   - Python 3.12
   - pyTelegramBotAPI
   - RapidFuzz
   - python-dotenv
   - pytest

## Тестирование
Покрытие тестами: 12 сценариев (pytest).
    Пример работы тестов:
<img width="969" height="315" alt="Pytests" src="https://github.com/user-attachments/assets/244efcd3-5a75-4cec-afb2-b05866b88d18" />

## 🚀 Демо
Тест-драйв бота: [@Answering_Support](https://t.me/Answering_Support_bot)
