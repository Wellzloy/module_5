class House:

    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        self.new_floor = new_floor
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)

print(h1 == h2)
