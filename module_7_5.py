import os
import time

directory = "."

def l_files():

    files = [f for f in os.listdir() if os.path.isfile(f)]

    print("Файлы в текущей папке:")
    print(files)

    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

l_files()

dirs = [d for d in os.listdir() if os.path.isdir(d)]
print("Папки в текущей папке:")
print(dirs)
if len(dirs):
    filepath = os.getcwd()
    for i in range(len(dirs)):
        dir_ = dirs[i]
        os.chdir(dir_)
        print(os.getcwd())
        l_files()
        os.chdir(filepath)



# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = os.getcwd()
#     filetime = os.path.getmtime(file)
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = os.path.getsize(file)
#     parent_dir = os.path.dirname(filepath)
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')