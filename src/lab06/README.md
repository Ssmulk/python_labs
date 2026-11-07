# Лабораторная работа 6 
## Задание A (cli_text.py)
Модуль `src/lab06/cli_text.py` используется для выполнения операций с текстовыми файлами через командную строку. В нём реализованы две команды: `cat` и `stats`. Первая команда (`cat --input <путь> [-n]`) позволяет прочитать файл и вывести его содержимое построчно. Если дополнительно указать параметр `-n`, каждая строка будет выведена с порядковым номером. Вторая команда (`stats --input <путь> [--top N]`) предназначена для анализа текста: она определяет общее число слов, количество различных слов и формирует список наиболее часто встречающихся слов. По умолчанию отображаются 5 самых популярных слов. Для чтения содержимого используется функция `read_text`, созданная в лабораторной работе №4, а обработка текста выполняется с помощью функций `normalize`, `tokenize`, `count_freq` и `top_n` из лабораторной работы №3. Разбор введённых параметров реализован с помощью библиотеки `argparse`. Также добавлена проверка, которая не позволяет указать нулевое или отрицательное значение параметра `--top`. Основная логика запуска программы находится в функции `main()`.
``` python
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text


def check_file(path: str) -> str:
    """Проверяет, что входной файл существует."""
    if not read_text(path):
        raise FileNotFoundError(f"Файл не найден: {path}")


def cmd_cat(path: str, numbered: bool) -> None:
    """Выводит файл построчно, при numbered=True — с номерами."""
    check_file(path)
    text = read_text(path)
    number = 1
    for line in text.splitlines():
        if numbered:
            print(f"{number}. {line}")
        else:
            print(line)
        number += 1


def cmd_stats(path: str, top: int) -> None:
    """Выводит топ-N самых частых слов файла."""
    check_file(path)
    text = read_text(path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов выводить (по умолчанию 5)")

    args = parser.parse_args()

    if args.command is None:
        parser.error("нужно указать подкоманду: cat или stats")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            if args.top <= 0:
                parser.error("--top должно быть положительным числом")
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main() 
```
### Сценарии проверки 
**Все команды выполняются из корневой папки python_labs, для запуска используется python3 -m.**
1. **cat — вывод содержимого файла**

Команда для вывода файла с нумерацией строк:
``` python
python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
```
**Результат**
![A задание](../../images/lab06/img%20A%201.png)

Команда для вывода файла без нумерации:
``` python
python3 -m src.lab06.cli_text cat --input data/samples/people.csv
```
**Результат**
![A задание](../../images/lab06/img%20A%202.png)

2. **stats — подсчёт частоты слов**

Для проверки используется файл `data/samples/people.txt`.

Команда для вывода пяти самых частых слов:
``` python
python3 -m src.lab06.cli_text stats --input data/samples/people.txt --top 5
```
**Результат**
![A задание](../../images/lab06/img%20A%203.png)

## Задание В (cli_convert.py)
Модуль `src/lab06/cli_convert.py` предназначен для конвертации файлов разных форматов с помощью командной строки. Он включает три подкоманды: `json2csv`, `csv2json` и `csv2xlsx`. Первая позволяет преобразовать данные из JSON в CSV, вторая — перенести информацию из CSV в JSON, а третья — создать Excel-файл на основе CSV. Для выполнения каждой команды необходимо указать два параметра: `--in`, определяющий путь к исходному файлу, и `--out`, задающий место сохранения результата. Для преобразования данных используются функции `json_to_csv`, `csv_to_json` и `csv_to_xlsx`, разработанные в лабораторной работе №5. Обработка команд и переданных аргументов реализована с помощью модуля `argparse`. Запуск программы осуществляется через главную функцию `main()`.
``` python 
import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных (JSON, CSV, XLSX)")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной .json файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной .csv файл")

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной .json файл")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной .xlsx файл")

    args = parser.parse_args()

    if args.cmd is None:
        parser.error("нужно указать подкоманду: json2csv, csv2json или csv2xlsx")

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
        print(f"Готово: {args.input} -> {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден ({e})")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
```
### Сценарии проверки

1. **json2csv — преобразование JSON в CSV**

Команда запуска:
``` python 
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
```
2. **csv2json — преобразование CSV в JSON**

Команда запуска:
``` python 
python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
```
3. **csv2xlsx — преобразование CSV в XLSX**

Команда запуска:
``` python 
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/cities.csv --out data/out/cities.xlsx
```

## Проверка справки --help
Для росмотра доступных подкоманд используются команды: 
``` python 
python3 -m src.lab06.cli_text --help
python3 -m src.lab06.cli_convert --help
```
![--help](../../images/lab06/img%20--help.png)

Можно получить справку по каждой подкоманде: 
``` python 
python3 -m src.lab06.cli_text cat --help
python3 -m src.lab06.cli_text stats --help
python3 -m src.lab06.cli_convert json2csv --help
python3 -m src.lab06.cli_convert csv2json --help
python3 -m src.lab06.cli_convert csv2xlsx --help
```
## Проверка ошибок 
Если отсутствует один из обязательных аргументов (`--input`, `--in` или `--out`), модуль argparse автоматически сообщает об ошибке и показывает, какие параметры необходимо добавить.
``` python 
python3 -m src.lab06.cli_convert json2csv
```
![error 1](../../images/lab06/img%20error%201%20.png)

Для подкоманды stats реализована отдельная проверка параметра `--top`. Его значение должно быть положительным целым числом. Если указать ноль или отрицательное число, программа завершит выполнение команды и выведет соответствующее сообщение об ошибке.
``` python 
python3 -m src.lab06.cli_text stats --input data/samples/text.txt --top -2
```
![error 2](../../images/lab06/img%20error%202.png)