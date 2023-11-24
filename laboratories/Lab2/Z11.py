from functools import reduce


def has_nested_list(ls):
    nested_list = list(map(lambda x: isinstance(x, list), ls))
    return any(nested_list)


def product(ls):
    new_ls = ls.copy()
    while has_nested_list(new_ls):
        new_ls = [
            item
            for element in new_ls
            for item in (element if isinstance(element, list) else [element])
        ]

    print(new_ls)
    return(reduce(lambda x,y: x*y, new_ls, 1))


if __name__ == "__main__":
    ls = [[1, 3, 5], [2, 4, [1, 2]], [1, 2, 3], 5]
    result = product(ls)
    print(result)
