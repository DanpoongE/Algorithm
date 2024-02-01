T = int(input())

for tc in range (1, T+1):
    N = int(input())
    empty_list = [[0]*N for _ in range(N)]
    r, c = 0, 0
    for i in range(1, N**2+1):
        empty_list[r][c] = i
        c += 1 # 가로 방향 전개
        if c == (N-1-r):
            r += 1 # 밑 방향 전개
            if r == (N-1)


    # print(f'#{tc}')
    # for r in empty_list:
    #     print(r)


    # 마지막(INDEX는 N-1) 에서 밑으로 쭉.