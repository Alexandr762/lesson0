immutable_var = 1, 5, "car", "cat"
print(immutable_var)
# immutable_var[1] = 10  ошибка ,потому что кортеж не поддерживает обращение по элементам
mutable_list = ["Петя", "Рома", "Коля"]
mutable_list[1] = "Bill"
print(mutable_list)