# Файлы
# абсолютные/относительные пути - abspath()/relpath()
import os
current_dir_abs = os.getcwd()
current_dir_rel = "."

# расширение и изменение директории
joined_path = os.path.join(current_dir_abs, 'some_file')
splitted_path = os.path.split(joined_path)

# OS.PATH.JOIN(root_path, child_path)
file_path1 = os.path.join(current_dir_abs, 'lesson1_files.py')

file_path = os.path.join(current_dir_abs, 'some_file')
if __name__ == '__main__':
    print(os.path.abspath(current_dir_abs)) # абсолютная директория
    print(os.path.relpath(current_dir_abs)) # f relpath() может принимать abs путь и преобразовывать его в rel
    print(os.path.relpath(current_dir_rel))
    print(os.path.abspath(current_dir_rel)) # f abspath() может принимать rel путь и преобразовывать его в abs

    print(joined_path) # модифицирует abs путь, добавив some_file в конце
    print(splitted_path) # tuple ('abs путь (отрезанная директория)','some_file')

    # проверка существования директории или файла
    print(os.path.exists(joined_path)) # False
    print(os.path.exists(current_dir_abs)) # True

    print(os.path.isdir(current_dir_abs)) # True

    print(os.path.isfile(current_dir_abs)) # False

    print(os.path.isfile(file_path1)) # True, в этом файле мы находимся
    print(os.path.isdir(file_path1))

    # СОЗДАТЬ ФАЙЛ И ЗАПИСАТЬ В НЕГО
    # OPEN(file_path, 'mode').function()
    open(file_path, 'w').write("Hello world")

    # ПРОЧИТАТЬ ФАЙЛ
    # БЛОК TRY/EXCEPT
    try:
        print(open(file_path, 'r').read())
    except FileNotFoundError:
        print(open(file_path, 'w').write("Hello, world"))
