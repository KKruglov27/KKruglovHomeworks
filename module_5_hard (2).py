import time
from colorama import Fore, Style


class User:

    def __init__(self, nickname, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, tittle: str, duration: int, time_now=0, adult_mode=False):
        self.tittle = tittle
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube():

    users = []
    videos = []
    current_user = None

    def register(self, nickname, password, age: int):
        self.user = [nickname, password, age]
        for i in self.users:
            if i[0] == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        else:
            self.users.append(self.user)
            self.logistr = 1
            self.login(nickname, password)
            self.logistr = 2

    #Проверка логина или пароля поочередно.
    def login(self, login, password):
        num = 0
        for i in self.users:
            if i[0] != login:
                num += 1
                continue
            else:
                if i[1] != password:
                    print(f"Введен неверный пароль. {login}, введите верный пароль. ")
                    return
        if num == len(self.users):
            print(f'Такого пользователя "{login}" нет.')
            num = 0
            return
        else:
            self.current_user = login
            if self.logistr == 1:
                print(f"Пользователь {login} зарегистрирован, добро пожаловать.")
            else:
                print(f"Пользователь {login} авторизован")
            print(f"{self.current_user} в сети")

    # Стандартная проверка из задачи
    # def login(self, login, password):
    #    for i in self.users:
    #        self.verif = True
    #        if i[0] != login or i[1] != password:
    #            continue
    #        else:
    #            self.verif = False
    #            self.current_user = login
    #            if self.logistr == 1:
    #                print(f"Пользователь {login} зарегистрирован, добро пожаловать.")  # Проверка без пароля.
    #            else:
    #                print(f"Пользователь {login} авторизован")
    #            print(f"{self.current_user} в сети")
    #            return
    #    if self.verif:
    #        print(f'Такого пользователя "{login}" нет.')
    #        return

    def log_out(self, nickname):
        if self.current_user != nickname:
            return
        else:
            if self.current_user == nickname:
                self.current_user = None
                print(f"{nickname} не в сети")
                return

    def add_video(self, *args):
        for i in args:
            self.video = [i.tittle, i.duration, i.time_now, i.adult_mode]
            verif = True
            for j in self.videos:
                if i.tittle == j[0]:
                    print(f'Видео с идентичным названием:"{j[0]}" уже существует.')
                    verif = False
            if verif == False:
                continue
            self.videos.append(self.video)
            print(f'Видео: "{i.tittle}" загружено успешно!')
        print()
        num1 = 1
        print("Список загруженных видео:")
        for i in self.videos:
            print('#', num1, i[0])
            num1 += 1
        print()

    def get_videos(self, video_search):
        self.found_videos = []
        video_search = video_search.lower()
        search = list(video_search.split(" "))
        for i in self.videos:
            i_low = (i[0].lower())
            for word_vid in search:
                if word_vid in i_low and i not in self.found_videos:
                    self.found_videos.append(i)
        if self.found_videos == []:
            print(f'По поиску: "{video_search}" результаты отсутствуют.')
        else:
            print(f'Поиск: "{video_search}" обладает следующими результатами:')
            return self.found_videos

    def watch_video(self, play_video):
        self.play_video = play_video
        print(f'{Fore.YELLOW}Воспроизведение видео:{Style.RESET_ALL} "{play_video}":')
        for i in self.videos:
            if i[0] == play_video:
                if self.current_user == None:
                    print(f"Войдите в аккаунт, чтобы смотреть видео.")
                    return
        else:
            for i in self.users:
                if (i[0]) == self.current_user:
                    for check in self.videos:
                        if check[0] != play_video:
                            continue
                        else:
                            if check[3] is True and i[2] >= 18 or check[3] is False:
                                duration = check[1]
                                print(f"Начало видео🔴: {play_video}")
                                for sec in range(duration):
                                    print(f'{sec} *', end=' '), time.sleep(1)
                                print(f'Конец видео')
                                return
                            else:
                                print(f"Вам нет 18 лет для просмотра"f"'{play_video}', "
                                      f"пожалуйста, покиньте страницу.")
                                return
        print(f'{Fore.RED}Ошибка воспроизведения: {Style.RESET_ALL}"{play_video}"')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 22, adult_mode=True)
v4 = Video('Как перейти в "Customize"?', 5)
ur.add_video(v1, v2, v3, v4)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print()
ur.watch_video('Как перейти в "Customize"?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Как перейти в "Customize"?')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF',25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
(print(f"Текущий пользователь: {ur.current_user}"))
ur.login('вася_пупкин', 'lolkekcheburek')
ur.login('vasya_pupkin', 'LOLKEKCHEBUREK')
ur.login('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
(print(f"Текущий пользователь: {ur.current_user}"))
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_out("vasya_pupkin")
(print(f"Текущий пользователь: {ur.current_user}"))
ur.watch_video('Лучший язык программирования 2024 года')
