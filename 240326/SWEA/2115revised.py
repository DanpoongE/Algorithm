def row_max(lst):
    for r in range(N):  # 행마다 보는데
        row_max = []
        for c in range(M - N + 1):
            lst[r][c:c + M]


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    row_max = []
