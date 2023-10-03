# Модуль OS преставляет множество функций для работы с операционной системой, причем их поведение, как правило, \
# не зависит от ОС, по-этому программы остаются переносимыми:
# Для начала  работы нужно импортировать import OS

# os.chdir(past) # смена текущей дериктории
# os.getcwd() - текущая рабочая директория
# os.path.basename(path) # Базовое имя пути
# os.path.abspath(path) # возвращает нормализованный абсолютный путь.

import os
print(os.getcwd()) # /Users/Alekseisemenov/PycharmProjects/Seminars/Lessons/Lesson_4

# os.path.basename(path) # Базовое имя пути
print(os.path.basename('/Users/Alekseisemenov/PycharmProjects/Seminars/Lessons/Lesson_4')) # Lesson_4

# os.path.abspath(path) # возвращает нормализованный абсолютный путь.
print(os.path.abspath('lesson.py')) # /Users/Alekseisemenov/PycharmProjects/Seminars/Lessons/Lesson_4/lesson.py