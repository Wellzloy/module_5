class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        area = self.width * self.length
        return area

    def perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter


# h1 = Rectangle(15, 90)
# area = h1.area()
# print(area)
# perimeter = h1.perimeter()
# print(perimeter)
# Создайте класс BankAccount, который представляет банковский счет.
# Определите в этом классе атрибуты account_number и balance, которые представляют номер счета и баланс.
# Через параметры конструктора передайте этим атрибутам начальные значения.
#
# Также в классе определите метод add, который принимает некоторую сумму и
# добавляет ее на баланс счета. И определите метод withdraw, который принимает некоторую сумму и
# снимает ее с баланса. При этом с баланса нельзя снять больше, чем имеется.
# Если на балансе недостаточно средств, то пользователю должно выводиться соответствующее сообщение.

class BankAccoun:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = float(balance)


    def add(self):
        summ = float(input('Введите сумму для зачисления на счет: '))
        self.balance = self.balance + summ
        return self.balance

    def withdraw(self):
        pass


h1 = BankAccoun(772123, 19000)
print(h1.add())
