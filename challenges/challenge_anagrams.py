"""
Linter
"""


def sort(w, s, e):
    """
    Linter
    """
    if s < e:
        par = spread(w, s, e)
        sort(w, s, par - 1)
        sort(w, par + 1, e)


def spread(w, s, e):
    """
    Linter
    """
    pivot = w[e]
    limiter = s - 1

    for index in range(s, e):
        if w[index] <= pivot:
            limiter = limiter + 1
            w[index], w[limiter] = w[limiter], w[index]

    w[limiter + 1], w[e] = w[e], w[limiter + 1]

    return limiter + 1


def order(w):
    """
    Linter
    """
    letters = list(w)

    sort(letters, 0, len(letters)-1)
    sort_letters = "".join(letters)

    return sort_letters


def is_anagram(f_string, s_string):
    """
    Linter
    """
    if f_string == '' and s_string == '':
        return ('', '', False)
    first = f_string.lower()
    second = s_string.lower()

    first_word = order(first)
    second_word = order(second)
    check = first_word == second_word

    return (first_word, second_word, check)
