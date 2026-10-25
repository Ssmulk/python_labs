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
    csv_to_json("data/lab05/samples/cities.csv", "data/lab05/out/cities_from_csv.json")

    print("Тест конвертации JSON <-> CSV выполнены.")

    with open("data/lab05/samples/people.json", encoding="utf-8") as f:
        count_json = len(json.load(f))
    
    with open("data/lab05/out/people_from_json.csv", encoding="utf-8", newline="") as f:
        count_csv = len(list(csv.DictReader(f)))

    with open("data/lab05/samples/cities.csv", encoding="utf-8", newline="") as f:
        count_csv = len(list(csv.DictReader(f)))

    with open("data/lab05/out/cities_from_csv.json", encoding="utf-8") as f:
        count_json = len(json.load(f))

    # проверка: количество записей до и после конвертации совпадает

    print(f"Записей в JSON: {count_json}, строк в CSV: {count_csv}")