# Файл palindrome.py
def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом.

    Аргументы:
        s (str): строка для проверки.

    Возвращает:
        bool: True, если строка является палиндромом, иначе False.
    """
    # Преобразуем строку: удаляем пробелы и приводим к нижнему регистру
    normalized_str = ''.join(s.lower().split())
    # Сравниваем строку с её обратной версией
    return normalized_str == normalized_str[::-1]


# Запрос ввода от пользователя
if __name__ == "__main__":
    input_text = input("Введите строку для проверки: ")
    if is_palindrome(input_text):
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")
