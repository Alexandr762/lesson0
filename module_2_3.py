my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []

if my_list[0] > 0:
    positive_numbers.append(my_list[0])
    i = 1

while i < len(my_list) and my_list[i] >= 0:
    positive_numbers.append(my_list[i])
    i = i + 1

print(positive_numbers)
