import hashlib


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password_hash = self.hash_password(password)
        self.age = age


    def hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)


    def check_password(self, password):
        return  self.password_hash == self.hash_password(password)



class Video:

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Пользователь {nickname} успешно вошел')
                return True

        print('Неверный логин или пароль')
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
                




ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
h1 = User('well', 123, 34)

# ur.log_in('well', 123)
# Добавление видео
# ur.add(v1, v2)
# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')

# def add_user(self, user):
#     self.users.append(user)
#     self.current_user = user
#     return self
# add_user — метод добавления пользователя в список users.

class UrTube:
    users = []

    def __init__(self, nickname, password):
        self.current_user = None
        self.age = None
        self.nickname = nickname
        self.password = password

    def register(self, nickname, password, age):
        if nickname in users:

    def log_in()