def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat: # Обрабатыаем пустую матрицу
        return []
    columns = len(mat[0]) 
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')
    result=[]
    for col in range (columns):
        newrow=[]
        for row in range (len(mat)):
            newrow.append(mat[row][col])
        result.append(newrow)
    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    columns=len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')
    sum_row=[]
    for row in mat:
        sum_row.append(sum(row))
    return sum_row

def col_sums(mat: list[list[float | int]]) -> list[float]:
    columns=len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')
    col=zip(*mat)
    sum_col=[]
    for i in col:
        sum_col.append(sum(list(i)))
    return sum_col    


#print('transpose:')
#print(transpose([[1, 2, 3]]))
#print(transpose([[1], [2], [3]]))
#print(transpose([[1, 2], [3, 4]]))
#print(transpose([]))
#print(transpose([[1, 2], [3]]))

#print('row_sums:')
#print(row_sums([[1, 2, 3], [4, 5, 6]]))
#print(row_sums([[-1, 1], [10, -10]]))
#print(row_sums([[0, 0], [0, 0]]))
#print(row_sums([[1, 2], [3]]))
    
print('col_sums:')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))