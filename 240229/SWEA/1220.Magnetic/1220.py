T = 10

def c_cnt(col):
    cnt = 0

    # red 자성체를 체크
    is_red = False

    for row in range(N):
        #1. red 자성체 발견
        if arr[row][col] == 1:
            is_red = True
        #2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt += 1
        elif is_red and arr[row][col] == 2:
            cnt += 1
            is_red = False
    return cnt

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for col in range(N):
        result += c_cnt(col)

    print(f'#{tc}', result)


    # for c in range(N):      # 열 우선순회
    #     for r in range(N):
    #         if arr[r][c] != 0:
    #             conflict_num.append(arr[r][c])
    #
    #         if len(conflict_num) > 1:
    #             if conflict_num[-1] == 2 and conflict_num[-2] == 1:
    #                 conflict += 1
    #                 conflict_num.pop()
    #                 conflict_num.pop()