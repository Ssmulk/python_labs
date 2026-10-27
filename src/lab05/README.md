# Лабораторная работа 5

## Задание А
``` python
import csv
import json
from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv

def check_extension(path: str, extension: str) -> None:
    """
    Проверяет расширение файла.
    """
    if Path(path).suffix.lower() != extension:
        raise ValueError(f"Неверный тип файла: {path} (ожидалось {extension})")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON со списком словарей в CSV.
    Отсутствующие поля заполняются пустыми строками.
    """

    check_extension(json_path, ".json")
    check_extension(csv_path, ".csv")

    # Читаем файл функцией из ЛР4.
    text = read_text(json_path)

    if text.strip() == "":
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Преобразуем JSON в объект Python.
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError("Некорректный JSON") from error

    # Проверяем, что данные — непустой список.
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Проверяем, что каждый элемент — словарь.
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("В JSON должен быть список словарей")

    # Собираем названия колонок в порядке появления.
    columns = []

    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)

    if len(columns) == 0:
        raise ValueError("В JSON нет полей для создания колонок")

    # Преобразуем словари в строки таблицы.
    rows = []

    for item in data:
        row = []

        for column in columns:
            # Если ключ отсутствует, записываем пустую строку.
            row.append(item.get(column, ""))

        rows.append(row)

    # Записываем CSV функцией из ЛР4.
    write_csv(rows, csv_path, header=tuple(columns))


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON — список словарей.
    Все значения сохраняются как строки.
    """

    check_extension(csv_path, ".csv")
    check_extension(json_path, ".json")

    # Читаем CSV и преобразуем строки в словари.
    with open(csv_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, restval="")

        # Проверяем наличие заголовка.
        if not reader.fieldnames:
            raise ValueError("CSV пустой или без заголовка")

        # Проверяем названия колонок.
        for name in reader.fieldnames:
            if name.strip() == "":
                raise ValueError("В заголовке CSV есть пустое название")

        rows = list(reader)

    # Проверяем наличие строк с данными.
    if len(rows) == 0:
        raise ValueError("В CSV нет данных (есть только заголовок)")

    # Создаём папку для результата.
    path = Path(json_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Записываем JSON.
    with path.open("w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)

    
if __name__ == "__main__":
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")

    print("Тест конвертации JSON <-> CSV выполнены.")

    with open("data/lab05/samples/people.json", encoding="utf-8") as f:
        count_json = len(json.load(f))
    
    with open("data/lab05/out/people_from_json.csv", encoding="utf-8", newline="") as f:
        count_csv = len(list(csv.DictReader(f)))

    # проверка: количество записей до и после конвертации совпадает.

    print(f"Записей в JSON: {count_json}, строк в CSV: {count_csv}")
```
Код проверяет правильность расширений входного и выходного файлов, а также наличие исходного файла. Затем считывает его содержимое и проверяет, что оно не пустое. С помощью `json.loads()` данные преобразуются из JSON в Python-объект, после чего проверяется, что это непустой список словарей. Названия столбцов берутся из ключей первого словаря, при этом их порядок сохраняется. Далее код перебирает все словари и формирует строки таблицы. Если в каком-либо словаре отсутствует нужное поле, вместо него подставляется пустая строка. В конце сформированные данные и заголовки передаются в функцию `write_csv`, которая записывает их в CSV-файл в кодировке UTF-8.

``` python 
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON — список словарей.
    Все значения сохраняются как строки.
    """

    check_extension(csv_path, ".csv")
    check_extension(json_path, ".json")

    # Читаем CSV и преобразуем строки в словари.
    with open(csv_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, restval="")

        # Проверяем наличие заголовка.
        if not reader.fieldnames:
            raise ValueError("CSV пустой или без заголовка")

        # Проверяем названия колонок.
        for name in reader.fieldnames:
            if name.strip() == "":
                raise ValueError("В заголовке CSV есть пустое название")

        rows = list(reader)

    # Проверяем наличие строк с данными.
    if len(rows) == 0:
        raise ValueError("В CSV нет данных (есть только заголовок)")

    # Создаём папку для результата.
    path = Path(json_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Записываем JSON.
    with path.open("w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)
```
Код подготавливает папку для выходного JSON-файла, проверяет расширения файлов и наличие исходного CSV-файла. Затем открывает его в кодировке UTF-8 и считывает данные с помощью `csv.DictReader()`, который использует первую строку в качестве заголовков столбцов. Проверяется наличие заголовков и самих данных: если они отсутствуют, возникает ошибка. После этого все строки таблицы собираются в список словарей. В конце функция `json.dump()` записывает полученные данные в JSON-файл. Параметр `ensure_ascii=False` сохраняет кириллицу в читаемом виде, а `indent=2` добавляет отступы в два пробела для удобного чтения файла.

