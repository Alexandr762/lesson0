def calculate_structure_sum(*args):
    total_sum = 0

    for i in args:
        if isinstance(i, int):
            total_sum += i
        elif isinstance(i, float):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        try:
            sum_of_nested_items = calculate_structure_sum(*i.values())
            total_sum += sum_of_nested_items
        except AttributeError:
            pass

    return total_sum

data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = calculate_structure_sum(*data_structure)
print(result)