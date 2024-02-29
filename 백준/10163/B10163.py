N = int(input())  # 색종이 장수
board = [[0] * 1001 for _ in range(1001)]

for _ in range(1, N + 1):
    x, y, w, h = list(map(int, input().split()))  # 직사각형의 왼쪽아래 x,y와 가로 세로길이

    for r in range(y, y + h):
        for c in range(x, x + w):
            board[r][c] += 1

result = []
for n in range(1, N+1):
    cnt = 0
    for i in range(1001):
        cnt += board[i].count(n)

    result.append(cnt)

print(*result, sep='\n')