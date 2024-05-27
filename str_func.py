import string

def str_upper(text):
    """Функция перевода текста в верхний регистр"""

    result = text.upper()
    return result


def str_title(text):
    """Функция перевода в заглавные первые буквы каждого слова в строке"""

    result = string.capwords(text)
    return result
