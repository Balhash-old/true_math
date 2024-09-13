from math import inf


def divide_(first, second):
    try:
        result = first / second
    except ZeroDivisionError as zde:
        result = inf

    return result

