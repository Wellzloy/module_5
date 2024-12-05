class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        names = ['Tom', 'Ivan', 'Anton']
        if name in names:
            self.__name = name
        else:
            print("Недопустимое имя")

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.age = 56  # Недопустимый возраст
tom.age = 25
tom.name = 'Ivan'  # Недопустимое имя
tom.age = 12
tom.print_person()  # Имя: Tom  Возраст: 25
