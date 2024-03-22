def dfs(level, val): #val == 행이 돌면서 곱해질 확률값
    global max_val
    if val <= max_val:
        return

    if level == N:
        if val > max_val:
            max_val = val
            return

    for i in range(N):
        if used[i] == 0:    # 사용된 적 없는 인덱스면
            used[i] = 1
            val *= arr[level][i] / 100
            dfs(level + 1, val)
            used[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    path = []
    max_val = 0 # 최대확률

    dfs(0, 1)
    print(max_val)




























# def dfs(level):
#     global chance
#     if level == N:
#         val = 1
#         for num in path:
#             val *= num
#         return answer.append(val)
#
#     for i in range(N):
#         if used[i] == 0:
#             used[i] = 1
#             path.append(arr[level][i] / 100)
#             dfs(level + 1)
#             path.pop()
#             used[i] = 0
#
# T = int(input())
# for x in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     chance = 1
#     path = []
#     used = [0] * N
#     answer = []
#     dfs(0)
#
#     ans = max(answer) * 100
#     print(f'#{x}', "{0:.6f}".format(ans))



    # while chance:
    #     j_list = chance.pop()
    #     val = 1
    #     r = 0
    #     for j in j_list:
    #         val *= arr[r][j] / 100
    #         r += 1
    #     answer.append(val)
    # ans = max(answer) * 100
