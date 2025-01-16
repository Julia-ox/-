import pytest
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize(string_utils):
    assert string_utils.capitalize("test") == "Test"
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("123") == "123"
    assert string_utils.capitalize("тест") == "Тест"

def test_trim(string_utils):
    assert string_utils.trim("  test") == "test"
    assert string_utils.trim("  ") == ""
    assert string_utils.trim("test  ") == "test  "
    assert string_utils.trim("  test  ") == "test  "

def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c") == ["a", "b", "c"]
    assert string_utils.to_list("") == []
    assert string_utils.to_list("1,2,3", delimiter=",") == ["1", "2", "3"]
    assert string_utils.to_list("1 2 3", delimiter=" ") == ["1", "2", "3"]

def test_contains(string_utils):
    assert string_utils.contains("test", "es") is True
    assert string_utils.contains("test", "xyz") is False
    assert string_utils.contains("", "") is True
    assert string_utils.contains("123", "2") is True

def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("test", "t") == "es"
    assert string_utils.delete_symbol("test", "x") == "test"
    assert string_utils.delete_symbol("", "t") == ""
    assert string_utils.delete_symbol("123", "2") == "13"

def test_starts_with(string_utils):
    assert string_utils.starts_with("test", "t") is True
    assert string_utils.starts_with("test", "e") is False
    assert string_utils.starts_with("", "t") is False
    assert string_utils.starts_with("123", "1") is True

def test_end_with(string_utils):
    assert string_utils.end_with("test", "t") is True
    assert string_utils.end_with("test", "e") is False
    assert string_utils.end_with("", "t") is False
    assert string_utils.end_with("123", "3") is True

def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("test") is False
    assert string_utils.is_empty("123") is False

def test_list_to_string(string_utils):
    assert string_utils.list_to_string(["a", "b", "c"]) == "a, b, c"
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert string_utils.list_to_string(["a", "b", "c"], delimiter="-") == "a-b-c"