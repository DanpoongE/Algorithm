path = []

# def permutation(n):
#     if n == 4:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         permutation(n + 1)
#         path.pop()

# permutation(1)


def permutation2(n):
    if n == 6:
        print(path)
        return

    for i in range(1, 5):
        path.append(i)
        permutation2(n + 1)
        path.pop()

permutation2(1)