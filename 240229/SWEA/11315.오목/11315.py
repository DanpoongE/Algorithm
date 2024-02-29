T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    # 1. 행으로 5개 검토
    for r in range(N):
        r_line = ''.join(arr[r])
        if 'ooooo' in r_line:
            result = 'YES'
            break

    # 2. 열로 5개 검토
    if result == 'NO':
        for j in range(N):
            c_list = []
            for i in range(N):
                c_list.append(arr[i][j])

            c_line = ''.join(c_list)
            if 'ooooo' in c_line:
                result = 'YES'
                break

    # 3. 대각선으로 5개 검토
    if result == 'NO':
        left_slash = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    left_slash.append(arr[i][j])

        left_slash_line = ''.join(left_slash)
        if 'ooooo' in left_slash_line:
            result = 'YES'

    if result == 'NO':
        right_slash = []

        for i in range(N):
            j = N - 1 - i
            right_slash.append(arr[i][j])

        right_slash_line = ''.join(right_slash)
        if 'ooooo' in right_slash_line:
            result = 'YES'

    print(f'#{tc}', result)