  # Параметры
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params('cnhjrf', False)
print_params(10, 'строка', False)
print_params(b = 25) # Работает
print_params(c = [1,2,3])# Работает

 # Распаковка
values_list = [1, 'строка', True]
values_dict = {'a' : 23, 'b' : 'слово', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

# .Распаковка + отдельные параметры
values_list_2 = [1, 'string']
print_params(*values_list_2)# Работает