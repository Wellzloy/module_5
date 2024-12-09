class Database:

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, passwrd_confirm):
        self.username = username
        if password == passwrd_confirm:
            self.password = password

if __name__ == '__main__':
    datbase = Database()
    user = User(input('Введите логин: '), input('Введите пароль: '), input('Повторите пароль: '))