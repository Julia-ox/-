class StringUtils:
    @staticmethod
    def reverse_string(s: str) -> str:
        """Возвращает перевернутую строку."""
        if s is None:
            return None
        return s[::-1]

    @staticmethod
    def to_uppercase(s: str) -> str:
        """Возвращает строку в верхнем регистре."""
        if s is None:
            return None
        return s.upper()

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Проверяет, является ли строка палиндромом."""
        if s is None:
            return False
        return s == s[::-1]

    @staticmethod
    def count_vowels(s: str) -> int:
        """Считает количество гласных в строке."""
        if s is None:
            return 0
        return sum(1 for char in s.lower() if char in 'aeiou')