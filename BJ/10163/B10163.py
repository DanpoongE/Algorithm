N = int(input())  # 색종이 장수
board = [[0] * 1001 for _ in range(1001)]

for paper_num in range(1, N + 1):
    x, y, w, h = list(map(int, input().split()))  # 직사각형의 왼쪽아래 x,y와 가로 세로길이

    for r in range(y, y + h):
        for c in range(x, x + w):
            board[r][c] = paper_num

result = [0] * (N + 1)
for n in range(1, N+1):
    for i in range(1001):
        result[n] += board[i].count(n)

result.remove(result[0])
print(*result, sep='\n')