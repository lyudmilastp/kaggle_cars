path = 'Z:/Сотрудники/'
import os

files_list = []
for root, dirs, files in os.walk(path, ) :
    for file in files:
        files_list.append(file)

files_list.sort()