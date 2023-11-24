def remove(ls):
    new_ls = list(map(lambda x,y: 1 if x==y else 0, ls, ls[1:]))
    filtered = list(filter(lambda x: x==1, new_ls))
    return len(filtered)


if __name__ == "__main__":
    ls = "aateesttoovi"
    result = remove(ls)
    print(result)