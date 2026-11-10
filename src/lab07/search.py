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