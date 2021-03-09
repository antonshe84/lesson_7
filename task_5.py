"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
 размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
  которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
 а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""

import os


def scan_size(root_folder):
    dict_files = {}
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            if os.path.abspath(__file__) == os.path.join(root, f):  # если найден текущий файл скрипта, то пропускаем
                break
            for s in range(2, 13):                                  # последовательно берем степени 10
                if os.stat(os.path.join(root, f)).st_size < 10 ** s:   # проверяем в какой диапазон размеров входит файл
                    exp = os.path.splitext(os.path.join(root, f))[1][1:]    # получаем расширение файла
                    if 10 ** s in dict_files:
                        count = dict_files[10 ** s][0]
                        list_ext = dict_files[10 ** s][1]
                        if exp not in list_ext:
                            list_ext.append(exp)
                        dict_files[10 ** s] = (count + 1, list_ext)
                    else:
                        dict_files[10 ** s] = (1, [exp])
                    break
    dict_files = {k: dict_files[k] for k in sorted(dict_files)}     # сортируем словарь
    return dict_files


if __name__ == '__main__':

    for k, v in scan_size(os.getcwd()).items():
        print(f"{k:12d}: {v}")
    input("Press any key to exit")
