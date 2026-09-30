def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError # Ошибка при пустом списке
    minn= nums[0] 
    maxx= nums[0]
    for i in nums:
        if i<minn: # Проверка по числам
            minn=i
        if i>maxx:
            maxx=i
    return minn, maxx

print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result=[] # Пустой список для сортировки чисел
    for i in nums:
        if i not in result:
            result.append(i) # Отсортированный список
         
    for i in range (len(result)): 
        for j in range (len(result)-1 -i):
            if result[j]>result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result # Отсортированный список чисел по возрастанию

print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    result = [] # Список для результата
    for i in mat:
        if type(i)==list or type(i)==tuple: # Проверка типа
            for n in i:
                result.append(n) # Добавление в матрицу
        else:
            raise TypeError('строка не строка строк матрицы')
    return result

print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], 'ab']))