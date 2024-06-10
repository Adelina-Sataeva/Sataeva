import re
def strip_punctuation_ru(data):
    # Удаление знаков препинания с помощью регулярного выражения
    return re.sub(r'[^\w\s]', '', data)
def test_strip_punctuation_ru():
    tests = [
        ("Привет, всем!", "Привет всем"),
        ("Привет как дела?", "Привет как дела"),
        ("Спасибо за участие,получите награду!", "Спасибо за участие получите награду"),
        ("8-999-360-40-50", "89993604050"),
    ]
    for test_input, expected_result in tests:
        result = strip_punctuation_ru(test_input)
        if result == expected_result:
            print("YES")
        else:
            print("NO")

# Запуск тестирования
test_strip_punctuation_ru()