# Лабораторная работа 2

## Задание A
```python
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


![A задание](../../images/lab02/img%20A.2.png)

def flatten(mat: list[list | tuple]) -> list:
    result = [] # Список для новой матрицы
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

![A задание](../../images/lab02/img%20A.3.png)

## Задание B 
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    columns = len(mat[0]) # Запоминаем число столбцов
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')
    result=[] # Пустой список для транспонированной матрицы
    for col in range (columns): # Проходимся по столбцам исходной матрицы
        newrow=[]
        for row in range (len(mat)): # Проходимся по строкам исходной матрицы
            newrow.append(mat[row][col])
        result.append(newrow)
    return result

![B задание](../../images/lab02/img%20B.1.png)

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    columns=len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица') # Проверка на равность
    sum_row=[]
    for row in mat:
        sum_row.append(sum(row)) # Сумма строки
    return sum_row

![B задание](../../images/lab02/img%20B.2.png)

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    columns=len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица') # Проверка на рваность 
    col=zip(*mat) # Группировка элементов по столбцам
    sum_col=[]
    for i in col:
        sum_col.append(sum(list(i))) # Сумма столбцов
    return sum_col    
![B задание](../../images/lab02/img%20B.3.png)

## Задание C
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:  # Проверка на кортеж
        raise TypeError('входные данные должны быть кортежем')

    gpa = round(rec[2], 2)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError('GPA должен быть в диапазоне от 0.0 до 5.0')

    fio = rec[0].split()
    if len(fio) == 0:
        raise ValueError('напиши имя')

    name = fio[0].lower()
    gr = rec[1]

    if len(gr) == 0:
        raise ValueError('напиши группу')

    if len(fio) == 3:
        fio1 = f'{name[0].upper() + name[1:]} {fio[1][0].upper()}.{fio[2][0].upper()}.'
    else:
        fio1 = f'{name[0].upper() + name[1:]} {fio[1][0].upper()}.'

    fio1 = f'{fio1.strip()}, гр. {gr.strip()}, GPA {gpa:.2f}'
    return fio1


print(format_record(('Иванов Иван Иванович', 'BIVT-25', 4.6)))
print(format_record(('Пктров Пётр', 'IKBO-12', 5.0)))
print(format_record(('Петров Пётр Петрович', 'IKBO-12', 5.0)))
print(format_record(('сидорова анна сергеевна', 'ABB-01', 3.999)))

![C задание](../../images/lab02/img%20C.png)