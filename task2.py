import csv  # Импортируем csv
import json  # Импортируем json

csv1 = "input.csv"   # Переменная CSV-файла
json1 = "output.json" # Переменная JSON-файла

def task() -> None:  # Вводим функцию task, которая ничего не возвращает
    with open(csv1, "r", encoding="utf-8") as csv_file:   # Открывает входной CSV-файл в режиме чтения UTF-8
        reader = csv.DictReader(csv_file) # Создаём объект, который читает CSV и автоматически использует первую строку как заголовки столбцов, а каждую следующую строку превращает в словарь
        data = list(reader)  # Преобразуем reader в список словарей
    with open(json1, "w", encoding="utf-8") as json_file: # Открываем JSON с кодировкой UTF-8
        json.dump(data, json_file, indent=4, ensure_ascii=False)         # Преобразуем список data в JSON и записывает в файл indent=4 – добавляет отступы по 4 пробела для читаемости
if __name__ == '__main__':  # Проверяем, запущен ли скрипт напрямую
    task()  # Вызываем функцию конвертации
    with open(json1) as json_f:  # Выводим файл джисона для чтения
        for line in json_f:   # Запускаем цикл, который читает файл
            print(line, end="") # Выводим ответ