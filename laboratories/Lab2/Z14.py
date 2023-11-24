from functools import reduce


def summ(ls):
    sum_of_products = reduce(
        lambda x, y: x + y,
        [reduce(lambda x, y: x * y, sublist, 1) for sublist in ls],
        0,
    )
    return sum_of_products


if __name__ == "__main__":
    ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = summ(ls)
    print(result)
