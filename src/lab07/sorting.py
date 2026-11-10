
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
