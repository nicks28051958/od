# Файл test_palindrome.py
import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        # Тест для строки, являющейся палиндромом
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"), "Ожидается True для строки-палиндрома")

    def test_non_palindrome(self):
        # Тест для строки, не являющейся палиндромом
        self.assertFalse(is_palindrome("Привет, мир"), "Ожидается False для непалиндрома")

    def test_empty_string(self):
        # Тест для пустой строки
        self.assertTrue(is_palindrome(""), "Ожидается True для пустой строки")

    def test_mixed_case_palindrome(self):
        # Тест для палиндрома с разными регистрами
        self.assertTrue(is_palindrome("A man a plan a canal Panama"),
                        "Ожидается True для строки-палиндрома с разными регистрами")

    def test_single_character(self):
        # Тест для строки, состоящей из одного символа
        self.assertTrue(is_palindrome("а"), "Ожидается True для строки из одного символа")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
