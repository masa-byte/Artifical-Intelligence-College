def calculate(ls):
    new_ls = [
        sum(item**2 for item in element) if isinstance(element, list) else element**2
        for element in ls
    ]
    return new_ls


if __name__ == "__main__":
    ls = [2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]
    result = calculate(ls)
    print(result)
