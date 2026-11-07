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
**Все команды выполняются из корневой папки python_labs через терминал VS Code. Для запуска используется python3 -m.**
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
![A задание](../../images/lab06/img%20A%202.png)