import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        # Хеширование пароля с использованием алгоритма SHA256
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошел.")
                return True

        print("Неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return False

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        return True

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print("Вы вышли из аккаунта.")
        else:
            print("Нет активного пользователя.")

    def add(self, *videos):
        """Добавляет новые видео в список, если они еще не существуют."""
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                continue  # Пропускаем видео, если оно уже есть
            self.videos.append(video)

    def get_videos(self, search_word):
        """Возвращает список названий всех видео, содержащих поисковое слово."""
        result = []
        search_word = search_word.lower()  # Приводим к нижнему регистру
        for video in self.videos:
            if search_word in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        """Воспроизведение видео с учётом возрастных ограничений и состояния сессии."""
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == title), None)
        if found_video is None:
            print(f"Видео '{title}' не найдено.")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(found_video.time_now + 1, found_video.duration + 1):
            print(second)
            sleep(1)  # Имитация задержки между кадрами
        print("Конец видео")
        found_video.time_now = 0  # Сброс времени после окончания просмотра


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


# Добавление видео

ur.add(v1, v2)


# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)


# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
