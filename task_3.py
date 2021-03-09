"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
 скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
 (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
  решена, например, во фреймворке django.
"""

from os.path import join
from os import walk
from shutil import copytree


def templates_sort(project_folder):
    for root, dirs, files in walk(project_folder):      # рекурсивно сканируем папку с проектом
        for dir in dirs:
            # Если найден каталок "templates", и он не находится в корне проекта
            if dir.lower() == "templates" and join(root, dir) != join(project_folder, dir):
                # находим все папки шаблонов
                for rt, dt, ft in walk(join(root, dir)):
                    for d in dt:
                        try:
                            # копируем папку шаблона со всеми файлами и папками в папку "templates" в корне проекта
                            copytree(join(rt, d), join(project_folder, "templates", d))
                        except OSError as exc:
                            # если папка шаблона существует, то вызывается исключение OSError
                            # выясняем, нужно ли перезаписать шаблон
                            i = input(f'Шаблон "{join(rt, d)}" существует, перезаписать? (y/n)')
                            # если ввели "y" или "Y", то сопируем шаблон с опцией dirs_exist_ok, тоесть перезаписываем
                            if i.lower() == "y":
                                copytree(join(rt, d), join(project_folder, "templates", d), dirs_exist_ok=True)
                                print(f'Шаблон "{join(rt, d)}" перезаписан!')
                            else:
                                print(f'Шаблон "{join(rt, d)}" пропущен!')
                                pass
                        except Exception as exc:
                            print(f"Что то пошло не так: {exc}")
                            break
                        else:
                            print(f'Шаблон "{join(rt, d)}" скопирован в "{join(project_folder, "templates", d)}"')


if __name__ == '__main__':
    project_filder = r"Projects\my_project"
    templates_sort(project_filder)



