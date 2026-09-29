from string_utils import StringUtils


def test_positive_capitalize_simple_word():
    """Проверяем обычную строку из одного слова"""
    utils = StringUtils()
    result = utils.capitalize("cat")
    assert result == "Cat"


def test_positive_capitalize_several_words():
    """Проверяем предложение, где первое слово начинается с маленькой буквы"""
    utils = StringUtils()
    result = utils.capitalize("my dog")
    assert result == "My dog"


def test_positive_capitalize_large_letter():
    """Проверяем, первая буква уже заглавная"""
    utils = StringUtils()
    result = utils.capitalize("Dog")
    assert result == "Dog"


def test_positive_capitalize_numbers():
    """Проверяем, если введены цифры"""
    utils = StringUtils()
    result = utils.capitalize("123")
    assert result == "123"


def test_negative_capitalize_unfilled():
    """Проверяем, если поле пустое"""
    utils = StringUtils()
    result = utils.capitalize("")
    assert result == ""


def test_negative_capitalize_space():
    """Проверяем, если введен пробел"""
    utils = StringUtils()
    result = utils.capitalize(" ")
    assert result == " "


def test_positive_trim_space():
    """Проверяем удаление пробелов в начале строки"""
    utils = StringUtils()
    result = utils.trim("   mops")
    assert result == "mops"


def test_positive_trim_no_space():
    """Проверяем строку без пробелов"""
    utils = StringUtils()
    result = utils.trim("mops")
    assert result == "mops"


def test_positive_trim_mix_space():
    """Проверяем удаление пробелов в начале строки"""
    """но сохранение в середине и конце"""
    utils = StringUtils()
    result = utils.trim("  mops mops  ")
    assert result == "mops mops  "


def test_negative_trim_unfilled():
    """Проверяем пустую строку"""
    utils = StringUtils()
    result = utils.trim("")
    assert result == ""


def test_positive_contains_symbol_present_middle():
    """Символ есть в середине строки"""
    utils = StringUtils()
    result = utils.contains("Dog", "o")
    assert result is True


def test_positive_contains_symbol_at_start():
    """Символ стоит в самом начале"""
    utils = StringUtils()
    result = utils.contains("Apple", "A")
    assert result is True


def test_positive_contains_symbol_at_end():
    """Символ находится в конце строки"""
    utils = StringUtils()
    result = utils.contains("Cat", "t")  # 'o' есть в конце
    assert result is True


def test_negative_contains_symbol_missing():
    """Символа в строке нет — должен вернуться False"""
    utils = StringUtils()
    result = utils.contains("Dog", "z")
    assert result is False


def test_negative_contains_in_empty_string():
    """Строка пустая, ищем любой символ — должен вернуться False"""
    utils = StringUtils()
    result = utils.contains("", "a")
    assert result is False


def test_positive_delete_symbol_middle():
    """Удаление подстроки в середине слова"""
    utils = StringUtils()
    result = utils.delete_symbol("MyPet", "Pe")
    assert result == "Myt"


def test_positive_delete_symbol_start():
    """Удаление подстроки в начале"""
    utils = StringUtils()
    result = utils.delete_symbol("CatDog", "C")
    assert result == "atDog"


def test_positive_delete_symbol_end():
    """Удаление подстроки в конце"""
    utils = StringUtils()
    result = utils.delete_symbol("MyName", "me")
    assert result == "MyNa"


def test_negative_delete_symbol_not_found():
    """Символ не найден — строка должна остаться неизменной"""
    utils = StringUtils()
    result = utils.delete_symbol("Dog", "Z")
    assert result == "Dog"


def test_negative_delete_empty_symbol():
    """Попытка удалить пустую строку"""
    utils = StringUtils()
    result = utils.delete_symbol("Cat", "")
    assert result == "Cat"
