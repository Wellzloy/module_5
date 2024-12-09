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
    while True:
        choice = int(input('Приветствую! Выбирите действие: \n1 - Вход \n2 - Регистрация \n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in datbase.data:
                if password == datbase.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print('Пароли не совпадают, попробуйте еще раз.')
                continue
            datbase.add_user(user.username, user.password)
