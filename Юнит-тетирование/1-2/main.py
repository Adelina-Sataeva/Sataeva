def is_palindrome(data):
    return data == data[::-1]

def test_is_palindrome():
    test_cases = ["radar", "level", "python", "madam"]

    for test_case in test_cases:
        if is_palindrome(test_case):
            print("YES")
        else:
            print("NO")


test_is_palindrome()

def check_palindrome():
    input_str = input("Введите строку: ")
    if is_palindrome(input_str):
        print("YES")
    else:
        print("NO")

# Вызов тестирующей программы
test_is_palindrome()

# Проверка строки на палиндром
check_palindrome()