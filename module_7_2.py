def custom_write(file_name, strings):
    with open(file_name, mode='w', encoding='utf-8') as file:
        strings_positions = {}

        for i, string in enumerate(strings, start=1):
            position = file.tell()

            file.write(string + '\n')

            strings_positions[(i, position)] = string

    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)