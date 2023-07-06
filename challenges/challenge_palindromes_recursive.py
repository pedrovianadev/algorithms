"""Linter"""


def is_palindrome_recursive(word, l_index, h_index):
    """Linter"""
    if not word or word[l_index] != word[h_index]:
        return False

    if l_index >= h_index:
        return True

    return is_palindrome_recursive(word, l_index + 1, h_index-1)
