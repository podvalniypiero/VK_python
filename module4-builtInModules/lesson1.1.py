#Написать функцию write_and_read, которая будет записывать в файл текст как параметр функции
# и читать текст из этого файла и передавать на выход функции.

import os

text = input()
current_dir_abs = os.getcwd()
file_path = os.path.join(os.path.abspath('/tmp'),'my_file')
# file_path = os.path.join(current_dir_abs, 'some_file')
def write_and_read(text):
    open(file_path, 'w').write(text)
    return open(file_path, 'r').read()

print(write_and_read(text))