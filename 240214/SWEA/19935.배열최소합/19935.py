def subset(arr):
    subset = []
    if len(subset) == N:
        return sum(subset)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_val = []
    for i in range(N):
        for j in range(N):
            empty_list = []
            empty_list.append(arr[i][j])

