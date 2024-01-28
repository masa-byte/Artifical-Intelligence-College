from functools import reduce
import itertools

arr = [1, 2, (3, 4), 5, [5, 9]]
for el in arr:
    if isinstance(el, list):
        print("list")
    elif isinstance(el, tuple):
        print("tuple")
    else:
        print("int")

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9]

print(list(map(lambda x, y: x + y, arr1, arr2)))
print(reduce(lambda x, y: x + y, arr1))

print(list(itertools.chain(arr1, arr2)))
print(list(itertools.compress(arr1, [True, False, True, False, True])))
for k, g in itertools.groupby(arr1, lambda x: x > 2):
    print(k, list(g), end=" ")
print()
print(list(itertools.pairwise(arr1)))
for x in list(itertools.tee(arr1, 3)):
    print(list(x), end=" ")
