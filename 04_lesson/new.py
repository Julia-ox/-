import pytest
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для метода capitalize
@pytest.mark.parametrize('input_string, expected_result', [
    ("test", "Test"),
    ("", ""),
    ("123", "123"),
    ("тест", "Тест")
])
def test_capitalize(string_utils, input_string, expected_result):
    assert expected_result == string_utils.capitalize(input_string)


# Тесты для метода trim
@pytest.mark.parametrize('input_string, expected_result', [
    ("  test", "test"),
    ("  ", ""),
    ("test  ", "test  "),
    ("  test  ", "test  ")
])
def test_trim(string_utils, input_string, expected_result):
    assert string_utils.trim(input_string) == expected_result

# Тесты для метода to_list
@pytest.mark.parametrize('input_string, delimiter, expected_result', [
    ("a,b,c", ",", ["a", "b", "c"]),
    ("", "", []),
    ("1,2,3", ",", ["1", "2", "3"]),
    ("1 2 3", " ", ["1", "2", "3"])
])
def test_to_list(string_utils, input_string, delimiter, expected_result):
    assert string_utils.to_list(input_string, delimiter) == expected_result

# Тесты для метода contains
@pytest.mark.parametrize('input_string, substring, expected_result', [
    ("test", "es", True),
    ("test", "xyz", False),
    ("", "", True),
    ("123", "2", True)
])
def test_contains(string_utils, input_string, substring, expected_result):
    assert string_utils.contains(input_string, substring) is expected_result

# Тесты для метода delete_symbol
@pytest.mark.parametrize('input_string, symbol, expected_result', [
    ("test", "t", "es"),
    ("test", "x", "test"),
    ("", "t", ""),
    ("123", "2", "13")
])
def test_delete_symbol(string_utils, input_string, symbol, expected_result):
    assert string_utils.delete_symbol(input_string, symbol) == expected_result

# Тесты для метода starts_with
@pytest.mark.parametrize('input_string, prefix, expected_result', [
    ("test", "t", True),
    ("test", "e", False),
    ("", "t", False),
    ("123", "1", True)
])
def test_starts_with(string_utils, input_string, prefix, expected_result):
    assert string_utils.starts_with(input_string, prefix) is expected_result

# Тесты для метода end_with
@pytest.mark.parametrize('input_string, suffix, expected_result', [
    ("test", "t", True),
    ("test", "e", False),
    ("", "t", False),
    ("123", "3", True)
])
def test_end_with(string_utils, input_string, suffix, expected_result):
    assert string_utils.end_with(input_string, suffix) is expected_result

# Тесты для метода is_empty
@pytest.mark.parametrize('input_string, expected_result', [
    ("", True),
    (" ", True),
    ("test", False),
    ("123", False)
])
def test_is_empty(string_utils, input_string, expected_result):
    assert string_utils.is_empty(input_string) is expected_result

# Тесты для метода list_to_string
@pytest.mark.parametrize('input_list, delimiter, expected_result', [
    (["a", "b", "c"], ", ", "a, b, c"),
    ([], "", ""),
    ([1, 2, 3], ", ", "1, 2, 3"),
    (["a", "b", "c"], "-", "a-b-c")
])
def test_list_to_string(string_utils, input_list, delimiter, expected_result):
    assert string_utils.list_to_string(input_list, delimiter) == expected_result