## Задание В
```python 
import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from src.lab05.json_csv import check_extension


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Преобразует CSV-файл в Excel.

    Первая строка CSV — заголовок.
    Лист называется Sheet1.
    Ширина столбцов зависит от содержимого, минимум 8 символов.
    Значения сохраняются как текст.
    """
    # Проверяем расширения файлов.
    check_extension(csv_path, ".csv")
    check_extension(xlsx_path, ".xlsx")

    # Читаем CSV.
    rows = []

    with open(csv_path, encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                rows.append(row)

    # Проверяем, что есть заголовок и хотя бы одна строка данных.
    if len(rows) < 2:
        raise ValueError(
            "CSV пустой или в нём нет данных (только заголовок)"
        )

    # Находим максимальную длину текста в каждом столбце.
    widths = {}

    for row in rows:
        for index, cell in enumerate(row):
            if len(cell) > widths.get(index, 0):
                widths[index] = len(cell)

    # Создаём Excel-книгу и лист.
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    # Переносим строки из CSV в Excel.
    for row in rows:
        sheet.append(row)

    # Устанавливаем ширину столбцов.
    for index, width in widths.items():
        letter = get_column_letter(index + 1)
        sheet.column_dimensions[letter].width = max(8, width)

    # Создаём папку для результата, если её нет.
    output_path = Path(xlsx_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Сохраняем Excel-файл.
    workbook.save(output_path)
    workbook.close()


if __name__ == "__main__":
    csv_to_xlsx(
        "data/lab05/samples/people.csv",
        "data/lab05/out/people.xlsx"
    )

    csv_to_xlsx(
        "data/lab05/samples/cities.csv",
        "data/lab05/out/cities.xlsx"
    )

    print("XLSX-файлы созданы.")
```
Код проверяет расширения входного CSV-файла и выходного XLSX-файла, а также наличие исходного файла. Затем считывает все непустые строки с помощью `csv.reader()` и сохраняет их в список. Проверяется, что таблица содержит заголовки и хотя бы одну строку с данными. Далее код определяет максимальную длину текста в каждом столбце, чтобы правильно настроить ширину колонок. Создаётся Excel-книга с помощью `Workbook`, а рабочий лист получает название `Sheet1`. Все строки переносятся в таблицу методом `ws.append()`. После этого ширина каждого столбца устанавливается по длине самого длинного значения, но не меньше 8 символов. В конце готовая таблица сохраняется в XLSX-файл по указанному пути.

## Краевые случаи 
- Отсутствие входного файла (FileNotFoundError): если файл не найден по указанному пути, возникает ошибка FileNotFoundError. Обрабатывать её должен вызывающий код, сами функции не выводят сообщения.
- Неверное расширение (`ValueError`): проверяются расширения входных и выходных файлов (`.json`, `.csv`, `.xlsx`). Если они не соответствуют ожидаемым, возникает ошибка ValueError.
- Пустой или некорректный JSON (`ValueError`): ошибка возникает, если файл пустой, содержит пустой список, неправильную структуру данных, элементы не в виде словарей, словари без ключей или некорректный JSON.
- Пустой или некорректный CSV (`ValueError`): ошибка возникает, если файл пустой, содержит только заголовки, пустые или повторяющиеся названия столбцов либо строки с большим количеством значений, чем предусмотрено заголовками.
- Различающиеся ключи в JSON: столбцы CSV формируются из всех ключей словарей, а отсутствующие значения заменяются пустыми строками.
- Типы данных: при преобразовании CSV в JSON все значения сохраняются как строки. При преобразовании JSON в CSV вложенные списки и словари записываются в виде JSON-строк, поэтому при обратном преобразовании их исходная структура автоматически не восстанавливается.

## Запуск 
Запуск выполняется из корня репозитория с помощью флага -m 
* Для задания В необходима библиотека `openpyxl`

## Тест-кейс А: 
**JSON → CSV**
Входной файл:
```python 
[
  {
    "name": "Alice",
    "age": 22,
    "city": "SPB"
  },
  {
    "name": "Bob",
    "age": 25,
    "city": "Moscow"
  },
  {
    "name": "Carlos",
    "age": 30,
    "city": "Kazan"
  },
  {
    "name": "Dana",
    "age": 21,
    "city": "SPB"
  },
  {
    "name": "Andrey",
    "age": 27,
    "city": "Novosibirsk"
  }
]
```
**Созданный файл**
```python 
name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan
Dana,21,SPB
Andrey,27,Novosibirsk
```

**Если у объектов разный набор ключей, недостающие значения заполняются пустыми строками.**

## Тест-кейс B: 
**CSV → JSON**
Входной файл:
```python
name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan
Dana,21,SPB
Andrey,27,Novosibirsk
```
**Созданный файл**
```python 
[
  {
    "name": "Alice",
    "age": "22",
    "city": "SPB"
  },
  {
    "name": "Bob",
    "age": "25",
    "city": "Moscow"
  },
  {
    "name": "Carlos",
    "age": "30",
    "city": "Kazan"
  },
  {
    "name": "Dana",
    "age": "21",
    "city": "SPB"
  },
  {
    "name": "Andrey",
    "age": "27",
    "city": "Novosibirsk"
  }
]
```
* Значение `age` - строка, т.к. в CSV отсутствуют типы. 

## Тест-кейс С: 
**CSV → XLSX**
Входной файл:
```python 
city,country,population
SPB,Russia,5384342
Moscow,Russia,13010112
Kazan,Russia,1306953
Novosibirsk,Russia,1620162
Yekaterinburg,Russia,1493749
```
**Созданный файл**
![B задание](../../images/lab05/img%20C.png)
