def check_matrix(mat: list[list[float | int]]):
    if not mat:
        return 
    columns = len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError

def transpose(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)
    if not mat:
        return []
    rows = len(mat)
    columns = len(mat[0])
    result = []
    for j in range(columns):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    if not mat:
        return []
    columns = len(mat[0])
    result = []
    for j in range(columns):
        total = 0
        for i in range(len(mat)):
            total += mat[i][j]
        result.append(total)
    return result


if __name__ == "__main__":
    print('transpose:')
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1, 2], [3, 4]]))
    print(transpose([]))
    try:
        print(transpose([[1, 2], [3]]))
    except ValueError as error:
        print('ValueError', error)

    print('row_sums:')
    print(row_sums([[1, 2, 3], [4, 5, 6]]))
    print(row_sums([[-1, 1], [10, -10]]))
    print(row_sums([[0, 0], [0, 0]]))
    try:
        print(row_sums([[1, 2], [3]]))
    except ValueError as error:
        print("ValueError", error)

    print('col_sums:')
    print(col_sums([[1, 2, 3], [4, 5, 6]]))
    print(col_sums([[-1, 1], [10, -10]]))
    print(col_sums([[0, 0], [0, 0]]))
    try:
        print(col_sums([[1, 2], [3]]))
    except ValueError as error:
        print("ValueError", error)