# empty_list = [[0, 0, 0, 0, 0, 0, 0] for _ in range(2)]
empty_list = [[0] * 7 for _ in range(2)]

N = int(input())

for p in range(4):
    empty_list[0][p] = N + p

    # empty_list[0][p] = N
    # N += 1 이렇게 하면 좀 더 문제 내용과 잘 맞음!

for q in range(4):
    empty_list[1][6-q] = N - q

print(empty_list)