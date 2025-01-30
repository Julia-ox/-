import pytest
from StringUtils import StringUtils

class TestStringUtils:

    # Тесты для метода reverse_string
    @pytest.mark.positive_test  # Позитивные тесты для метода reverse_string
    @pytest.mark.parametrize('string, result', [
        ("Тест", "тсеТ"),
        ("123", "321"),
        ("04 апреля 2023", "3202 яревпа 40"),
        ("", ""),
        (" ", " ")
    ])
    def test_reverse_string_positive(self, string, result):
        res = StringUtils.reverse_string(string)
        assert res == result

    @pytest.mark.negative_test  # Негативные тесты для метода reverse_string
    @pytest.mark.parametrize('string', [
        None
    ])
    def test_reverse_string_negative(self, string):
        res = StringUtils.reverse_string(string)
        assert res is None

    # Тесты для метода to_uppercase
    @pytest.mark.positive_test  # Позитивные тесты для метода to_uppercase
    @pytest.mark.parametrize('string, result', [
        ("тест", "ТЕСТ"),
        ("123", "123"),
        ("04 апреля 2023", "04 АПРЕЛЯ 2023"),
        ("", ""),
        (" ", " ")
    ])
    def test_to_uppercase_positive(self, string, result):
        res = StringUtils.to_uppercase(string)
        assert res == result

    @pytest.mark.negative_test  # Негативные тесты для метода to_uppercase
    @pytest.mark.parametrize('string', [
        None
    ])
    def test_to_uppercase_negative(self, string):
        res = StringUtils.to_uppercase(string)
        assert res is None

    # Тесты для метода is_palindrome
    @pytest.mark.positive_test  # Позитивные тесты для метода is_palindrome
    @pytest.mark.parametrize('string, result', [
        ("топот", True),
        ("12321", True),
        ("", True),
        (" ", False)
    ])
    def test_is_palindrome_positive(self, string, result):
        res = StringUtils.is_palindrome(string)
        assert res == result

    @pytest.mark.negative_test  # Негативные тесты для метода is_palindrome
    @pytest.mark.parametrize('string', [
        None,
        ("тест", False)
    ])
    def test_is_palindrome_negative(self, string):
        res = StringUtils.is_palindrome(string)
        if string is None:
            assert res is False
        else:
            assert res is False  # Поскольку "тест" не палиндром

    # Тесты для метода count_vowels
    @pytest.mark.positive_test  # Позитивные тесты для метода count_vowels
    @pytest.mark.parametrize('string, result', [
        ("тест", 1),
        ("123", 0),
        ("04 апреля 2023", 5),
        ("", 0),
        (" ", 0)
    ])
    def test_count_vowels_positive(self, string, result):
        res = StringUtils.count_vowels(string)
        assert res == result

    @pytest.mark.negative_test  # Негативные тесты для метода count_vowels
    @pytest.mark.parametrize('string', [
        None
    ])
    def test_count_vowels_negative(self, string):
        res = StringUtils.count_vowels(string)
        assert res == 0  # Пустая строка, возвращаем 0