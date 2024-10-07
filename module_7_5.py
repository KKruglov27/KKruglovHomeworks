
import os
import time
from pathlib import Path

dir_way = r'F:\Программирование\Urban. Домашние работы\module_7_5'

"""
Создание папок и текстовиков
"""

print(os.getcwd())
new_text = open('Textovik_A1.txt', 'w', encoding='utf-8')
new_text.write('Это первый текстовый файл, созданный в пятой практической работе модуля 7')
new_text.close()
os.mkdir('This_NewFolder_1')
os.chdir('This_NewFolder_1')
new_text1 = open('Textovik_B3.txt', 'w', encoding='utf-8')
os.mkdir('This_NewFolder_2')
os.chdir('This_NewFolder_2')
new_text2 = open('Textovik_B2.txt', 'w', encoding='utf-8')
os.mkdir('This_NewFolder_3')
os.chdir('This_NewFolder_3')
new_text3 = open('Textovik_B1.txt', 'w', encoding='utf-8')
os.chdir(r'F:\Программирование\Urban. Домашние работы\module_7_5')
os.makedirs(r'Second_Folder_1\Second_Folder_2\Second_Folder_3')
os.chdir(r'F:\Программирование\Urban. Домашние работы\module_7_5\Second_Folder_1\Second_Folder_2\Second_Folder_3')
new_text = open('Textovik_C1.txt', 'w', encoding='utf-8')
new_text.write('Это текстовый файл, созданный в Second_Folder_3')
print(os.getcwd())


"""
Проверка искомых файлов.
"""

print()
print("FILE_INFO:")
print()

for root, dirs, files in os.walk(dir_way):
        for filename in files:
            if filename.startswith('Textovik_') or filename.endswith('.py'):
                file = os.path.join(root, filename)
                filepath = file
                file_data_create = os.stat(file).st_ctime
                file_last_open = os.stat(file).st_atime
                file_last_change = os.stat(file).st_mtime
                dara_create = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_data_create))
                last_open = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_open))
                last_change = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_change))
                file_size = os.stat(file).st_size
                parent_dir = os.path.basename(os.path.dirname(file))
                info = (f'Обнаружен файл: {filename}',
                f'Путь: {filepath}',
                f'Размер: {file_size} байт',
                f'Дата создания: {dara_create}',
                f'Дата последнего открытия: {last_open}',
                f'Дата последнего изменения: {last_change}',
                f'Родительская директория: {parent_dir}')
                for i in info:
                    print(i)
                print()
                continue

"""
Добавление новых строк.
"""

os.chdir(r'F:\Программирование\Urban. Домашние работы\module_7_5')
new_text = open('Textovik_A1.txt', 'a', encoding='utf-8')
new_text.write('Это вторая запись в Textovik_A1.txt, для проверки')
new_text.close()
os.chdir('This_NewFolder_1')
new_text1 = open('Textovik_B3.txt', 'w', encoding='utf-8')
new_text1.write('Это строка в файле Textovik_B1. Файл Textovik_B1 находится в директории First_Folder_1.')
new_text1.close()
os.chdir('This_NewFolder_2')
new_text2 = open('Textovik_B2.txt', 'w', encoding='utf-8')
new_text2.write('Это строка в файле Textovik_B2. Файл Textovik_B2 находится в директории First_Folder_2.')
new_text2.close()
os.chdir('This_NewFolder_3')
new_text3 = open('Textovik_B1.txt', 'w', encoding='utf-8')
new_text3.write('Это строка в файле Textovik_B3. Файл Textovik_B3 находится в директории First_Folder_3.')
new_text3.close()

"""
Проверка искомых файлов.
"""

print()
print("FILE_INFO:")
print()

for root, dirs, files in os.walk(dir_way):
        for filename in files:
            if filename.startswith('Textovik_') or filename.endswith('.py'):
                file = os.path.join(root, filename)
                filepath = file
                file_data_create = os.stat(file).st_ctime
                file_last_open = os.stat(file).st_atime
                file_last_change = os.stat(file).st_mtime
                dara_create = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_data_create))
                last_open = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_open))
                last_change = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_change))
                file_size = os.stat(file).st_size
                parent_dir = os.path.basename(os.path.dirname(file))
                info = (f'Обнаружен файл: {filename}',
                f'Путь: {filepath}',
                f'Размер: {file_size} байт',
                f'Дата создания: {dara_create}',
                f'Дата последнего открытия: {last_open}',
                f'Дата последнего изменения: {last_change}',
                f'Родительская директория: {parent_dir}')
                for i in info:
                    print(i)
                print()
                continue


