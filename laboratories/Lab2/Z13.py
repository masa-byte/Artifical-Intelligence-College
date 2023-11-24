from itertools import zip_longest


def collect(ls):
    new_list = [
        [x + y for x, y in zip_longest(sublist1, sublist2, fillvalue=0)]
        for sublist1, sublist2 in zip(ls, ls[1:])
    ]
    return new_list


if __name__ == "__main__":
    ls = [[1, 3, 5], [2, 4, 6], [1, 2]]
    result = collect(ls)
    print(result)
