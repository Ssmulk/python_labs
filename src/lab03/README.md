# Лабораторная работа 2

## Задание A
Реализует набор функций для обработки текста: нормализацию строки с приведением к единому регистру и заменой «ё» на «е» (`normalize`), выделение слов с помощью регулярного выражения с поддержкой дефисов внутри слов (`tokenize`), подсчёт количества повторений каждого слова (`count_freq`) и определение топ-N наиболее часто встречающихся слов с сортировкой по частоте и алфавиту при одинаковых значениях (`top_n`). Функции не используют ввод и вывод данных и проверяются с помощью `assert` внутри файла. Общая логика для работы с текстом вынесена в отдельный модуль `src/lib/text.py`.
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует строку text.

    Если casefold = True - приводит к casefold.
    Если yo2e = True - заменяет все ё/Ё на е/Е.
    Убирает невидимые управляющие символы (например, \t, \r) -> 
    заменяет на пробелы, схлопывает повторяющиеся пробелы в один.
    """
    result = text

    if casefold:
        result = result.casefold()
    else:
        result = result.lower()

    if yo2e:
        result = result.replace("ё", "е")
        result = result.replace("Ё", "Е")

    result = result.replace("\t", " ")
    result = result.replace("\r", " ")
    result = result.replace("\n", " ")

    result = re.sub(r" +", " ", result)

    result = result.strip()

    return result


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на список слов (токенов).

    Словом считается последовательность символов \\w (буквы, цифры,
    подчёркивание), внутри которой может встречаться дефис,
    соединяющий две части слова (например, "по-настоящему").

    Всё остальное (знаки препинания, пробелы, эмодзи и т.д.)
    считается разделителем и в результат не попадает.
    """
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Считает, сколько раз встречается каждое слово.
    Возвращает словарь вида {слово: количество}.
    """
    freq: dict[str, int] = {}

    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает n самых частых слов из словаря частот freq.

    Пары (слово, частота) сортируются по убыванию частоты,
    а при равной частоте - по алфавиту (по возрастанию).
    """
    pairs = list(freq.items())

    pairs.sort(key=lambda pair: (-pair[1], pair[0]))

    return pairs[:n]


if __name__ == "__main__":  
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    # tokenize
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    # count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"aa": 2, "bb": 2, "cc": 1}
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
```

## Задание B
Программа получает весь текст из `stdin` до окончания ввода (`EOF`), выполняет его нормализацию и разбивает на слова с помощью функций из `src/lib/text.py`. Затем она подсчитывает общее и уникальное количество слов и выводит пять наиболее часто встречающихся слов в формате `слово:количество`. Файл программы находится в `src/lab03/01_text_stats.py`.
```python
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    raw_text = sys.stdin.read()
 
    normalized = normalize(raw_text)
    tokens = tokenize(normalized)
 
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)
 
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
 
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")
 
 
if __name__ == "__main__":
    main()
```
