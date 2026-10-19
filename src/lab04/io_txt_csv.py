import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает текстовый файл и возвращает всё его содержимое.

    Путь к файлу передаётся через path, а encoding задаёт кодировку.
    По умолчанию - UTF-8.

    Если файл не найден или его не удалось прочитать в указанной
    кодировке, возникают FileNotFoundError и UnicodeDecodeError 
    соответственно.
    Для пустого файла возвращается пустая строка.
    """
    path = Path(path)
    text = path.read_text(encoding=encoding)
    return text


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """
    Записывает данные из rows в CSV-файл.

    path задаёт путь к файлу, а header позволяет добавить названия
    столбцов в начало таблицы.

    Перед записью проверяется, что все строки содержат одинаковое
    количество элементов. Если задан заголовок, количество его
    элементов также должно совпадать с длиной строк.

    Если длина строк различается - ValueError.
    Если данных нет, файл всё равно создаётся: при наличии header
    в него записывается заголовок.

    Если файл уже существует, его старое содержимое заменяется.
    """
    path = Path(path)

    # сохраняем спроки в списке, чтобы проверить их перед записью
    rows_list = list(rows)

    # проверяем, что все строки одинаковой длины
    if len(rows_list) > 0:
        first_row_len = len(rows_list[0])

        for row in rows_list:
            if len(row) != first_row_len:
                raise ValueError(
                    "Все строки в rows должны иметь одинаковую длину"
                )

        if header is not None and len(header) != first_row_len:
            raise ValueError(
                "Длина header должна совпадать с длиной строк в rows"
            )

    # создаём родительскую папку, если её ещё нет
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows_list:
            writer.writerow(row)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV создан.")