def where_is_num(board, target):
    r_idx = 0
    c_idx = 0
    flag = 0

    for i in range(5):              # board 순회하다가
        for j in range(5):
            if board[i][j] == target:   # target 찾으면
                r_idx = i
                c_idx = j
                flag += 1
                break
        if flag == 1:
            break

    return r_idx, c_idx


board = [list(map(int, input().split())) for _ in range(5)]
call_nums = []
for __ in range(5):
    arr = list(map(int, input().split()))
    call_nums.extend(arr)

r_count = [0] * 5
c_count = [0] * 5
left_slash = 0
right_slash = 0
bingo = 0
cnt = 0

for nums in call_nums:                  # 사회자가 부르는 넘버
    r, c = where_is_num(board, nums)    # 그게 board의 어디에 있는지 파악해야 해.

    cnt += 1                            # 사회자가 부른 횟수

    r_count[r] += 1
    c_count[c] += 1
    if r == c:
        left_slash += 1
    if c == (4 - r):
        right_slash += 1

    if r_count[r] == 5:
        bingo += 1
        r_count[r] = 0

    if c_count[c] == 5:
        bingo += 1
        c_count[c] = 0

    if left_slash == 5:
        bingo += 1
        left_slash = 0

    if right_slash == 5:
        bingo += 1
        right_slash = 0

    if bingo >= 3:                  # 사회자가 불렀을 때 빙고가 2 -> 4개가 될 수도 있으므로
        print(cnt)
        break
