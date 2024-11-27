import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password_to_check):
        hashed_input = self._hash_password(password_to_check)
        return self.password == hashed_input

    def is_adult(age):
        return age >= 18


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
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
                print(f"Приветствуем вас, {nickname}! Вы вошли в систему.")
                break
        else:
            print("Неправильное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        print(f"Учетная запись {nickname} была создана успешно.")

    def log_out(self):
        if self.current_user:
            self.current_user = None
            print("Вы вышли из системы.")
        else:
            print("Вы не авторизованы.")

    def add(self, *videos):
        for video in videos:
            if isinstance(video, Video) and video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Видео '{video.title}' было добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_word):
        results = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                results.append(video.title)
        return results

    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == video_title), None)

        if not found_video:
            print(f"Видео с названием '{video_title}' не найдено.")
            return

        if found_video.adult_mode and not User.is_adult(self.current_user.age):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Воспроизведение видео '{found_video.title}' началось с {found_video.time_now} секунды.")

        for i in range(found_video.time_now + 1, found_video.duration + 1):
            sleep(1)
            print(i)

        found_video.time_now = 0
        print("Конец видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года']
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
print(ur.watch_video)