def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError
    minn= nums[0]
    maxx= nums[0]
    for i in nums:
        if i<minn:
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
    result=[]
    for i in  range (len(nums)):
         if nums[i]<=nums[i]:
            if nums[i] not in result:
                result.append(nums[i])
            else:
                continue
    return sorted(result)

print('unique_sored')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for i in mat:
        if type(i)==list or type(i)==tuple:
            for n in i:
                result.append(n)
        else:
            raise TypeError
    return result

print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], 'ab']))