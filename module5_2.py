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
        return self.number_of_floors
    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floors}'
h1 = House('dog', 25)
h2 = House('Вишенка', 10)
print(str(h2))
print(str(h1))
print(len(h2))
print(len(h1))