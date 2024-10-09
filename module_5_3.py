class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= 1 or new_floor >= self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Задача "Нужно больше этажей":
#
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
#
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __radd__(self, other):
        self.number_of_floors += other
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self


    def __eq__(self, other):
        return self.number_of_floors == other


    def __lt__(self, other):
        return self.number_of_floors < other


    def __le__(self, other):
        return self.number_of_floors <= other


    def __gt__(self, other):
        return self.number_of_floors > other


    def __ge__(self, other):
        return self.number_of_floors >= other


    def __ne__(self, other):
        return self.number_of_floors != other



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
