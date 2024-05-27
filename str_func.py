import string

def str_upper(text):
    """Функция перевода текста в верхний регистр"""
    return text.upper()


def str_title(text):
    """Функция перевода в заглавные первые буквы каждого слова в строке"""
    return string.capwords(text)