"""
Придется сделать проверку через два запуска с раскомментированием нижней строки.

Иначе я получаю ошибку:

PermissionError: [WinError 5] Отказано в доступе: 'This_NewFolder_3' -> 'First_Folder_3', 
Пока что я с ней не разобрался. 

Я загружал на репозиторий несколько запакованных файлов,
но так предоставлять свою домашнюю работу нельзя, только одним файлом.py.

В любом случае лучше запустить нижние конструкции из отдельного .py.
"""

"""
Рекурсивное изменение подстрок в каталоге.
"""

# dir_way_b = r'F:\Программирование\Urban. Домашние работы\module_7_5'


old = "This_New"
new_name = "First_"
for root, dirs, files in os.walk(dir_way_b, topdown=False):
    for name in dirs:
        if name.startswith(old):
            directoryPath = os.path.join(root, name)
            parentDirectory = Path(directoryPath).parent
            os.chdir(parentDirectory)
            os.rename(name, name.replace(old, new_name))
print(f'Подстроки "{old}" в каталогах с наличием данной подстроки переименованы в "{new_name}".')


"""
Просто добавление новых строк в файлы.
"""

os.chdir(r'F:\Программирование\Urban. Домашние работы\module_7_5\First_Folder_1')
new_text1 = open('Textovik_B3.txt', 'a', encoding='utf-8')
new_text1.write('\nОписание в строке выше не является правдивым, это не Textovik_B1, теперь он не содержится в This_NewFolder_3.')
new_text1.close()
os.chdir('First_Folder_2')
new_text2 = open('Textovik_B2.txt', 'a', encoding='utf-8')
new_text2.write('\nОписание в строке выше является частично правдивым, это Textovik_B2, теперь он не содержится в This_NewFolder_2')
new_text2.close()
os.chdir('First_Folder_3')
new_text3 = open('Textovik_B1.txt', 'a', encoding='utf-8')
new_text3.write('\nОписание в строке выше не является правдивым, это не Textovik_B3, теперь он не содержится в This_NewFolder_1.')
new_text3.close()

"""
Проверка каталогов и директорий
"""
print()
print("DIR_INFO:")
print()

for root, dirs, files in os.walk(dir_way):
        for dirname in dirs:
            dir = os.path.join(root, dirname)
            dirpath = dirname
            dir_data_create = os.stat(dir).st_ctime
            dir_last_open = os.stat(dir).st_atime
            dir_last_change = os.stat(dir).st_mtime
            dara_create = time.strftime("%d.%m.%Y %H:%M", time.localtime(dir_data_create))
            last_open = time.strftime("%d.%m.%Y %H:%M", time.localtime(dir_last_open))
            last_change = time.strftime("%d.%m.%Y %H:%M", time.localtime(dir_last_change))
            file_size = os.stat(dir).st_size
            parent_dir = os.path.basename(os.path.dirname(dir))
            info = (f'Обнаружен файл: {dirname}',
            f'Путь: {dirpath}',
            f'Размер: {file_size} байт',
            f'Дата создания: {dara_create}',
            f'Дата последнего открытия: {last_open}',
            f'Дата последнего изменения: {last_change}',
            f'Родительская директория: {parent_dir}')
            for i in info:
                print(i)
            print()
            continue

"""
Повторная проверка искомых файлов.
"""

print()
print("FILE_INFO:")
print()

for root, dirs, files in os.walk(dir_way):
        for filename in files:
            if filename.startswith('Textovik_') or filename.endswith('.py'):
                file = os.path.join(root, filename)
                filepath = file
                file_data_create = os.stat(file).st_ctime
                file_last_open = os.stat(file).st_atime
                file_last_change = os.stat(file).st_mtime
                dara_create = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_data_create))
                last_open = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_open))
                last_change = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_last_change))
                file_size = os.stat(file).st_size
                parent_dir = os.path.basename(os.path.dirname(file))
                info = (f'Обнаружен файл: {filename}',
                f'Путь: {filepath}',
                f'Размер: {file_size} байт',
                f'Дата создания: {dara_create}',
                f'Дата последнего открытия: {last_open}',
                f'Дата последнего изменения: {last_change}',
                f'Родительская директория: {parent_dir}')
                for i in info:
                    print(i)
                print()
                continue

