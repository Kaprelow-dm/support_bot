import re
from rapidfuzz import fuzz

CATEGORIES = {
    "доставка": ["достав", "привез", "курьер", "отправ", "мкад", "регион"],
    "оплата": ["оплат", "плат", "карт", "сбп", "налич", "налом", "перевод"],
    "возврат": ["возврат", "верну", "обмен", "гарант"],
    "цена": ["цен", "стоим", "скольк", "прайс", "руб", "куп"],
    "ассортимент": ["ассортимент", "каталог", "что есть", "шмот", "одежд", "размер", "товар"]
}

ANSWERS = {
    "доставка": "Доставка по Москве (в пределах МКАД + 2 км) — бесплатно. В регионы — от 1500 руб. Точную стоимость уточняйте у оператора при оформлении заказа.",
    "оплата": "Оплата картой, СБП или наличными при получении.",
    "возврат": "Возврат в течение 14 дней при наличии чека. Гарантия на товар — 30 дней.",
    "цена": "Цена зависит от лота и объема заказа. С полным ассортиментом вы можете ознакомиться на нашем сайте: example.com.",
    "ассортимент": "С полным ассортиментом вы можете ознакомиться на нашем сайте: example.com."
}

def normalize_text(text):
    text = text.lower()
    # Убираем знаки препинания, оставляем только буквы и пробелы
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def get_answer(user_text):
    text = normalize_text(user_text)
    
    # Ищем совпадения по каждой категории
    results = []
    for category, keywords in CATEGORIES.items():
        best_score = 0
        for kw in keywords:
            # Сравниваем весь текст с ключевым словом (fuzzy)
            score = fuzz.partial_ratio(text, kw)
            if score > best_score:
                best_score = score
        
        if best_score >= 80:  # Порог 80%
            results.append((category, best_score))
    
    # Сортируем по убыванию процента
    results.sort(key=lambda x: x[1], reverse=True)
    
    print(f"   [DEBUG] Вы написали: '{user_text}'")
    print(f"   [DEBUG] Найдены категории (процент): {[(r[0], r[1]) for r in results]}\n")

    if not results:
        return "Не понял вопрос. Попробуйте переформулировать или напишите /help."
    
    # Если одна категория
    if len(results) == 1:
        return ANSWERS[results[0][0]]
    
    # Если несколько — выдаем до 3-х
    response = "По вашему запросу найдено несколько тем:\n\n"
    count = 0
    for cat, score in results:
        if count >= 3:
            response += "... и другие темы. Уточните, пожалуйста.\n"
            break
        response += f"🔹 *{cat.capitalize()}:*\n{ANSWERS[cat]}\n\n"
        count += 1
    return response

if __name__ == "__main__":
    test_questions = [
        "скока стоит",
        "Че по цене брат?",
        "Сколько стоит, куда доставляете, что по ассортименту?",
        "Дурова ебать"
    ]
    for q in test_questions:
        print(f"Клиент: {q}")
        print(f"Бот: {get_answer(q)}\n")