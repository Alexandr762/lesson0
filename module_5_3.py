class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            return f'Такого этажа нет'
        else:
            return f'Вы находитесь на этаже {new_floor} в доме {self.name}'

    def __len__(self):
        return self.C

    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floors}'

    def __eq__(self, other):
        return self.name == other.name or self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self


    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return f'House(floors={self.number_of_floors})'



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 + 10
print(h1)

print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 < h2)
print(h1 != h2)
print(h1 >= h2)
print(h1 <= h2)
