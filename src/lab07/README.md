# Лабораторная работа 7
## Задание А
``` python 
def linear_search(nums: list[int], x: int) -> int:
    """
    Находит первое появление числа x в списке nums.
    Принимает список чисел и значение, которое нужно найти.
    Возвращает индекс найденного числа или -1, если его нет.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for i, value in enumerate(nums):
        if value == x:
            return i
 
    return -1


def binary_search(sorted_nums: list[int], x: int) -> int:
    """
    Выполняет поиск числа x в отсортированном списке.
    Принимает список чисел, расположенных по возрастанию, и искомое число.
    Возвращает индекс числа, если оно найдено, иначе -1.
    Для неотсортированного списка результат может быть неправильным.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Подбирает два элемента списка, сумма которых равна target.
    Принимает список чисел и нужную сумму.
    Возвращает индексы двух подходящих элементов или None, если таких нет.
    Использует полный перебор всех возможных пар (O(n^2)).

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Находит два элемента, которые в сумме дают target, с помощью словаря.
    Принимает список чисел и необходимую сумму.
    Возвращает индексы найденных элементов или None, если пара не найдена.
    Выполняет поиск за один проход по списку (O(n)).
    """
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None
```
1. `linear_search`: Последовательно проверяет каждый элемент списка с помощью цикла `for`. Если находит нужное значение, сразу возвращает его индекс. Если элемент не найден, возвращает `-1`.

2. `binary_search`: Использует две границы поиска — `lo` и `hi`. На каждом шаге находит середину списка (`mid`) и сравнивает её значение с искомым. Если значение меньше искомого, поиск продолжается в правой части, если больше — в левой. Когда границы пересекаются, поиск заканчивается и возвращается `-1`. Для работы алгоритма список обязательно должен быть отсортирован.

3. `two_sum_brute`: Перебирает все возможные пары элементов с помощью двух вложенных циклов. Для каждой пары проверяет, равна ли сумма элементов заданному числу. Из-за перебора всех пар сложность алгоритма составляет `O(n²)`.

4. `two_sum_fast`: Проходит по списку один раз, используя словарь `seen`, в котором хранятся уже встреченные числа и их индексы. Для каждого элемента проверяет, есть ли в словаре число, которое в сумме с текущим даст нужный результат (`target - nums[j]`). Благодаря быстрому поиску по словарю сложность алгоритма составляет `O(n)`.

## Здание В
``` python 

def bubble_sort (nums):
    """
    Сортирует список по возрастанию и возвращает его копию.
    Исходный список остаётся без изменений.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums = list(nums)
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:  # Если перестановок не было, список уже отсортирован
            break
    return nums


def insertion_sort (nums):
    """
    Сортирует элементы списка по возрастанию и возвращает копию.
    Исходный список не изменяется.
    """
    nums = list(nums)
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums


def selection_sort (nums):
    """
    Упорядочивает элементы списка по возрастанию.
    Возвращает новый список, не изменяя исходный.
    """
    nums = list(nums)
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
```
1. Копирование списка: В начале каждой функции создаётся копия исходного списка с помощью `nums = list(nums)`. Благодаря этому первоначальный список остаётся неизменным после сортировки.

2. `bubble_sort`: Сравнивает соседние элементы и меняет их местами, если они расположены в неправильном порядке. После каждого прохода наибольший элемент оказывается в конце списка. Переменная `swapped` позволяет завершить сортировку раньше, если за проход не произошло ни одного обмена, то есть список уже отсортирован.

3. `insertion_sort`: Берёт очередной элемент (`current`) и сравнивает его с предыдущими. Все элементы, которые больше него, сдвигаются вправо, а сам элемент вставляется на подходящее место.

4. `selection_sort`: На каждом этапе находит наименьший элемент в неотсортированной части списка. Для этого используется поиск индекса минимума без встроенной функции `min`. Затем найденный элемент перемещается на текущую позицию `i`.

5. Обработка пустого списка и списка из одного элемента: ошибок не возникает, поскольку циклы не выполняются, а функция возвращает список без изменений.

