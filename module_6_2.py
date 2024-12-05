class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'silver', 'blue']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def model(self):
        return f"Модель: {self.__model}"

    def horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.model}\n{self.horsepower}\n{self.color}\nВладелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in map(lambda x: x.lower(), self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

    def passengers_limit(self):
        return f"Пассажировместимость: {self.__PASSENGERS_LIMIT}"
sedan = Sedan("Иван Иванов", "Toyota Camry", 200, "черный")

print(sedan.model)
print(sedan.horsepower)
print(sedan.color)
sedan.print_info()

sedan.set_color('красный')
print(sedan.color)

sedan.set_color('фиолетовый')

print(sedan.passengers_limit())

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
