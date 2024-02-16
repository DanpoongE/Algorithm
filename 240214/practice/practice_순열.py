# def f(i, k):
#     global min_v   # 나 최솟값 구할 거
#     if i==k:
#         # print(*P)
#         s = 0   # 선택한 원소의 합
#         for j in range(k):  # j행에 대해
#             s += arr[j][P[j]] # j행에서 P[j]열을 고른 경우의 합
#         if min_v > s:
#             min_v = s
#     else: # 다 돌지 않았다면
#         for j in range(i, k):  # P[i]자리에 올 원소 P[j]
#             P[i], P[j] = P[j], P[i]
#             f(i+1, k)
#             P[i], P[j] = P[j], P[i]     # 원상복구
#
#
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# P = [i for i in range(N)]
# min_v = 100
# f(0, N)
# print(min_v)


# 지금까지 고른 원소들의 합 추가
def f(i, k, s):
    global cnt
    global min_v   # 나 최솟값 구할 거
    cnt += 1
    if i==k:
        # print(*P)

        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else: # 다 돌지 않았다면
        for j in range(i, k):  # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]
            f(i+1, k, s+arr[i][P[j]])
            P[i], P[j] = P[j], P[i]     # 원상복구




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
f(0, N, 0)
print(min_v)