## Задание С
``` python 

import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    """
    Тестирует функцию сортировки на случайных списках,
    сравнивая результат со встроенной функцией sorted().
    Принимает функцию для проверки и число тестов (по умолчанию 100).
    Возвращает количество выполненных тестов.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: получено {result}, ожидалось {sorted(nums)}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials


def check_search() -> int:
    """
    Проверяет правильность работы линейного и бинарного поиска
    на случайно созданных списках.
    Возвращает количество успешно выполненных испытаний.
    """
    trials = 100
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        x = random.randint(-60, 60)

        # Сравниваем линейный поиск с методом index()
        try:
            expected_lin = nums.index(x)
        except ValueError:
            expected_lin = -1
        actual_lin = linear_search(nums, x)
        assert actual_lin == expected_lin, f"linear_search ошиблась для поиска {x} в {nums}: получено {actual_lin}, ожидалось {expected_lin}"

        # Проверяем бинарный поиск на отсортированном списке
        sorted_nums = sorted(nums)
        try:
            expected_bin = sorted_nums.index(x)
        except ValueError:
            expected_bin = -1
        actual_bin = binary_search(sorted_nums, x)
        if expected_bin == -1:
            assert actual_bin == -1, f"binary_search не нашла элемент, которого нет: {x} в {sorted_nums}"
        else:
            assert actual_bin != -1 and sorted_nums[actual_bin] == x, f"binary_search вернула некорректный индекс {actual_bin} для {x} в {sorted_nums}"
    return trials


def check_two_sum(trials: int = 100) -> int:
    """
    Сравнивает результаты двух способов поиска пары чисел:
    полного перебора и поиска с помощью словаря.
    Принимает количество испытаний (по умолчанию 100).
    Возвращает число успешно пройденных тестов.
    """
    for _ in range(trials):
        n = random.randint(2, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        if random.random() > 0.3 and n >= 2:
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-200, 200)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        if res_brute is None:
            assert res_fast is None, f"two_sum_brute нашла None, а fast нашла {res_fast} для nums={nums}, target={target}"
        else:
            bi, bj = res_brute
            assert nums[bi] + nums[bj] == target, f"two_sum_brute вернула неверные индексы {res_brute}"
            assert res_fast is not None, f"two_sum_brute нашла пару, а fast вернула None"
            fi, fj = res_fast
            assert nums[fi] + nums[fj] == target, f"two_sum_fast вернула неверные индексы {res_fast}"
    return trials


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")
```
Модуль предназначен для проверки правильности работы реализованных алгоритмов на случайно сгенерированных данных.

1. `check_sorting(fn, trials=100)`: Сравнивает результат работы функции сортировки с результатом встроенной `sorted(nums)`. Дополнительно проверяет, что первоначальный список остался без изменений.

2. `check_search()`: Проверяет алгоритмы поиска. `linear_search` сравнивается со встроенным методом `list.index`. Если элемент не найден и возникает ошибка `ValueError`, правильным результатом считается `-1`. `binary_search` проверяется на предварительно отсортированных списках, включая случаи, когда искомого элемента нет. При наличии повторяющихся значений проверяется, что возвращённый индекс указывает на нужный элемент.

3. `check_two_sum(trials=100)`: Сравнивает работу двух алгоритмов поиска пары чисел — `two_sum_brute` и `two_sum_fast`. Также проверяет, что сумма элементов, найденных по возвращённым индексам, совпадает с `target`.

4. Генерация данных: Для тестирования создаются случайные списки длиной от 0 до 50 элементов. В них могут присутствовать отрицательные числа и повторяющиеся значения.

5. Обнаружение ошибок: Если результаты проверяемых функций отличаются от ожидаемых, возникает исключение `AssertionError`, которое содержит данные, на которых была обнаружена ошибка.

**Результат**
Запуск производиться через флаг -m
``` python 
python -m src.lab07.check
```
![check](../../images/lab07/img%20check.png)

## Задание D
``` python 
import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

LIMIT_N = 10_000  # квадратичные сортировки на большем n не запускаем


def make_data(n):
    """Случайный список из n чисел (seed задан один раз в main)."""
    return [random.randint(0, 10 * n) for _ in range(n)]


def bench_sorts(n):
    data = make_data(n)
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    for name, fn in (("bubble", bubble_sort), ("insertion", insertion_sort), ("selection", selection_sort)):
        if n > LIMIT_N:
            rows.append(("sort", n, name, "> 60 с"))  # слишком долго
        else:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, t))
    return rows


def bench_search(n=100_000, queries=10_000):
    data = make_data(n)
    xs = [random.choice(data) for _ in range(queries)]  # искомые значения есть в списке
    rows = []

    def run_linear():
        for x in xs:
            linear_search(data, x)

    t_lin = timeit.timeit(run_linear, number=1)
    rows.append(("search", n, "linear", t_lin))

    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)

    def run_binary():
        for x in xs:
            binary_search(sorted_data, x)

    t_bin = timeit.timeit(run_binary, number=1)
    rows.append(("search", n, "binary", t_bin))
    rows.append(("search", n, "sorted_for_binary", t_sort))
    rows.append(("search", n, "binary+sort", t_bin + t_sort))
    return rows


def bench_two_sum(n):
    # большой разброс значений, чтобы другой пары с такой суммой почти не было
    data = [random.randint(0, 10**12) for _ in range(n)]
    target = data[-2] + data[-1]  # пара гарантированно существует (в конце списка)
    rows = []
    t = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("two_sum", n, "brute", t))
    t = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
    rows.append(("two_sum", n, "fast", t))
    return rows


def print_table(rows):
    print(f"{'task':<10} | {'n':>8} | {'impl':<18} | {'seconds':>10}")
    print("-" * 50)
    for task, n, impl, sec in rows:
        if isinstance(sec, float):
            sec = f"{sec:.6f}"
        print(f"{task:<10} | {n:>8} | {impl:<18} | {sec:>10}")


def main():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows += bench_sorts(n)
    rows += bench_search()
    for n in (1_000, 10_000):
        rows += bench_two_sum(n)

    print_table(rows)
    csv_rows = []
    for task, n, impl, sec in rows:
        if isinstance(sec, float):
            sec = f"{sec:.6f}"
        csv_rows.append((task, n, impl, sec))
    write_csv(csv_rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))


if __name__ == "__main__":
    main()
```
1. Одинаковые исходные данные: В функции `main` один раз устанавливается `random.seed(42)`, чтобы результаты генерации были воспроизводимыми. Все алгоритмы в рамках одного измерения работают с одинаковым списком `data`.

