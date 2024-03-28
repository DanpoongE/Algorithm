import sys
sys.stdin = open('2117.txt')

def served_houses(K):

    num_house = 0
    for dr in range(-K + 1, K): # 행
        ddr = abs(dr)
        for dc in range(-K + ddr + 1, K - ddr):   # 열
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N: # 행렬 범위 내에서
                if arr[nr][nc] == 1: # 집이 있다면
                    num_house += 1

    return num_house

def profit(K):
    num = served_houses(K)
    pf = num * M - K * K - (K - 1) * (K - 1)
    return pf, num

T = int(input())

for x in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = 0

    for r in range(N):
        for c in range(N):  # arr 선회하면서 서비스지역마다 이윤 확인
            area = 1
            while area <= N + 1:
                if profit(area)[0] >= 0 and profit(area)[1] > houses:   # 손해를 보지 않고, 서비스할 수 있는 집의 개수가 더 많다면
                    houses = profit(area)[1]
                area += 1
    
    print(f'#{x}', houses)