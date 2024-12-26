def add_everything_up(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return f"{a}{b}"

    try:
        result = a + b
        return result
    except TypeError as e:
        return f"{a}{b}"
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))