T=int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 행 탐색
    for i in range(9):
        if len(set(arr[i])) != 9:
            result -= 1
            break

    # 전치행렬
    new_arr = list(zip(*arr))

    # 열 탐색
    for i in range(9):
        if len(set(new_arr[i])) != 9:
            result -= 1
            break

    # 마지막으로 작은 격자 탐색
    for z in [0, 3, 6]:             # 3씩 끊어 셀건데
        temp_set = set()
        for r in range(3):
            for c in range(3):
                temp_set.add(arr[r+z][c+z])

        if len(temp_set) != 9:
            result -= 1
            break

    print(f'#{tc} {result}')