2. Сортировки: Время работы встроенной `sorted` и трёх собственных алгоритмов сортировки измеряется с помощью `timeit.timeit(..., number=1)` для списков размером 1 000, 10 000 и 100 000 элементов. Для списка из 100 000 элементов медленные сортировки с квадратичной сложностью не запускаются. Вместо измеренного времени в таблице указывается `> 60 с` — примерная оценка на основе теоретической сложности (около 10¹⁰ операций).

3. Поиск: Проверяются 10 000 случайных запросов к списку из 100 000 элементов. Искомые значения выбираются непосредственно из списка. Для бинарного поиска время предварительной сортировки измеряется отдельно в строке `sorted_for_binary`, а в строке `binary+sort` указывается общее время сортировки и поиска.

4. Two Sum: В качестве `target` используется сумма двух последних элементов списка (`data[-2] + data[-1]`). Таким образом, подходящая пара точно существует и находится в конце списка. Числа генерируются в диапазоне до 10¹², чтобы вероятность появления других подходящих пар была очень маленькой и алгоритм перебирал почти все возможные варианты.

5. Вывод результатов: Результаты оформляются в виде таблицы с выравниванием столбцов с помощью f-строк. Таблица выводится в консоль и дополнительно сохраняется в файл `data/lab07/bench.csv` с помощью функции `write_csv`, написанной в лабораторной работе №4.

**Результат**
``` python 
task,n,impl,seconds
sort,1000,sorted,0.000081
sort,1000,bubble,0.030932
sort,1000,insertion,0.015675
sort,1000,selection,0.014291
sort,10000,sorted,0.001024
sort,10000,bubble,3.388711
sort,10000,insertion,1.729166
sort,10000,selection,1.353330
sort,100000,sorted,0.013089
sort,100000,bubble,> 60 с
sort,100000,insertion,> 60 с
sort,100000,selection,> 60 с
search,100000,linear,13.221946
search,100000,binary,0.017160
search,100000,sorted_for_binary,0.013022
search,100000,binary+sort,0.030182
two_sum,1000,brute,0.0a20231
two_sum,1000,fast,0.000108
two_sum,10000,brute,2.040298
two_sum,10000,fast,0.000997
```
![bench](../../images/lab07/img%20bench.png)

## Вывод
**Сортировки**
Пузырьковая сортировка, сортировка вставками и сортировка выбором имеют сложность O(n²). Это означает, что при увеличении размера списка в 10 раз количество операций возрастает примерно в 100 раз. Например, время работы `bubble_sort` увеличилось с 0,013858 с до 1,471899 с, то есть примерно в 106 раз.

Встроенная функция `sorted`, использующая алгоритм Timsort, работает со сложностью O(n log n). Поэтому при увеличении количества элементов в 10 раз время выполнения возрастает примерно в 10–13 раз. В наших замерах оно увеличилось с 0,000062 с до 0,000663 с, то есть примерно в 10,7 раза.

При размере списка 100 000 элементов квадратичные алгоритмы становятся слишком медленными, так как требуют порядка 10¹⁰ операций. Поэтому их запуск в данном случае нецелесообразен (в таблице для них указано время более 60 секунд). При этом `sorted` выполняет сортировку всего за 0,007391 с.

Среди реализованных квадратичных алгоритмов быстрее всего показала себя сортировка вставками (`insertion_sort`), а медленнее всего — пузырьковая сортировка (`bubble_sort`).

**Поиск**
Бинарный поиск можно применять только к отсортированному списку. Он сравнивает искомое значение `x` со средним элементом и на каждом шаге исключает половину оставшихся элементов. Если список не отсортирован, такой подход может привести к тому, что нужный элемент будет пропущен и результат окажется неправильным.

Однако предварительная сортировка имеет сложность O(n log n), тогда как линейный поиск выполняется за O(n). Поэтому, если нужно найти элемент всего один раз, сортировать список перед бинарным поиском невыгодно. Но при большом количестве запросов затраты на сортировку окупаются. Для списка из 100 000 элементов это происходит примерно после 17 запросов.

В проведённых замерах при 10 000 запросов линейный поиск занял 5,565852 с, а бинарный — 0,007753 с. С учётом предварительной сортировки общее время составило 0,015993 с, что значительно меньше времени линейного поиска.

Похожая ситуация наблюдается при сравнении алгоритмов `two_sum`. Быстрый алгоритм `two_sum_fast` со сложностью O(n) на списке из 10 000 элементов выполнился за 0,000722 с, тогда как `two_sum_brute` со сложностью O(n²) потребовал 1,158347 с. Это показывает, насколько сильно выбор алгоритма влияет на скорость выполнения программы.