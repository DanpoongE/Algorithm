t = int(input())
# hashnum = 1

for hash in range(1, t+1):
    N = int(input())

    # 2로 먼저 나눔. 나머지 없으면 한번더 num += 1
    # 나머지 생겨 -> 그만해. num = a
    # 3

    a = 0
    while N % 2 == 0:
        a += 1
        N = N / 2

    b = 0
    while N % 3 == 0:
        b += 1
        N = N / 3

    c = 0
    while N % 5 == 0:
        c += 1
        N = N / 5

    d = 0
    while N % 7 == 0:
        d += 1
        N = N / 7

    e = 0
    while N % 11 == 0:
        e += 1
        N = N / 11

    print(f'#{hash}', a, b, c, d, e)

