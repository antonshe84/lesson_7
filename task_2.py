"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
 этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
  конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
 (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os


def parse_and_create(file_struct, dist_folder):
    """
        Функция парсинга структуры каталогов и файлов
    :param file_struct: файл структуры вида (первая строка - корневой каталог):
                        |--my_project
                            |--settings
                            |  |--__init__.py
    :param dist_folder: каталог, в котором будут созданы файлы и папки
    :return: создает каталоги и пустые файлы в соответствии со структурой
    """

    # читаем структуру в список
    with open(file_struct, "r", encoding="utf-8") as f:
        ls = [l.replace("\n", "").replace(" ", "").replace("-", "") for l in f.readlines()]
    # первый уровень - корневой каталог, читаем из первой строки
    level_1 = ls[0].replace("|", "")
    level_2, level_3, level_4 = "", "", ""
    ls = ls[1:]
    dirs = []
    files = []
    # последовательно выясняем уровни вложенности (зависит от колличества знаков "|") и определяем, файл или папка
    for st in ls:
        if st.count("|") == 1:  # если первый уровень вложенности
            st = st.replace("|", "")
            if st.find(".") > 0:                        # если файл
                files.append(os.path.join(level_1, st)) # добавляем в список файлов текущий файл,
                                                        # "склеивая" последовательно каталоги уровней ниже
            else:                                       # если каталог
                level_2 = st                            # то уровнем выше выставляем текущую папку
                dirs.append(os.path.join(level_1, st))  # добавляем в список каталогов текущую папку,
                                                        # "склеивая" последовательно каталоги уровней ниже
        elif st.count("|") == 2:  # если второй уровень вложенности
            st = st.replace("|", "")
            if st.find(".") > 0:
                files.append(os.path.join(level_1, level_2, st))
            else:
                level_3 = st
                dirs.append(os.path.join(level_1, level_2, st))
        elif st.count("|") == 3:  # если третий уровень вложенности
            st = st.replace("|", "")
            if st.find(".") > 0:
                files.append(os.path.join(level_1, level_2, level_3, st))
            else:
                level_4 = st
                dirs.append(os.path.join(level_1, level_2, level_3, st))
        elif st.count("|") == 4:  # если четвертый уровень вложенности
            st = st.replace("|", "")
            if st.find(".") > 0:
                files.append(os.path.join(level_1, level_2, level_3, level_4, st))
            else:
                dirs.append(os.path.join(level_1, level_2, level_3, level_4, st))

    print(f"Найденые каталоги: {dirs}")
    print(f"Найденые файлы: {files}")

    for d in dirs:
        dir_1 = os.path.abspath(os.path.join(dist_folder, d))
        if not os.path.exists(dir_1):
            os.makedirs(dir_1)
        else:
            print(f"Каталог {dir_1} уже существует")

    for fi in files:
        file_1 = os.path.abspath(os.path.join(dist_folder, fi))
        if not os.path.exists(file_1):
            with open(file_1, "w") as f:
                pass
        else:
            print(f"Файл {file_1} уже существует")

    print(f"Структура каталогов и файлов создана в папке: {os.path.abspath(dist_folder)}")

    return 0


if __name__ == '__main__':
    root = r"Projects"
    parse_and_create("config.yaml", root)
