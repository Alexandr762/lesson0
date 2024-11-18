class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            return f'Такого этажа нет'
        else:
            return f'Вы находитесь на этаже {new_floor} в доме {self.name}'

h1 = House('dog', 25)
h2 = House('Вишенка', 10)
print(h1.go_to(56))
print(h2.go_to(4))
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
