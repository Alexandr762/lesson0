my_dict = {"Vasya" : 1994, "Kolya": 2001, "Dima" : 2017}
print(my_dict)
print(my_dict["Dima"])
print(my_dict.get("Nastya"))
my_dict.update({"Anna": 1900,
               "Oleg" : 1997})
n = my_dict.pop("Vasya")
print(n)
print(my_dict)

my_set = {1,1,3,4,5,6,7,1,1,2,4,4,"tree","dog"}
print(my_set)
my_set.update({8,9})
print(my_set)
my_set.remove(4)
print(my_set)