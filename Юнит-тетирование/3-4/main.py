def is_correct_mobile_phone_number_ru(number):

    number = number.replace(' ', '').replace('-', '')

    # Проверяем корректность номера телефона
    if number.startswith('8') or number.startswith('+7'):
        if len(number) == 11 and number[1:4].isdigit() and number[4:].isdigit():
            return True
        elif len(number) == 12 and number[2:5].isdigit() and number[5:].isdigit():
            return True
    elif number.startswith('+7(') and ')' in number:
        code_end = number.index(')')
        if code_end == 6 and number[3:6].isdigit() and number[7:].isdigit():
            return True
    return False
def test_is_correct_mobile_phone_number_ru():
    test_cases = ["+7(900)2238560", "+7 987 223-85-60", "8(987)2238560", "8 987 2238560"]
    for case in test_cases:
        result = is_correct_mobile_phone_number_ru(case)
        if result:
            print("YES")
        else:
            print("NO")
test_is_correct_mobile_phone_number_ru()