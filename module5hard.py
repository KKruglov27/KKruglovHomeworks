from colorama import Fore, Style
import time


class User:

    def __init__(self, nickname, password, gender, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.gender = gender


class Video:

    def __init__(self, tittle: str, duration: int, time_now=0, adult_mode=False):
        self.tittle = tittle
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube():

    users = []
    videos = []
    users_verif = ()
    users_age = ()
    current_user = None


    def login(self, login, password):
        users_num = len(self.users_verif)
        num = 0
        for i in self.users_verif:
            for key, cod in i.items():
                if key != login:
                    num += 1
                else:
                    if cod != password:
                        print(f'{Fore.LIGHTWHITE_EX}{login}: {Style.RESET_ALL}'
                              f'{Fore.YELLOW}введен неверный пароль{Style.RESET_ALL}')
                        return
                if num == users_num:
                    print(f'{Fore.YELLOW}Пользователя {Style.RESET_ALL}{Fore.LIGHTWHITE_EX}{login}{Style.RESET_ALL}'
                          f'{Fore.YELLOW} не существует{Style.RESET_ALL}')
                    num = 0
                    return
                if num != users_num:
                    continue
        self.current_user = login
        print(f"Пользователь {Fore.LIGHTWHITE_EX}{login}{Style.RESET_ALL} авторизован")
        print(f"{Fore.LIGHTWHITE_EX}{self.current_user}{Fore.GREEN} в сети{Style.RESET_ALL}")


    def register(self, nickname, password, gender, age: int):
        self.user = []
        self.data = {}
        for lock1 in self.users:
            for lock2 in lock1:
                if isinstance(lock2, dict):
                    for login, kod in lock2.items():
                        if login == nickname:
                            print(f'{Fore.YELLOW}Пользователь {Fore.LIGHTWHITE_EX}{nickname}{Style.RESET_ALL} '
                                  f'{Fore.YELLOW}уже существует.{Style.RESET_ALL}')
                            return
        else:
            self.data[nickname] = password
            self.users_verif = list(self.users_verif)
            self.users_verif.append(self.data)
            self.users_verif = tuple(self.users_verif)
            self.users_age = list(self.users_age)
            self.users_age.append([nickname, age])
            self.users_age = tuple(self.users_age)
            self.user.append([self.data, gender, age])
            self.users.append(*self.user)
            print(f"{Fore.GREEN}Пользователь{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{nickname}{Style.RESET_ALL} "
                  f"{Fore.GREEN}зарегистрирован, добро пожаловать!{Style.RESET_ALL}")
            self.current_user = nickname
            print(f"{Fore.LIGHTWHITE_EX}{self.current_user}{Fore.GREEN} в сети{Style.RESET_ALL}")


    def log_out(self, nickname):
        if self.current_user != nickname:
            return
        else:
            if self.current_user == nickname:
                self.current_user = None
                print(f"{Fore.LIGHTWHITE_EX}{nickname}{Style.RESET_ALL} не в сети")
                return


    def add_video(self, *args):
        for elem1 in args:
            verif = True
            for elem2 in self.videos:
                if elem1.tittle == elem2[0]:
                    time.sleep(1)
                    print(f'{Fore.RED}Видео с идентичным названием: {Fore.LIGHTWHITE_EX}"{elem2[0]}"{Style.RESET_ALL}'
                          f'{Fore.RED} уже существует.{Style.RESET_ALL}')
                    time.sleep(1)
                    verif = False
            if verif == False:
                continue
            self.videos.append([elem1.tittle, elem1.duration, elem1.time_now, elem1.adult_mode])
            print(f'{Fore.GREEN}Видео:{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}"{elem1.tittle}"{Style.RESET_ALL}'
                        f'{Fore.GREEN} загружено успешно!{Style.RESET_ALL}')
            time.sleep(1)

    def get_videos(self, video_search):
        self.found_videos = []
        low_word = video_search.lower()
        search = list(low_word.split(" "))
        for videos_list in self.videos:
            if isinstance(videos_list, list):
                word_list = (videos_list[0].lower())
                for word in search:
                    if word in word_list:
                        if videos_list[0] not in self.found_videos:
                            self.found_videos.append(videos_list[0])
        if self.found_videos == []:
            time.sleep(1)
            print(f'{Fore.LIGHTWHITE_EX}По поиску: "{video_search}" результаты отсутствуют :({Style.RESET_ALL}')
            time.sleep(1)
        else:
            time.sleep(1)
            print(f'{Fore.LIGHTWHITE_EX}Поиск: "{video_search}" обладает следующими результатами:{Style.RESET_ALL}')
            time.sleep(0.5)
            return self.found_videos



    def watch_video(self, play_video):
        self.play_video = play_video
        if self.current_user == None:
            print(f"{Fore.YELLOW}Войдите в аккаунт, чтобы смотреть видео.{Style.RESET_ALL}")
            time.sleep(2)
            return
        else:
            for i in self.users_age:
               if (i[0]) == self.current_user:
                for chek in self.videos:
                    if chek[0] != self.play_video:
                        continue
                    else:
                        if chek[3] == True:
                            if i[1] >= 18:
                                duration = chek[1]
                                print(f"{Fore.BLUE}Воспроизведение видео{Style.RESET_ALL} 🔴: {self.play_video}")
                                for sec in range(duration):
                                    print(f'{Fore.LIGHTWHITE_EX}{sec}{Style.RESET_ALL}'
                                        f'{Fore.MAGENTA} *{Style.RESET_ALL}', end=' '), time.sleep(1)
                                print(f'{Fore.BLUE}Видео закончилось{Style.RESET_ALL}')
                                time.sleep(1)
                            else:
                                print(f"{Fore.LIGHTRED_EX}Вам нет 18 лет для просмотра {Style.RESET_ALL}"
                                      f"{Fore.LIGHTWHITE_EX}'{self.play_video}'{Style.RESET_ALL}"
                                      f"{Fore.LIGHTRED_EX} пожалуйста, покиньте страницу.{Style.RESET_ALL}")
                                time.sleep(2)
                                return




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


ur.add_video(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 'male', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 'male', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 'male', 55)
(print(f"{Fore.LIGHTWHITE_EX}Текущий пользователь: {Style.RESET_ALL}{Fore.GREEN}{ur.current_user}{Style.RESET_ALL}"))

ur.watch_video('Лучший язык программирования 2024 года!')