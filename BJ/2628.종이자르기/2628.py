W, L = list(map(int, input().split()))  # 가로, 세로의 길이
N = int(input())                        # 칼로 잘라야 하는 점선의 개수

# 가로로 자를 넘버
W_list = [0, W]
# 세로로 자를 넘버
L_list = [0, L]

for _ in range(N):
    cut = list(map(int, input().split()))

    if cut[0] == 0:     # 가로로 자르는 거면 세로 넘버에 PUSH
        L_list.append(cut[1])

    else:               # 세로로 자르는 거면
        W_list.append(cut[1])

# 가로 세로 자를 넘버 오름차순 정리해주고~
W_list.sort()
L_list.sort()

max_W = 0
max_L = 0
# 앞뒤로 한쌍씩 잘라줍니다.

for i in range(len(W_list) - 1):
    cut_W = W_list[i + 1] - W_list[i]
    if cut_W >= max_W:                  # 자른 길이가 최대 길이면 대체
        max_W = cut_W

for j in range(len(L_list) - 1):
    cut_L = L_list[j + 1] - L_list[j]
    if cut_L >= max_L:  # 자른 길이가 최대 길이면 대체
        max_L = cut_L

result = max_W * max_L

print(result)